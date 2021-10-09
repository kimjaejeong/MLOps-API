import numpy as np
import xgboost as xgb
from imblearn.under_sampling import RandomUnderSampler
import pandas as pd

def xgboost(x,y,testX,testY):
    trainD = xgb.DMatrix(x, label = y)
    param = {
        'colsample_bytree': 0.75, 'min_child_weight': 3,
        'eta': 0.3, 
        'max_depth': 5,  
        'objective': 'multi:softprob',  # softmax
        'eval_metric':'mlogloss',
        'num_class': 2}   # class 개수 = 2개 (binary class classification)
    model = xgb.train(params = param, dtrain = trainD, num_boost_round = 20)

    return model

def get_dummies(df,dummy_list):
    if not dummy_list:
        return df
    
    else:
        df_ = pd.get_dummies(data=df, columns=dummy_list)
        
        return df_

def preprocess(df):
#     더미데이터 변환
    df = get_dummies(df, ['OCCP_NAME_G_6_9','MATE_OCCP_NAME_G_6_9','LT1Y_PEOD_RATE','TEL_MBSP_GRAD_G_6_9','PAYM_METD_G_6_9','TEL_MBSP_GRAD_G_6_9','LINE_STUS','CBPT_MBSP_YN','SEX'])
    
#     AGE 비식별값은 따로 처리가 필요할 예정
    df['AGE'] = df['AGE'].str.replace(pat=r'*', repl=r'0', regex=True)
    
    for k in df.columns:
        df[k] = df[k].astype('float32')
        
    return df

def randomunder_ratio(i):
    randomunder_on_1 = 3858*(10-i)
    rus = RandomUnderSampler(sampling_strategy={0: randomunder_on_1})
    X_resampled, y_resampled = rus.fit_resample(X_train, y_train)
    model = xgboost(X_resampled,y_resampled,testX,testY)

    return model

def kb_classifier(model):
    # import the IrisClassifier class defined above
    from b_kb_classifier import KbClassifier

    # Create a iris classifier service instance
    kb_classifier_service = KbClassifier()

    # Pack the newly trained model artifact
    kb_classifier_service.pack('model', model)

    # Save the prediction service to disk for model serving
    saved_path = kb_classifier_service.save()


def init_set(relative_path):
    # 경로를 data에 따라 설정 -> 절대경로 지정 시, ./로 설정
    train = pd.read_csv(relative_path + 'train.csv')
    test = pd.read_csv(relative_path + 'test.csv')

    cols = train.columns
    cols = list(cols)

    cols[14] = 'OCCP_NAME_G_6_9'
    cols[19] = 'LAST_CHLD_AGE_6_9'
    cols[20] = 'MATE_OCCP_NAME_G_6_9'
    cols[54] = 'TEL_MBSP_GRAD_G_6_9'
    cols[64] = 'PAYM_METD_G_6_9'

    del_list = ['OCCP_NAME_G', 'LAST_CHLD_AGE', 'MATE_OCCP_NAME_G','TEL_MBSP_GRAD','PAYM_METD']
    for d in del_list:
        train.drop(d,axis=1)
        test.drop(d,axis=1)

    for d in del_list:
        train_c = pd.read_csv(relative_path + 'train_'+d+'.csv')
        test_c = pd.read_csv(relative_path + 'test_'+d+'.csv')
        train_c = train_c.iloc[: , -1]
        test_c = test_c.iloc[:, -1]
        train = pd.concat([train,train_c], axis=1)
        test = pd.concat([test,test_c], axis=1)

    train = train[cols]
    test = test[cols]

    object_cols = ['OCCP_NAME_G_6_9', 'MATE_OCCP_NAME_G_6_9', 'LT1Y_PEOD_RATE', 'SEX', 'TEL_MBSP_GRAD_G_6_9', 'CBPT_MBSP_YN', 'PAYM_METD_G_6_9', 'LINE_STUS']
    for o in object_cols:
        dic_o = {}
        for i,n in enumerate(train[o].unique()):
            dic_o[n] = i
        train = train.replace({o:dic_o})
        test = test.replace({o:dic_o})

    return train, test

if __name__ == "__main__":
    # 데이터 초기 세팅
    relative_path = "../data/"
    train, test = init_set(relative_path)

    # 데이터 전처리
    train = preprocess(train)
    test = preprocess(test)

    # 데이터 훈련 세팅
    X_train = train.drop('TARGET', axis=1)
    y_train = train.TARGET
    testX = test.drop('TARGET', axis=1)
    testY = test.TARGET
    X_train = X_train.to_numpy()
    y_train = y_train.to_numpy()
    testX = testX.to_numpy()
    testY = testY.to_numpy()


    # 모델링
    model = randomunder_ratio(4)

    # 모델 배포 - bentoml을 활용한 classifer 모델 생성
    kb_classifier(model)

    print("process finish")
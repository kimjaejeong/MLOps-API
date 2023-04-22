# from pandas.core.frame import DataFrame
from fastapi import FastAPI, Body
from pydantic import BaseModel
from xgboost import XGBClassifier

app = FastAPI()


# class Payload(BaseModel):
#     data : str = ""

@app.get("/")
def root():
    return {"Prediction": "Model!!!!"}


# @app.post("/predict")
# def inference(dict_data: dict = Body(...)):
#     # 모델 불러오기
#     filename = "model/xgb_model.model"
#     new_xgb_model = XGBClassifier()  # 모델 초기화
#     new_xgb_model.load_model(filename)  # 모델 불러오기
#
#     data = dict_data['data']
#     data = pd.DataFrame(data)
#     testX = data.iloc[:, :-1].to_numpy()
#
#     predY = new_xgb_model.predict(testX)
#
#     return predY.tolist()




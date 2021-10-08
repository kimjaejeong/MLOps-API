# 1) 모델 학습 코드
from sklearn import svm
from sklearn import datasets
from xgboost import XGBClassifier 
# import xgboost as xgb

# Load training data
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Model Training
model = XGBClassifier()
model.fit(X,y)

# clf = svm.SVC(gamma='scale')
# clf.fit(X, y)

# import the IrisClassifier class defined above
from assign_iris_classifier import IrisClassifier

# Create a iris classifier service instance
iris_classifier_service = IrisClassifier()

# Pack the newly trained model artifact
iris_classifier_service.pack('model', clf)

# Save the prediction service to disk for model serving
saved_path = iris_classifier_service.save()
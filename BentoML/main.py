# 1. 모델 학습 코드
from sklearn import svm
from sklearn import datasets
# import the IrisClassifier class defined above
from iris_classifier import IrisClassifier

# Load training data
iris = datasets.load_iris()
X, y = iris.data, iris.target

# Model Training
clf = svm.SVC(gamma='scale')
clf.fit(X, y)

# Create a iris classifier service instance
iris_classifier_service = IrisClassifier()

# Pack the newly trained model artifact
iris_classifier_service.pack('model', clf)

# Save the prediction service to disk for model serving
saved_path = iris_classifier_service.save("./bentoml")

# saved_path = iris_classifier_service.save_to_dir(path = "./bentoml")

print("종료")

####################save to dir 참고############################ -> codec utf-8 형태로 저장이 안되어 문제가 됨
# saved_path = iris_classifier_service.save_to_dir()
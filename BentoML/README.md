# Generated BentoService bundle - IrisClassifier:20211004153852_E3A994

This is a ML Service bundle created with BentoML, it is not recommended to edit
code or files contained in this directory. Instead, edit the code that uses BentoML
to create this bundle, and save a new BentoService bundle.

A minimum prediction service exposing a Scikit-learn model

# bentoml 실행
- export BENTOML_HOME='~/workspace/MLOps-API/BentoML/bentoml'
- bentoml serve IrisClassifier:latest
- <!-- bentoml serve KbClassifier:latest -->
- 확인: http://127.0.0.1:5000/


# Yatai 실행
- bentoml yatai-service-start
- 확인: http://127.0.0.1:3000/

# 도커로 띄우기
- bentoml containerize KbClassifier:latest -t kb-classifier
    - docker 권한 문제 해결 필요
- docker run -it --rm -d -p 5000:5000 [image-id]

# 도커 이미지 전체 삭제
- docker rmi $(docker images -q)


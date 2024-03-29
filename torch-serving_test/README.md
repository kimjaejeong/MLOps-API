### TorchServe 저장소 다운로드
```
mkdir torchserve-examples
cd torchserve-examples
git clone https://github.com/pytorch/serve.git
```

### DenseNet 이미지 분류 모델 다운로드
```
wget https://download.pytorch.org/models/densenet161-8d451a50.pth
```

### 모델을 Pytorch에서 TorchServe 형식으로 변환
- TorchServe는 확장명이 .mar인 모델 아카이브 형식을 사용
```commandline
torch-model-archiver --model-name densenet161 --version 1.0 --model-file serve/examples/image_classifier/densenet_161/model.py --serialized-file densenet161-8d451a50.pth --extra-files serve/examples/image_classifier/index_to_name.json --handler image_classifier
```

### 모델 호스팅
```commandline
mkdir model-store
mv densenet161.mar model-store/
```

### jdk 설치(참고)
- torch-serving을 위해서는 jdk가 필요. 
- 하지만 pytorch/torchserve:0.1-cpu 와 같은 base image가 있을 때, 설치 하지 않아도 될 것 같음
```commandline
# JDK 설치
sudo apt-get update
sudo apt-get install openjdk-17-jdk

# JAVA_HOME 환경변수 설정
export JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# 환경변수 영구 추가
~/.bashrc에 export PATH=$PATH:$JAVA_HOME/bin 확인

# 자바버전 확인
java -version
```

### 참고자료
- https://zephyrnet.com/ko/Torchserve%EB%A5%BC-%EC%82%AC%EC%9A%A9%ED%95%98%EC%97%AC-%EA%B7%9C%EB%AA%A8%EC%97%90-%EB%94%B0%EB%A5%B8-%EC%B6%94%EB%A1%A0%EC%9D%84%EC%9C%84%ED%95%9C-Pytorch-%EB%AA%A8%EB%8D%B8-%EB%B0%B0%ED%8F%AC/


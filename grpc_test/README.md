- install grpc
```
python -m pip install grpcio
python -m pip install grpcio-tools
```

- 실행 순서
1. .proto 파일을 작성하여 통신을 정의
2. codegen을 하여 파이썬 코드를 생성함
```
python -m grpc_tools.protoc \
      -I . \
      --python_out=. \
      --grpc_python_out=. \
      ./helloworld.proto
```
3. 서버측 코드를 작성하여 서버를 실행
4. 클라이언트측 코드를 작성하여 서버에 호출
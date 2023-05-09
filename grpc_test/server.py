from concurrent import futures
import logging

import grpc
import helloworld_pb2
import helloworld_pb2_grpc


# 서비스 이름으로 클래스를 생성하고, 서비스이름+{Servicer}의 클래스를 상속받습니다.
class Greeter(helloworld_pb2_grpc.GreeterServicer):

    # .proto에서 지정한 메서드를 구현하는데, request, context를 인자로 받습니다.
    # 요청하는 데이터를 활용하기 위해서는 request.{메시지 형식 이름} 으로 호출합니다.
    # 응답시에는 메서드 return에 proto buffer 형태로 메시지 형식에 내용을 적어서 반환합니다.
    def SayHello(self, request, context):
        return helloworld_pb2.HelloReply(message='Hello, %s!' % request.name)
    def SayHelloAgain(self, request, context):
        return helloworld_pb2.HelloReply(message=f'Hello again. {request.name}!')

def serve():
    port = '50051'
    # 서버를 정의할 때, futures의 멀티 스레딩을 이용하여 서버를 가동할 수 있습니다.
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # 위에서 정의한 서버를 지정해 줍니다.
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()
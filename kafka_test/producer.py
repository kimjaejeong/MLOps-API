# from confluent_kafka import Producer
# import socket
# conf = {"bootstrap.servers": "kafka-service:9092", "client.id": socket.gethostname()}
# producer = Producer(conf)
# producer.produce("test_topic", key="key_value", value="Hello, Kafka!")

from confluent_kafka import Producer
import socket

# Kafka 서버 설정
conf = {
    "bootstrap.servers": "localhost:9092",
    "client.id": socket.gethostname()
}

# Kafka Producer 인스턴스 생성
producer = Producer(conf)

# 메시지를 보낼 토픽과 데이터
topic = 'my_topic'
key = 'my-key'
value = 'Hello, Kafka!!'

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')


# 메시지 전송
producer.produce(topic, key=key, value=value, callback=delivery_report)

# 메시지 큐에 대기 중인 메시지 전송
producer.flush()
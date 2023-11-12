import pika
import base64


def encode_file():
    with open('../api/departuredelays.csv', 'rb') as f:
        return f.read()


def send_message(file=None):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='message-sender')
    channel.basic_publish(exchange='', routing_key='message-sender', body='hello')
    print('File Sent [x]')
    connection.close()


if __name__ == "__main__":
    send_message()
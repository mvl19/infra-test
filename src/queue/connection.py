import pika


class RMQ:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

    def send_message(self, file):
        channel = self.connection.channel()
        channel.queue_declare(queue='message-sender')
        with open(file, 'rb') as f:
            channel.basic_publish(exchange='', routing_key='message-sender', body=f.read())
        print('File Sent [x]')
        self.connection.close()
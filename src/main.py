from fastapi import FastAPI, Response, UploadFile, File
import uvicorn
import pika

app = FastAPI()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


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


@app.get("/")
async def root():
    return {"message": "Hello there!"}


@app.get("/api/v1/download", response_class=OctetStreamResponse)
async def get_csv():
    with open('../src/api/file.csv', 'rb') as file:
        return Response(
            file.read(),
            media_type="application/octet-stream"
        )


@app.post("/api/v1/generate")
async def generate(file: UploadFile = File(...)):
    try:
        content = file.file.read()
        with open('../src/api/file.csv', 'wb') as file:
            file.write(content)
            return {'status': 'success'}
    except Exception:
        return {'message': 'Error occurred uploading the file'}


@app.get('/api/v1/send_mq')
async def send_mq():
    try:
        rm = RMQ()
        rm.send_message('../src/api/file.csv')
        return {'status': 'success'}
    except Exception as e:
        return {'status': f'Exception {e} encountered'}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)

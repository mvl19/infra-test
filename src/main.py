from fastapi import FastAPI, Response, UploadFile, File
from api.download import OctetStreamResponse
import uvicorn
from fastapi.responses import StreamingResponse
import io

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/download/", response_class=OctetStreamResponse)
async def get_csv():
    with open('api/file.csv', 'rb') as file:
        return Response(
            file.read(),
            media_type="application/octet-stream"
        )


@app.post("/generate/")
async def generate(file: UploadFile = File(...)):
    try:
        content = file.file.read()
        with open('file.csv', 'wb') as file:
            file.write(content)
    except Exception:
        return {'message': 'Error occurred uploading the file'}


@app.get('/send_mq/')
async def send_mq():
    pass


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)

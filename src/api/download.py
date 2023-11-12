from fastapi import FastAPI, Response
app = FastAPI()


class OctetStreamResponse(Response):
    media_type = "application/octet-stream"


"""@app.get("/download", response_class=OctetStreamResponse)
async def get_csv():
    # with open('departuredelays.csv', 'r') as file:
    #     stream = io.StringIO(file.read())
    #     response = StreamingResponse(iter([stream.getvalue()]), media_type='text_csv')
    #     response.headers["Content-Disposition"] = "attachment; filename=download.csv"
    #     return response
    with open('departuredelays.csv', 'rb') as file:
        return Response(
            file.read(),
            media_type="application/octet-stream"
        )
"""

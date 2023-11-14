from fastapi import FastAPI, File, UploadFile
from typing import List

app = FastAPI()


@app.post("/files/")
async def create_file(file: List[bytes] = File()):
    return {"file_size": [len(i) for i in file]}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    return {"filename": file.filename}



if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='127.0.0.1', port=8000)
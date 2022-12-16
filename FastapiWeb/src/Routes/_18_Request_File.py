from fastapi import FastAPI, File, UploadFile
from typing import List
from fastapi.responses import HTMLResponse

app = FastAPI()

# files will be uploaded as form data, contents will be received as bytes
@app.post("/files/")
async def create_file(files: List[bytes]=File(default=None)):
    return {"file_size": [len(file) for file in files]}

# Upload file uses spooled file, work for bigger file
@app.post("/uploadfile/")
async def create_upload_file(files: List[UploadFile]):
    return {"filename": [file.filename for file in files]}

# Multiple file upload
@app.post("/UploadMultipleFiles/")
async def upload_multiple_file(files: List[UploadFile]):
    return {"filenames": [file.filename for file in files]}

# return HTML content at the endpoint path
@app.get("/")
async def main():
    content = """
<body>
<form action="/files/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
<form action="/UploadMultipleFiles/" enctype="multipart/form-data" method="post">
<input name="files" type="file" multiple>
<input type="submit">
</form>
</body>
    """
    return HTMLResponse(content=content)

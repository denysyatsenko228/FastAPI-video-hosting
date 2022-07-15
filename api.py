import shutil
from typing import List
from fastapi import APIRouter, UploadFile, File, Form, Request
from fastapi.responses import JSONResponse

from schemas import UploadVideo, GetVideo, User, Message


video_router = APIRouter()


@video_router.post("/")
async def root(title: str = Form(...), description: str = Form(...), file: UploadFile = File(...)):
    info = UploadVideo(title=title, description=description)
    with open(f'{file.filename}', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    return {"filename": file.filename, "info": info}


@video_router.post("/img")
async def upload_image(files: List[UploadFile] = File(...)):
    for img in files:
        with open(f'{img.filename}', 'wb') as buffer:
            shutil.copyfileobj(img.file, buffer)

    return {"filename": "Great!"}


@video_router.get("/video", response_model=GetVideo, responses={404: {"model": Message}})
async def get_video():
    user = {"id": 25, "name": "Dudets"}
    video = {'title': 'Test', 'description': "Description of the title"}
    info = GetVideo(user=user, video=video)
    return JSONResponse(status_code=200, content=info.dict())


@video_router.get("/test")
async def get_video(req: Request):
    print(req.base_url)
    return {}

from typing import List

from fastapi import UploadFile, APIRouter, Depends, File, Form
from starlette.background import BackgroundTasks
from starlette.templating import Jinja2Templates

from .models import User, Video
from .schemas import GetListVideo
from .services import save_video
from user.auth import current_active_user


video_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@video_router.post("/")
async def create_video(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...),
        user: User = Depends(current_active_user)
):
    return await save_video(user, file, title, description, back_tasks)


@video_router.get("/user/{user_pk}", response_model=List[GetListVideo])
async def get_list_video(user_pk: str):
    video_list = await Video.objects.filter(user=user_pk).all()
    return video_list

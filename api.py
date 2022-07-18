from fastapi import APIRouter, UploadFile, File, Form, BackgroundTasks
from starlette.responses import StreamingResponse

from models import User

from schemas import GetVideo, Message

from services import save_video


video_router = APIRouter()


@video_router.post("/")
async def create_video(
        back_tasks: BackgroundTasks,
        title: str = Form(...),
        description: str = Form(...),
        file: UploadFile = File(...)):

    user = await User.objects.first()
    return await save_video(user, file, title, description, back_tasks)


@video_router.get("/video/{video_pk}", response_model=GetVideo, responses={404: {"model": Message}})
def get_video(video_pk: int):
    # file = await Video.objects.select_related('user').get(pk=video_pk)
    file_like = open('media/lesson3.mp4', mode='rb')
    return StreamingResponse(file_like, media_type="video/mp4")

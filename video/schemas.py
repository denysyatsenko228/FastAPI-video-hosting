from pydantic import BaseModel


class UploadVideo(BaseModel):
    title: str
    description: str


class GetListVideo(BaseModel):
    id: int
    title: str
    description: str
    like_count: int


class GetVideo(GetListVideo):
    pass


class Message(BaseModel):
    message: str
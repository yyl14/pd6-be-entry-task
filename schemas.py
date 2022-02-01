from pydantic import BaseModel


class PostIn(BaseModel):
    author: str
    title: str
    content: str


class PostOut(BaseModel):
    id: int
    author: str
    title: str
    content: str

    class Config:
        def __init__(self):
            pass

        orm_mode = True


class CommentIn(BaseModel):
    author: str
    content: str


class CommentOut(BaseModel):
    id: int
    author: str
    content: str
    post_id: int

    class Config:
        def __init__(self):
            pass

        orm_mode = True

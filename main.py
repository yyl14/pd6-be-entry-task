from fastapi import FastAPI, Depends, HTTPException
import models
import schemas
from config import app_config
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from typing import Optional

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title=app_config.title,
    docs_url=app_config.docs_url,
    redoc_url=app_config.redoc_url,
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/post", response_model=schemas.PostOut)
async def add_post(post: schemas.PostIn, db: Session = Depends(get_db)) -> schemas.PostOut:
    new_post = models.Post(author=post.author, title=post.title, content=post.content)
    db.add(new_post)
    db.commit()
    return new_post


@app.delete("/post")
async def delete_post(post_id: int, db: Session = Depends(get_db)) -> str:
    db.query(models.Comment).filter(models.Comment.post_id == post_id).delete()
    db.query(models.Post).filter(models.Post.id == post_id).delete()
    db.commit()
    return f"Post id {post_id} is deleted."


@app.get("/post/{post_id}", response_model=schemas.PostOut)
async def read_post(post_id: int, db: Session = Depends(get_db)) -> schemas.PostOut:
    return db.query(models.Post).filter(models.Post.id == post_id).first()


@app.get("/post", response_model=list[schemas.PostOut])
async def browse_post(db: Session = Depends(get_db)) -> list[schemas.PostOut]:
    return db.query(models.Post).all()


@app.patch("/post/{post_id}", response_model=schemas.PostOut)
async def edit_post(post_id: int, title: Optional[str] = None, content: Optional[str] = None,
                    db: Session = Depends(get_db)) -> schemas.PostOut:
    if title is not None:
        db.query(models.Post).filter(models.Post.id == post_id).update(dict(title=title))
    if content is not None:
        db.query(models.Post).filter(models.Post.id == post_id).update(dict(content=content))
    db.commit()
    new_post = db.query(models.Post).get(post_id)
    return new_post


@app.post("/post/{post_id}/comment", response_model=schemas.CommentOut)
async def add_comment(post_id: int, comment: schemas.CommentIn, db: Session = Depends(get_db)) -> schemas.CommentOut:
    new_comment = models.Comment(author=comment.author, content=comment.content, post_id=post_id)
    db.add(new_comment)
    db.commit()
    return new_comment


@app.get("/post/{post_id}/comment", response_model=list[schemas.CommentOut])
async def browse_comment(post_id: int, db: Session = Depends(get_db)) -> list[schemas.CommentOut]:
    # return db.query(models.Post).get(post_id).comments
    return db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from database import Base


class Post(Base):
    __tablename__ = "post"

    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    # comments = relationship("Comment", back_populates="post")


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True)
    author = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    post_id = Column(Integer, ForeignKey("post.id"), nullable=False)
    # post = relationship("Post", back_populates="comments")

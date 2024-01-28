from pydantic import EmailStr
from sqlalchemy import ForeignKey, Integer, String, Column, Date, DateTime
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = 'users'
    
    username = Column(String, primary_key=True)
    password = Column(String, nullable=False)
    email = Column(String)
    full_name = Column(String, nullable=False)
    gender = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    created_time = Column(DateTime, nullable=False)
    articles = relationship("Article", back_populates="owner")
    
class Article(Base):
    __tablename__ = 'articles'
    
    id = Column(Integer, primary_key=True)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    owner_username = Column(String, ForeignKey('users.username'))
    
    owner = relationship("User", back_populates="articles")
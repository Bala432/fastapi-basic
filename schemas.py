from datetime import datetime, date
from pydantic import BaseModel

class ArticleBase(BaseModel):
    title : str
    content : str
    
class ArticleCreate(ArticleBase):
    pass

class Article(ArticleBase):
    id : int
    
    class Config:
        orm_mode = True
    
class UserBase(BaseModel):
    username : str 
    full_name : str
    date_of_birth : date
    gender : str
    email : str
    created_time : datetime = datetime.now()
    
class UserCreate(UserBase):
    password : str
    
    
class UserUpdate(UserBase):
    pass

class User(UserBase):
    articles : list[Article] = []
    
    class Config:
        orm_mode = True
    

    

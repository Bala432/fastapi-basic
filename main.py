from fastapi import FastAPI, Depends
from database import SessionLocal, engine
from sqlalchemy.orm import Session
import models
import schemas
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()
        
@app.post('/user/{username}/create-article/', response_model = schemas.ArticleCreate)
def create_article(request: schemas.Article, username : str, db: Session = Depends(get_db)):
    article = models.Article(title=request.title,content=request.content,owner_username=username)
    db.add(article)
    db.commit()
    db.refresh(article)
    return article

@app.get('/get-articles-list/', response_model = list[schemas.Article])
def get_articles( db: Session = Depends(get_db)):
    articles = db.query(models.Article).all()
    return articles

@app.get('/article/{article_id}/', response_model = schemas.Article)
def get_article(article_id: int, db: Session = Depends(get_db)):
    article = db.query(models.Article).filter(models.Article.id == article_id )
    return article
    
@app.post('/create-user/', response_model=schemas.User)
def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
    new_user = models.User(username=request.username, password=request.password,email=request.email,
                    full_name=request.full_name,gender=request.gender, date_of_birth=request.date_of_birth,
                    created_time=datetime.now())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get('/get-users-list/', response_model = list[schemas.User])
def get_users_list(db : Session = Depends(get_db)):
    users_list = db.query(models.User).all()
    return users_list

@app.get('/get-user/{username}', response_model = schemas.User)
def get_user( username : str, db : Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username==username).first()
    return user
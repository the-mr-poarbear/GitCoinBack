from fastapi import Body, Depends, FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware
# from models import Users , Base
# from database import SessionLocal, engine
# from schemas import UserSch






from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship














import datetime
from typing import Union
import pydantic as _pydantic
from pydantic import BaseModel


class UserSch(BaseModel):
    name  : str
    stars : int
    commits  : int
    energyBoost : int
    touchBoost : int
    maxEnergy : int

class PurchesSch(BaseModel):
    user  : str
    item : str


class ItemSch(BaseModel):

    name  : str
    starsBoost : int
    price  : int








from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./GitCoin.db'
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread': False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


class Users(Base):
    __tablename__ = "users"

    name = Column(String , primary_key=True)
    stars = Column(Integer) #profit
    commits = Column(Integer) #coins
    energyBoost = Column(Integer) 
    touchBoost = Column(Integer)
    maxEnergy = Column(Integer) 



class Purcheses(Base):
    __tablename__ = "purcheses"

    user = Column(String , ForeignKey('users.name'), primary_key=True)
    item = Column(String , ForeignKey('items.name'), primary_key=True)
    

class Items(Base):
    __tablename__ = "items"

    name = Column(String , primary_key=True)
    price = Column(Integer) 
    starsBoost = Column(Integer) 

















Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = {
    "http://localhost:5173",
    "http://127.0.0.1:5173",
    'http://10.0.2.2:8000',
    'https://2nenfombw5.loclx.io'
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    #allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers = ["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get('/')
def default():
    return {'hi'}

@app.get("/getuser/{name}" )
async def getUsers(name ,  db : Session = Depends(get_db)):
    return db.query(Users).filter(Users.name == name).first()

@app.post("/create")
def CreateUser(user:UserSch , db : Session = Depends(get_db)):

    user_model = Users()
    user_model.name = user.name 
    user_model.commits = user.commits
    user_model.stars = user.stars
    user_model.energyBoost = user.energyBoost 
    user_model.maxEnergy = user.maxEnergy
    user_model.touchBoost = user.touchBoost
    
    db.add(user_model)
    db.commit()

    return {'done'}
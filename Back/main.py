from fastapi import Body, Depends, FastAPI, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session

from fastapi.middleware.cors import CORSMiddleware
from Back import models , schemas
from Back.database import SessionLocal, engine
models.Base.metadata.create_all(bind=engine)

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


@app.get("/getuser/{name}" )
def getUsers(name ,  db : Session = Depends(get_db)):
    return db.query(models.Users).filter(models.Users.name == name).first()

@app.post("/")
def CreateUser(user:schemas.UserSch , db : Session = Depends(get_db)):

    user_model = models.Users()
    user_model.name = user.name 
    user_model.commits = user.commits
    user_model.stars = user.stars
    user_model.energyBoost = user.energyBoost 
    user_model.maxEnergy = user.maxEnergy
    user_model.touchBoost = user.touchBoost
    
    db.add(user_model)
    db.commit()

    return user
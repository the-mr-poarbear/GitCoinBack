from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


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
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
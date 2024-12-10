from pydantic import BaseModel
from typing import List

class PointBase(BaseModel):
    name: str
    coordinates: List[float]

class PointCreate(PointBase):
    pass

class PointResponse(BaseModel):
    id: int
    name: str
    coordinates: List[float]

    class Config:
        orm_mode = True

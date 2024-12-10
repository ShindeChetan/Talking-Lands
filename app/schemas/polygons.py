from pydantic import BaseModel
from typing import List

class PolygonBase(BaseModel):
    name: str
    coordinates: List[List[float]]

class PolygonCreate(PolygonBase):
    pass

class PolygonResponse(BaseModel):
    id: int
    name: str
    coordinates: List[List[float]]

    class Config:
        orm_mode = True

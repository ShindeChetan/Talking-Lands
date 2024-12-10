from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, TIMESTAMP
from geoalchemy2 import Geometry
from app.database import Base

class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    location = Column(Geometry("POINT"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Correct default value

class Polygon(Base):
    __tablename__ = "polygons"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    area = Column(Geometry("POLYGON"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())  # Correct default value

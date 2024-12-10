from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.models import Point
from app.schemas.points import PointCreate, PointResponse
from geoalchemy2.shape import from_shape
from shapely.geometry import Point as ShapelyPoint

router = APIRouter()

@router.post("/", response_model=PointResponse)
async def create_point(point: PointCreate, db: AsyncSession = Depends(get_db)):
    geometry = from_shape(ShapelyPoint(point.coordinates), srid=4326)
    db_point = Point(name=point.name, location=geometry)
    db.add(db_point)
    await db.commit()
    await db.refresh(db_point)
    return db_point

@router.get("/", response_model=list[PointResponse])
async def get_points(db: AsyncSession = Depends(get_db)):
    result = await db.execute("SELECT * FROM points")
    return [PointResponse(id=row.id, name=row.name, coordinates=row.location.coords[0]) for row in result]

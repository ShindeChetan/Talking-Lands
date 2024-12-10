from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.schemas.polygons import PolygonCreate, PolygonResponse
from app.crud.polygons import create_polygon, get_all_polygons

router = APIRouter()

@router.post("/", response_model=PolygonResponse)
async def add_polygon(data: PolygonCreate, db: AsyncSession = Depends(get_db)):
    try:
        polygon = await create_polygon(db, name=data.name, coordinates=data.coordinates)
        return polygon
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[PolygonResponse])
async def list_polygons(db: AsyncSession = Depends(get_db)):
    polygons = await get_all_polygons(db)
    return polygons

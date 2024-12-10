from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Polygon
from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon as ShapelyPolygon

async def create_polygon(db: AsyncSession, name: str, coordinates: list):
    geometry = from_shape(ShapelyPolygon(coordinates), srid=4326)
    db_polygon = Polygon(name=name, area=geometry)
    db.add(db_polygon)
    await db.commit()
    await db.refresh(db_polygon)
    return db_polygon

async def get_all_polygons(db: AsyncSession):
    result = await db.execute(select(Polygon))
    return result.scalars().all()

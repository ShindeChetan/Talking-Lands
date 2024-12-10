from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import Point
from geoalchemy2.shape import from_shape
from shapely.geometry import Point as ShapelyPoint

async def create_point(db: AsyncSession, name: str, coordinates: list):
    geometry = from_shape(ShapelyPoint(coordinates), srid=4326)
    db_point = Point(name=name, location=geometry)
    db.add(db_point)
    await db.commit()
    await db.refresh(db_point)
    return db_point

async def get_all_points(db: AsyncSession):
    result = await db.execute(select(Point))
    return result.scalars().all()

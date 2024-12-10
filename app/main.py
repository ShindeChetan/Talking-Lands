from fastapi import FastAPI
from app.routes import points, polygons
from app.database import init_db

app = FastAPI(title="Spatial Data API", version="1.0.0")

# Include routes
app.include_router(points.router, prefix="/points", tags=["Points"])
app.include_router(polygons.router, prefix="/polygons", tags=["Polygons"])

@app.on_event("startup")
async def startup():
    await init_db()

@app.get("/")
def root():
    return {"message": "Spatial Data API is running"}

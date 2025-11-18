# app/main.py
from fastapi import FastAPI, Depends
from app.config import settings
from app.db import engine, Base

app = FastAPI(title="BragBoard Auth (dev)")

@app.on_event("startup")
async def startup():
    # Create DB tables for dev (use Alembic for real migrations)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.get("/health")
async def health():
    return {"status": "ok"}

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from app.api.routes import router as api_router
from app.config import settings
from app.services.logger import app_logger as logger

app = FastAPI(title=settings.PROJECT_NAME)

@app.on_event("startup")
async def startup_event():
    logger.info("Application starting up...")

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Application shutting down...")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "AI Script Analyzer is running"}

# # Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(api_router, prefix="/api")

# Mount static files
app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/")
async def root():
    return FileResponse("frontend/index.html")

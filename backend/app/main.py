from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from app.routes import auth
from app.config import settings
import os

app = FastAPI(title=settings.PROJECT_NAME)

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (React build)
static_path = os.path.join(os.path.dirname(__file__), "static")
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Health check or root route
@app.get("/")
def read_root():
    return {"message": f"{settings.PROJECT_NAME} API running."}

# React frontend fallback (serves index.html for client-side routing)
@app.get("/{full_path:path}")
async def serve_react_app(full_path: str):
    index_file_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_file_path):
        return FileResponse(index_file_path)
    return {"error": "Frontend not built or index.html missing"}

# Register routes
app.include_router(auth.router)

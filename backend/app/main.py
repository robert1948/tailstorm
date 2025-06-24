import os
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

app = FastAPI(title=settings.project_name)

# Allow CORS (adjust as needed)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Built frontend path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FRONTEND_DIR = os.path.abspath(os.path.join(BASE_DIR, "../../../client/dist"))

if not os.path.exists(FRONTEND_DIR):
    raise RuntimeError(f"Missing frontend build directory: {FRONTEND_DIR}")

# Mount static files
app.mount("/assets", StaticFiles(directory=os.path.join(FRONTEND_DIR, "assets")), name="assets")

# Root route
@app.get("/")
def serve_index():
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

# Catch-all for SPA routes
@app.get("/{path:path}")
def catch_all(path: str):
    full_path = os.path.join(FRONTEND_DIR, path)
    if os.path.exists(full_path) and os.path.isfile(full_path):
        return FileResponse(full_path)
    return FileResponse(os.path.join(FRONTEND_DIR, "index.html"))

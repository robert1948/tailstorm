from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from app.config import settings  # Make sure this is correctly pointing to your Settings
import os

app = FastAPI(title=settings.project_name)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Path to frontend build
frontend_dist_path = os.path.join(os.path.dirname(__file__), "../../client/dist")

# Mount static files (e.g., /assets/index.js)
app.mount("/assets", StaticFiles(directory=os.path.join(frontend_dist_path, "assets")), name="assets")

# Serve index.html at root
@app.get("/")
def serve_frontend():
    return FileResponse(os.path.join(frontend_dist_path, "index.html"))

# Catch-all to support client-side routing (e.g. /dashboard)
@app.get("/{full_path:path}")
def serve_spa(full_path: str):
    file_path = os.path.join(frontend_dist_path, full_path)
    if os.path.isfile(file_path):
        return FileResponse(file_path)
    return FileResponse(os.path.join(frontend_dist_path, "index.html"))

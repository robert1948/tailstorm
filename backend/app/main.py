from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.routes import auth
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (React build output)
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Path to index.html (used in both root and fallback)
index_html = os.path.join(static_path, "index.html")

# Health check or serve React root
@app.get("/", include_in_schema=False)
def serve_landing():
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"message": f"{settings.PROJECT_NAME} API running."}

# API routes
app.include_router(auth.router, prefix="/auth")

# Catch-all fallback to React SPA
@app.get("/{full_path:path}", include_in_schema=False)
async def spa_fallback(full_path: str):
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"error": "Frontend not built or index.html missing"}

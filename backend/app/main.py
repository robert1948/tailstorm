from fastapi import FastAPI, Request
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

# Static directory
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
index_html = os.path.join(static_path, "index.html")

# Mount static files (for /static/assets/...)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Health check or root index.html
@app.get("/", include_in_schema=False)
def serve_root():
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"message": f"{settings.PROJECT_NAME} API running."}

# API endpoints
app.include_router(auth.router, prefix="/auth")

# Catch-all for React SPA (only non-static, non-file paths)
@app.get("/{full_path:path}", include_in_schema=False)
async def spa_fallback(full_path: str, request: Request):
    if full_path.startswith("static/") or "." in full_path:
        return {"error": f"Path not found: /{full_path}"}
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"error": "Frontend not built or index.html missing"}

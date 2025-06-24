import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from dotenv import load_dotenv
from app.routes import auth
from app.config import settings

# Load environment variables from .env
load_dotenv()

app = FastAPI(title=settings.project_name)


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define path to React build (typically /client/dist)
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
index_html = os.path.join(static_path, "index.html")

# Mount static assets (like JS, CSS, images)
app.mount("/static", StaticFiles(directory=static_path), name="static")

# API endpoints
app.include_router(auth.router, prefix="/auth")

# Serve index.html at root
@app.get("/", include_in_schema=False)
def serve_landing():
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"message": f"{settings.PROJECT_NAME} frontend not built."}

# Catch-all fallback for SPA routes (non-API, non-static, non-assets)
@app.get("/{full_path:path}", include_in_schema=False)
async def spa_fallback(full_path: str):
    if full_path.startswith("static/") or "." in full_path:
        return {"error": f"File not found: /{full_path}"}
    if os.path.exists(index_html):
        return FileResponse(index_html)
    return {"error": "Frontend not built or index.html missing"}

# ✅ DEV-ONLY utility route
if os.getenv("ENV", "development") == "development":
    @app.get("/check-secret", include_in_schema=False)
    def check_secret():
        return {
            "SECRET_KEY": os.getenv("SECRET_KEY", "Not Found"),
            "ENV": os.getenv("ENV", "development")
        }

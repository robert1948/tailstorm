from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.routes import auth
from app.config import settings

app = FastAPI(title=settings.PROJECT_NAME)

# CORS middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files from the built React app
static_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
app.mount("/static", StaticFiles(directory=static_path), name="static")

# Health check endpoint
@app.get("/", include_in_schema=False)
def health_check():
    # Attempt to serve index.html as landing
    index_file_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_file_path):
        return FileResponse(index_file_path)
    return {"message": f"{settings.PROJECT_NAME} API running."}

# Register backend routes
app.include_router(auth.router, prefix="/auth")

# Fallback for React SPA routing
@app.get("/{full_path:path}", include_in_schema=False)
async def serve_react_app(full_path: str):
    index_file_path = os.path.join(static_path, "index.html")
    if os.path.exists(index_file_path):
        return FileResponse(index_file_path)
    return {"error": "Frontend not built or index.html missing"}
# Fixed 06.36
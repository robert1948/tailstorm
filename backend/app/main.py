from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
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

@app.get("/")
def read_root():
    """
    Health check endpoint for the API.
    """
    return {"message": f"{settings.PROJECT_NAME} API running."}

# Register routes
app.include_router(auth.router)

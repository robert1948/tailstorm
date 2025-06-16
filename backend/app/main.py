from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import auth  # Updated import to match new structure

app = FastAPI()

# CORS configuration for local frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Use environment/config for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    """
    Health check endpoint for the API.
    """
    return {"message": "CapeControl API running."}

# Include authentication routes
app.include_router(auth.router)

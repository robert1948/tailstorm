from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Get the database URL from environment variables for security
DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://postgres:stinkie@localhost:5432/capecontrol')

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base class for declarative models
Base = declarative_base()

def get_db():
    """
    Dependency that provides a database session.
    Closes the session after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
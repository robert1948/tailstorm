from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    """
    Schema for creating a new user.
    """
    email: EmailStr  # User's email address
    password: str    # User's plain password

    class Config:
        from_attributes: bool = True  # Enable ORM mode for Pydantic v2

class UserOut(BaseModel):
    """
    Schema for returning user information (excluding sensitive data).
    """
    id: int          # User's unique ID
    email: EmailStr  # User's email address

    class Config:
        from_attributes: bool = True  # Enable ORM mode for Pydantic v2
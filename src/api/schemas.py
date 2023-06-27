from pydantic import Field, EmailStr

from src.types import BaseModel


class ContactForm(BaseModel):
    name: str = Field(..., max_length=64)
    email: EmailStr = Field(...)
    message: str = Field(...)

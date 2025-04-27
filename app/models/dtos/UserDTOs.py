from pydantic import BaseModel, Field
from typing import List, Optional
from app.models.Alert import Alert

class UserCreateDTO(BaseModel):
    user_id: int = Field(..., example=1)
    username: str = Field(..., example="santi")
    email: str = Field(..., example="santi@example.com")
    alerts: Optional[List[Alert]] = Field(default=[], example=[])

class UserResponseDTO(BaseModel):
    user_id: int
    username: str
    email: str
    alerts: Optional[List[Alert]] = []

    class Config:
        orm_mode = True

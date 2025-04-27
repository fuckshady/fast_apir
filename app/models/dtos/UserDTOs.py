from pydantic import BaseModel
from typing import List, Optional
from app.models.Alert import Alert

# DTO create user (input)
class UserCreateDTO(BaseModel):
    user_id: int
    username: str
    email: str
    alerts: Optional[List[Alert]] = []

# DTO show user (output)
class UserResponseDTO(BaseModel):
    user_id: int
    username: str
    email: str
    alerts: Optional[List[Alert]] = []

    class Config:
        orm_mode = True

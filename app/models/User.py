from pydantic import BaseModel
from typing import List, Optional
from app.models.Alert import Alert

#update
class User(BaseModel):
    user_id: int
    username: str
    email: str
    alerts: Optional[List[Alert]] = []
from pydantic import BaseModel

#update
class Alert(BaseModel):
    alert_id: int
    title: str
    description: str
    user_id: int
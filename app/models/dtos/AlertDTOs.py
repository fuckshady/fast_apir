from pydantic import BaseModel

# DTO create alert (input)
class AlertCreateDTO(BaseModel):
    alert_id: int
    title: str
    description: str
    user_id: int

# DTO show alert (output)
class AlertResponseDTO(BaseModel):
    alert_id: int
    title: str
    description: str
    user_id: int

    class Config:
        orm_mode = True

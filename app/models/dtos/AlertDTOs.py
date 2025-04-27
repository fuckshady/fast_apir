from pydantic import BaseModel, Field

class AlertCreateDTO(BaseModel):
    alert_id: int = Field(..., example=101)
    title: str = Field(..., example="Fire detected")
    description: str = Field(..., example="Smoke was detected in building B")
    user_id: int = Field(..., example=1)

class AlertResponseDTO(BaseModel):
    alert_id: int
    title: str
    description: str
    user_id: int

    class Config:
        orm_mode = True

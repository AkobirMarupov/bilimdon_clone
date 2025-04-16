from pydantic import BaseModel
from datetime import datetime


class PartipicationResponse(BaseModel):
    id: int
    user_id: int
    game_id: int
    start_time: datetime
    end_time: datetime
    gained_score: int
    registered_at: datetime

    class Config:
        arm_mode = True

class PartipicationCreate(BaseModel):
    user_id: int
    game_id: int
    start_time: datetime
    end_time: datetime
    gained_score: int
    registered_at: datetime

class PartipicationUpdate(BaseModel):
    user_id: int
    game_id: int
    start_time: datetime
    end_time: datetime
    gained_score: int
    registered_at: datetime
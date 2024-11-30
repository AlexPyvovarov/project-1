from sqlmodel import SQLModel, Field
from typing import Optional
from config import restart_db, session

class Tur(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    price: float
    description: str
    image_url: str = Field(default="https://picsum.photos/200/300?grayscale")
    is_booked: bool = False




#EOF
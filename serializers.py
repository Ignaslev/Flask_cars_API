from pydantic import BaseModel
import datetime

class ProjektasSchema(BaseModel):
    id : int
    brand : str
    model : str
    year : int
    price : float
    date : datetime.datetime
    image : str | None

    class Config:
        from_attributes = True
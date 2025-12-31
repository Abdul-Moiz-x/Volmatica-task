from pydantic import BaseModel


class Patient(BaseModel):
    name:str
    height:float
    weight:int



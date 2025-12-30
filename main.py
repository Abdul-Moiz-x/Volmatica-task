from fastapi import FastAPI,HTTPException
from data.data import patients_data

app = FastAPI()

@app.get("/patient/{id}")
def get_patients(id:int):
    
    if id <= 0:
        return patients_data
    
    if id in patients_data:
        return patients_data[id]
    else:
        raise HTTPException(404,"Not Found")
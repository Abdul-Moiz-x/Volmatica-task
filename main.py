from fastapi import FastAPI,HTTPException,Query,Depends
from fastapi.responses import JSONResponse
from data.data import patients_data
from schemas.models import Patient
from repository.patient_repo import PatientRepo,get_patient_repo

app = FastAPI()


@app.get("/patients")
def get_patients_list(name:str = Query(None), repo:PatientRepo = Depends(get_patient_repo)):
    if name:
        result = repo.get_patient_by_name(name)
        if result:
            return result
        else:
            raise HTTPException(404, "Patient does not exist")
    
    return JSONResponse(patients_data)


@app.get("/patient/{id}")
def get_patient(id:int):
    
    if id in patients_data:
        return patients_data[id]
    else:
        raise HTTPException(404,"Not Found")


@app.post("/patient/{id}")
def add_patient(id:int, patient:Patient, repo:PatientRepo = Depends(get_patient_repo)):
    try:
        repo.add_patient(id,patient)
        return JSONResponse("Created", 201)
    except:
        raise HTTPException(400,"ID already exists")


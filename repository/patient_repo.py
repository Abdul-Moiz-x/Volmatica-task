from data.data import patients_data
from schemas.models import Patient

class PatientRepo:
    def __init__(self,patients:dict):
        self.patients = patients
    
    def add_patient(self, patient_id:int, patient:Patient):
        if patient_id in self.patients.keys():
            raise KeyError("ID exists")
        
        self.patients[patient_id] = patient.model_dump()



    def get_patient_by_name(self, patient_name:str):
        for dic in patients_data.values():
            if patient_name == dic.get("name"):
                return dic
        return 0
    

def get_patient_repo():
    return PatientRepo(patients_data)
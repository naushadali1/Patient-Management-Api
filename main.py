from fastapi import FastAPI, HTTPException, Path, Query
import  json

# Load data from JSON file
def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

# create FastAPI instance
app= FastAPI()

# Home Page api
@app.get("/")
async def root():
    return {"message": "Patient Management System Api"}

# About the API
@app.get("/about")
async def about():
    return {
        "message": "management system for patients for a hospital"
    }

# API for getting all patients
@app.get("/view")
async def get_patients():
    data = load_data()
    return  data

# API for getting a specific patient by ID
@app.get("/view/{patient_id}")
async def get_patient(patient_id: str = Path(..., description="The ID of the patient to get", example= "p0001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    else:
        raise HTTPException(status_code=404, detail="Patient not found")

#  sort by height , wight and bmi
@app.get("/sort")
async def sort_patients(sort_by: str = Query(..., description="Sort patients by height, weight, or bmi", example="height"), order: str = Query("asc", description="Order of sorting: asc or desc")):
    data = load_data()
    sorted_fields = ["height", "weight", "bmi"]
    if sort_by not in sorted_fields:
        raise HTTPException(status_code=400, detail=f"Invalid sort parameter '{sort_by}'. Must be one of {sorted_fields}.")
    
    if order not in ["asc", "desc"]:
        raise HTTPException(status_code=400, detail="Invalid order parameter. Must be 'asc' or 'desc'.")
    
    sorted_order = True if order == "desc" else False
    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by, 0), reverse=sorted_order)
    return sorted_data



from fastapi import FastAPI
app= FastAPI()

@app.get("/")
async def root():
    return {"message": "Patient Management System Api"}

# About the API
@app.get("/about")
async def about():
    return {
        "message": "management system for patients for a hospital"
    }


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Predictive Healthcare API is running!"}

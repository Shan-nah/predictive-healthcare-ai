from fastapi import FastAPI
from api.routes import predict

app = FastAPI()

app.include_router(predict.router)

@app.get("/")
def read_root():
    return {"message": "Predictive Healthcare AI API is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api.main:app", host="127.0.0.1", port=800)

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.services.service import predict_risk  # Ensure this function accepts 'patient_data'

router = APIRouter()

class InputData(BaseModel):
    features: list

@router.post("/predict")
async def predict(data: InputData):
    try:
        risk_score = predict_risk(data.features)  # ✅ Pass 'data.features' correctly
        return {"risk_score": risk_score}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

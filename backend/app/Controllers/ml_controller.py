from fastapi import APIRouter

from app.schemas import DiabetesInput, HeartInput
from app.Services.ml_service import MLService

router = APIRouter(prefix="/api/predict", tags=["ML Predictions"])
ml_service = MLService()


@router.post("/diabetes")
def predict_diabetes(payload: DiabetesInput):
    return ml_service.diabetes(payload.model_dump())


@router.post("/heart")
def predict_heart(payload: HeartInput):
    return ml_service.heart(payload.model_dump())

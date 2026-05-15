from fastapi import FastAPI, HTTPException
from core.schemas import FishFeedInput, PredictionOutput
from ml.inference import FishFeedPredictor
from src.utils import setup_logging, get_logger
import uvicorn
import os

# Initialize components
setup_logging()
logger = get_logger('api')

app = FastAPI(title="Fish Feed Prediction API")

# Global predictor instance
predictor = None

@app.on_event("startup")
def load_models():
    global predictor
    try:
        predictor = FishFeedPredictor()
        logger.info("Models loaded successfully at startup.")
    except Exception as e:
        logger.error(f"Failed to load models: {e}")

@app.get("/")
def read_root():
    return {"message": "Fish Feed Prediction API is running"}

@app.post("/predict", response_model=PredictionOutput)
def predict(input_data: FishFeedInput):
    if predictor is None:
        raise HTTPException(status_code=503, detail="Model not loaded")
    
    try:
        result = predictor.predict(input_data.dict())
        return result
    except Exception as e:
        logger.error(f"Prediction failed: {e}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

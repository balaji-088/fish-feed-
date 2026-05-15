from pydantic import BaseModel, Field
from typing import Optional

class FishFeedInput(BaseModel):
    ph: float = Field(..., ge=0, le=14, description="pH level of the water")
    temperature: float = Field(..., ge=0, le=50, description="Temperature in Celsius")
    turbidity: float = Field(..., ge=0, description="Turbidity level")
    fish: str = Field(..., description="Fish species")
    Fish_Weight: float = Field(..., ge=0, description="Weight of the fish")

class PredictionOutput(BaseModel):
    feed_ratio: float
    feed_quantity: float

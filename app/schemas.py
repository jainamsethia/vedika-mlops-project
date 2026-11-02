from pydantic import BaseModel, Field


class HouseFeatures(BaseModel):
    area: float = Field(gt=0, le=100_000, description="Living area in square feet")
    bedrooms: int = Field(ge=1, le=20)
    bathrooms: float = Field(ge=1, le=20)
    age: float = Field(ge=0, le=200, description="Property age in years")
    distance_to_city: float = Field(ge=0, le=500, description="Distance in kilometers")


class PredictionResponse(BaseModel):
    predicted_price: float
    currency: str = "USD"

import time

from fastapi import FastAPI, Request
from prometheus_client import Counter, Histogram, make_asgi_app

from app.model import predict
from app.schemas import HouseFeatures, PredictionResponse

app = FastAPI(title="House Price Prediction API", version="1.0.0")
REQUEST_COUNT = Counter("prediction_api_requests_total", "Total API requests", ["method", "path", "status"])
REQUEST_LATENCY = Histogram("prediction_api_request_latency_seconds", "API request latency", ["path"])
app.mount("/metrics", make_asgi_app())


@app.middleware("http")
async def metrics_middleware(request: Request, call_next):
    start = time.perf_counter()
    response = await call_next(request)
    REQUEST_COUNT.labels(request.method, request.url.path, response.status_code).inc()
    REQUEST_LATENCY.labels(request.url.path).observe(time.perf_counter() - start)
    return response


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict_price(features: HouseFeatures) -> PredictionResponse:
    return PredictionResponse(predicted_price=round(predict(features.model_dump()), 2))

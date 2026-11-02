FROM python:3.12-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY app ./app
COPY streamlit_app ./streamlit_app
RUN python -m app.train && cp models/house_price_model.joblib streamlit_app/house_price_model.joblib
EXPOSE 8501
CMD ["streamlit", "run", "streamlit_app/app.py", "--server.address=0.0.0.0", "--server.port=8501"]

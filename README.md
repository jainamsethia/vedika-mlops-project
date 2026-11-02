# House Price Prediction MLOps Project

An end-to-end house price prediction system with:

- FastAPI prediction API and Prometheus metrics
- Streamlit user interface
- Scikit-learn model training
- Docker image
- GitHub Actions CI and container publishing
- Kubernetes deployment with HPA
- Terraform infrastructure for AWS EKS
- Prometheus and Grafana monitoring

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m app.train
uvicorn app.main:app --reload
```

In another terminal:

```bash
streamlit run streamlit_app/app.py
```

Open `http://localhost:8501`. The API is available at `http://localhost:8000/docs`.

## Docker

```bash
docker build -t house-predictor:local .
docker run --rm -p 8000:8000 house-predictor:local
```

## Kubernetes

Build and publish the image, then replace `ghcr.io/your-org/house-predictor:latest`
in `k8s/api-deployment.yaml`:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/api-deployment.yaml
kubectl apply -f k8s/streamlit-deployment.yaml
kubectl apply -f k8s/monitoring.yaml
```

The manifests use a `LoadBalancer` service for Streamlit and an internal API
service. For local clusters, use `minikube tunnel` or `kubectl port-forward`.

## AWS infrastructure

The Terraform module provisions an EKS cluster and node group. Configure AWS
credentials and run:

```bash
cd terraform
terraform init
terraform plan -var='cluster_name=house-predictor'
terraform apply -var='cluster_name=house-predictor'
```

## CI/CD

`.github/workflows/ci-cd.yml` runs tests and builds the image on every pull
request. On pushes to `main`, it publishes the image to GitHub Container
Registry and updates the Kubernetes deployment. Set repository permissions to
allow `packages: write` and configure a cluster context secret named
`KUBE_CONFIG` for deployment.

## Model

The included training script creates a deterministic demonstration dataset
using common housing features. Replace `app/train.py` with your production
dataset pipeline when real data is available. The API validates inputs with
Pydantic and exposes `/health`, `/predict`, and `/metrics`.

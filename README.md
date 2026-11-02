# House Price Prediction MLOps Project

An end-to-end, self-contained Streamlit house price prediction system with:

- Streamlit user interface
- Scikit-learn model training
- Docker image
- GitHub Actions CI and container publishing
- Kubernetes deployment
- Terraform infrastructure for AWS EKS

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run streamlit_app/app.py
```

Open `http://localhost:8501`. The model trains or loads inside the Streamlit
process; no separate backend or API URL is required.

## Deploy the Streamlit app

1. Push this repository to GitHub.
2. On [share.streamlit.io](https://share.streamlit.io), choose **New app**,
   select this repository and branch, and set the main file to
   `streamlit_app/app.py`.
3. Click **Deploy**. The model is trained/loaded inside the Streamlit app.

## Docker

```bash
docker build -t house-predictor:local .
docker run --rm -p 8501:8501 house-predictor:local
```

## Kubernetes

Build and publish the image, then replace
`ghcr.io/your-org/house-predictor:latest` in
`k8s/streamlit-deployment.yaml`:

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/streamlit-deployment.yaml
```

The Streamlit manifest uses a `LoadBalancer` service. For local clusters, use
`minikube tunnel` or `kubectl port-forward`.

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

`.github/workflows/ci-cd.yml` checks Python syntax and builds the image on every
pull request. On pushes to `main`, it publishes the image to GitHub Container
Registry and updates the Streamlit Kubernetes deployment. Set repository
permissions to allow `packages: write` and configure a cluster context secret
named `KUBE_CONFIG` for deployment.

## Model

The included Streamlit model helper creates a deterministic demonstration
dataset using common housing features. Replace the training logic in
`streamlit_app/model.py` with your production dataset pipeline when real data
is available.


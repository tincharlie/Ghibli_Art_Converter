# README.md
# Ghibli Art Converter

This project converts images into Studio Ghibli-style art using AnimeGANv2.

## Setup
```
docker build -t ghibli-art-converter .
docker run -v $(pwd)/models:/app/models ghibli-art-converter
```

## Kubernetes Deployment
```
kubectl apply -f k8s-deployment.yaml
```

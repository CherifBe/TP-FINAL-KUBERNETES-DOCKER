# Multi-Container Web Application Deployment

This project demonstrates a multi-container web application deployment using Docker Compose for local development and Kubernetes for production-like orchestration.

## Prerequisites

- Docker Desktop
- Minikube
- kubectl
- PowerShell

## Project Structure

```
.
├── frontend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── backend/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yaml
├── backend-deployment.yaml
├── frontend-deployment.yaml
├── services.yaml
├── pv.yaml
└── hpa.yaml
```

## Docker Compose Deployment

1. Start Docker containers:
```powershell
docker-compose up -d
```

2. Verify containers:
```powershell
docker-compose ps
```

## Kubernetes Deployment

1. Start Minikube:
```powershell
minikube start
```

2. Enable metrics server:
```powershell
minikube addons enable metrics-server
```

3. Connect to Minikube's Docker daemon:
```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

4. Build the images:
```powershell
docker-compose build
```

5. Apply Kubernetes manifests:
```powershell
kubectl apply -f pv.yaml
kubectl apply -f backend-deployment.yaml
kubectl apply -f frontend-deployment.yaml
kubectl apply -f services.yaml
kubectl apply -f hpa.yaml
```

## Testing

1. Start the service tunnel:
```powershell
minikube service frontend
```

2. In a new terminal, test endpoints:
```powershell
# Status check
curl http://127.0.0.1:<PORT>/status

# Load test
for ($i=0; $i -lt 100; $i++) {
    Invoke-WebRequest -Uri "http://127.0.0.1:<PORT>/compute" -UseBasicParsing
}
```

3. Monitor scaling:
```powershell
kubectl get hpa -w
```

## Cleanup

```powershell
# Delete Kubernetes resources
kubectl delete -f .

# Stop Minikube
minikube stop

# Stop Docker Compose
docker-compose down
```

## API Endpoints

- `/write/{data}`: Writes data to the backend
- `/read`: Reads all data from the backend
- `/compute`: Simulates heavy computation
- `/status`: Returns backend health status
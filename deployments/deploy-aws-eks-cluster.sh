#!/bin/bash

# Variables
KUBECONFIG="/root/.kube/config"
NAMESPACE="cloudapp-django-web"
DOCKER_IMAGE="joelwembo/cloudapp-django-web:latest"
DEPLOYMENT_NAME="cloudapp-django-web"
SERVICE_NAME="mycluster"
PORT=80

# Set KUBECONFIG environment variable
export KUBECONFIG="$KUBECONFIG"

# Apply Kubernetes manifests
kubectl apply -f k8s/deployment.yaml

# Update the Docker image in the deployment
kubectl set image deployment/$DEPLOYMENT_NAME $DEPLOYMENT_NAME=$DOCKER_IMAGE -n $NAMESPACE

# Expose the deployment as a service
kubectl expose deployment $DEPLOYMENT_NAME --type=LoadBalancer --port=$PORT --target-port=$PORT -n $NAMESPACE --name=$SERVICE_NAME

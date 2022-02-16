#!usr/bin/python3
from subprocess import call
import os

os.system('sudo apt-get remove docker docker-engine docker.io containerd runc')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y ca-certificates curl gnupg lsb-release')
os.system('curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg')
os.system('echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null')
os.system('sudo apt-get update')
os.system('sudo apt-get install -y docker-ce docker-ce-cli containerd.io')

os.system('sudo gcloud config set project bloque4-338917')
os.system('sudo gcloud services enable container.googleapis.com')
os.system('sudo snap install kubectl --classic')

# Creamos los pods a partir de los archivos de configuracion yaml
os.system('sudo gcloud container clusters create cluster4 --num-nodes=5 --zone=us-central1-a')

os.system('sudo kubectl apply -f productpage.yaml')
os.system('sudo kubectl apply -f details-service.yaml')
os.system('sudo kubectl apply -f details-deployment.yaml')
os.system('sudo kubectl apply -f ratings-service.yaml')
os.system('sudo kubectl apply -f ratings-deployment.yaml')
os.system('sudo kubectl apply -f reviews-service.yaml')

# Descomentar la versión deseada
#os.system('sudo kubectl apply -f reviews-v1-deployment.yaml')
#os.system('sudo kubectl apply -f reviews-v2-deployment.yaml')
os.system('sudo kubectl apply -f reviews-v3-deployment.yaml')

# Exponer servicio
os.system('sudo kubectl expose deployment productpage --type=LoadBalancer --port=9080')

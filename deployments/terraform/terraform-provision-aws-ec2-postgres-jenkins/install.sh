#!/bin/bash

# Jenkins installations
sudo apt-get install debian-keyring debian-archive-keyring --assume-yes
sudo apt-key update
sudo apt-get update
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 40976EAF437D05B5
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 5BA31D57EF5975CA
sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 3B4FE6ACC0B21F32
sudo apt update
sudo apt install openjdk-11-jre-headless --assume-yes
sudo java -version
curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins --assume-yes
# sudo service jenkins status
echo 'Jenkins successfully installer'

# Postgres Installation
# sudo apt update
# enable repository to install postgresql
sudo apt install postgresql postgresql-contrib --assume-yes
# Install PostgreSQL server and initialize the database 
# cluster for this server
# Start the db service
systemctl enable postgresql
systemctl start postgresql
echo 'Postgresql Installed successfully installer'


# Docker installation
sudo apt install apt-transport-https ca-certificates curl software-properties-common --assume-yes
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'
apt-cache policy docker-ce
sudo apt install docker-ce --assume-yes
sudo chmod 777 /var/run/docker.sock
sudo usermod -a -G docker jenkins
sudo usermod -a -G docker argocd
sudo usermod -a -G docker kubectl

# sudo systemctl status docker
echo 'Docker successfully installer'

# install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
echo "Docker Compose Installed successfully installer"

# install git
sudo yum install git -y
echo "Git Installed successfully installer"
# install terraform
sudo yum install -y yum-utils
sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
sudo yum -y install terraform
echo "Terraform Installed successfully installer"
# install kubectl

# Kubectl installations
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo tee /usr/share/keyrings/kubernetes.gpg
echo "deb [arch=amd64 signed-by=/usr/share/keyrings/kubernetes.gpg] http://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee -a /etc/apt/sources.list
sudo apt install kubeadm kubelet kubectl -y
sudo apt-mark hold kubeadm kubelet kubectl -y
echo "Kubeclt Installed successfully installer"

# install minikube
sudo apt install -y curl wget apt-transport-https
wget https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo cp minikube-linux-amd64 /usr/local/bin/minikube
sudo chmod +x /usr/local/bin/minikube
minikube version
echo "Minikube Installed successfully installer"



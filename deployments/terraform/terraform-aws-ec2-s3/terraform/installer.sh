#!/bin/bash

# Java Installations
sudo apt-get install openjdk-11-jdk -y
sudo apt-get install zip -y
echo 'JDK Installed successfully installer'
# Postgres Installation
# sudo apt update
# enable repository to install postgresql
sudo apt install postgresql postgresql-contrib --assume-yes
# Install PostgreSQ L server and initialize the database 
# cluster for this server
# Start the db service
systemctl stop postgresql
systemctl enable postgresql
# systemctl start postgresql
echo 'Postgresql Installed successfully installer'

# Docker installation
sudo apt install apt-transport-https ca-certificates curl software-properties-common --assume-yes
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable'
apt-cache policy docker-ce
sudo apt install docker-ce --assume-yes
sudo chmod 777 /var/run/docker.sock

# sudo systemctl status docker
echo 'Docker successfully installer'

# install docker compose
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose 
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version
echo "Docker Compose Installed successfully installer"








sudo wget https://binaries.sonarsource.com/Distribution/sonarqube/sonarqube-9.8.0.63668.zip
sudo unzip sonarqube-9.8.0.63668.zip
sudo mv sonarqube-9.8.0.63668 /opt/sonarqube
sudo groupadd sonar
sudo useradd -d /opt/sonarqube -g sonar sonar
sudo chown sonar:sonar /opt/sonarqube -R



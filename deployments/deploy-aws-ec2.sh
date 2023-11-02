#!/bin/sh
whoami
echo 'deployed to production server'
# ssh root@YOUR_SERVER_IP_ADDRESS <<EOF
#   cd /path/to/your/project
#   git pull
#   docker-compose -f docker-compose-production.yml up --build -d
#   exit
# EOF
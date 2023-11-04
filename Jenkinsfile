pipeline{
    agent any
     options {
        buildDiscarder(logRotator(numToKeepStr: '3'))
      }
      environment {
        DOCKERHUB_CREDENTIALS = credentials('globaldockerhub')
        appName = "server"
        registry = ""
        registryCredential = ""
        projectPath = ""
        AWS_ACCESS_KEY_ID = credentials('your_aws_access_key_id')
        AWS_SECRET_ACCESS_KEY = credentials('your_aws_secret_access_key')
        AWS_REGION = 'your_aws_region'
        EC2_INSTANCE = 'your_ec2_instance_id'
        SSH_KEY = credentials('your_ssh_key')
      }
    stages {

            stage('Checkout Code'){
            steps {
                sh 'python3 --version'
                    git url: 'https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes.git' 
                }
        
            }

            stage('Copy Application to EC2') {
            steps {
                sh "scp -i ${SSH_KEY} -o StrictHostKeyChecking=no -r * ec2-user@${EC2_INSTANCE}:/path/to/destination"
            }
        }
            stage('Build'){ 
            steps  {
                sh 'docker-compose down'
                sh 'docker build -t joelwembo/cloudapp-django-web:latest --no-cache .'
                }
            }
            stage('Login') {
                steps {
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                    
                }
            }

           stage('Docker Push') {
                steps {
                    sh 'docker images'
                    // sh 'docker images --filter "reference=cloudapp-django-web*"' 
                    sh 'docker push joelwembo/cloudapp-django-web:latest'
                }
            }
            stage('Run the Application'){
                steps {
                    sh 'docker-compose up -d'
                }
            }
            stage('Execute Manuel Tests'){
                steps {
                    sh 'echo "Migration Operation Completed , Please Check the logs status"'
                }
            }

          stage('k8s Deployment') {
          steps {
            sh 'kubectl config set-cluster minikube --server=https://192.168.49.2:8443 --insecure-skip-tls-verify=true'
            sh 'kubectl config set-context minikube --cluster=minikube --user=minikube'
            sh 'kubectl config use-context minikube'
            // sh 'kubectl cluster-info'
        //     dir('deployments/k8s') {
        //       sh 'kubectl delete namespace cloudapp-django-web'
        //       sh 'kubectl create namespace cloudapp-django-web'
        //       sh 'kubectl config set-context --current --namespace=cloudapp-django-web'
        //       sh 'kubectl apply -f deployment.yaml'
        //     }    
        //     sh 'kubectl get services && kubectl get pods'
        //     sh 'minikube service cloudapp-django-web -n  cloudapp-django-web &'
        //     sh 'exit 0'
        //    }
         } 
          } 

        //  stage('Deploy to AWS') {
        //     steps {
        //          dir('deployments') {
        //             sh "pwd"
        //             sh "chmod +x -R ./deploy-aws-ec2.sh"
        //             sh 'docker images --filter "reference=cloudapp-django-web*"' 
        //             sh './deploy-aws-ec2.sh'
        //          }
              
        //     }
        // }
        stage('SSH into EC2') {
            steps {
                script {
                    withAWS(region: AWS_REGION, credentials: 'aws-credentials') {
                        sshCommand remote: ec2_user@${EC2_INSTANCE}, command: '''
                            # Replace with your setup and deployment commands
                            cd /path/to/destination
                            source /path/to/venv/bin/activate
                            python manage.py migrate
                            python manage.py collectstatic --noinput
                            # Add any other Django deployment commands here
                        '''
                    }
                }
            }
        } 
    }

 }


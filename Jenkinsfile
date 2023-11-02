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
      }
    stages {

            stage('Environment'){
            steps {
                sh 'python3 --version'
                    git url: 'https://github.com/joelwembo/django-multitenant-saas-ecommerce-kubernetes.git' 
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
    }
}
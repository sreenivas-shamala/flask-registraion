pipeline {

    agent any

    environment {
        IMAGE_NAME = "sreenivasulusamala108/flask-registration"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Checkout') {
            steps {
 
                git branch: 'main', url:
                  'https://github.com/sreenivas-shamala/flask-registraion.git'

            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG .'
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_PASS'
                )]) {

                    sh '''
                    echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl apply -f flask-app.yaml
                
                '''
            }
        }

        stage('Verify Deployment') {
            steps {
                sh '''
                kubectl get pods
                kubectl get services
                '''
            }
        }
    }

    post {
        success {
            echo "Deployment Successful!"
        }

        failure {
            echo "Pipeline Failed!"
        }
    }
}

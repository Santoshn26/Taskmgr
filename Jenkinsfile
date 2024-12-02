pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Santoshn26/Taskmgr.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t taskmgr .'
            }
        }
        stage('Tag and Push Docker Image') {
            environment {
                DOCKER_REGISTRY = 'docker.io' // Docker Hub
                DOCKER_IMAGE = 'santoshn26/taskmgr:latest'
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                    echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin $DOCKER_REGISTRY
                    docker tag taskmgr $DOCKER_IMAGE
                    docker push $DOCKER_IMAGE
                    '''
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                sh '''
                docker stop taskmgr || true
                docker rm taskmgr || true
                docker run -d --name taskmgr -p 5000:5000 taskmgr
                '''
            }
        }
    }
}

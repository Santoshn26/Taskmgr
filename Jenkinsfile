pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'santoshnc26/taskmgr:latest'
        DOCKER_REGISTRY = 'docker.io'
    }
    stages {
        stage('Cleanup Existing Containers') {
            steps {
                script {
                    sh '''
                    # Stop and remove existing containers if they exist
                    docker ps -aq --filter "name=flask-app" | xargs -r docker rm -f
                    docker ps -aq --filter "name=mysql-db" | xargs -r docker rm -f
                    '''
             }
        }
        stage('Clone Repository') {
            steps {
                git branch: 'Taskmgr_v2', url: 'https://github.com/Santoshn26/Taskmgr.git'
            }
        }
        stage('Build Docker Images with Docker Compose') {
            steps {
                script {
                    // Build the Docker images using docker-compose
                    sh 'docker-compose build'
                }
            }
        }
        stage('Push Docker Images to Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker-compose push
                        '''
                    }
                }
            }
        }
        stage('Run Docker Containers with Docker Compose') {
            steps {
                script {
                    // Use docker-compose to bring up the containers
                    sh 'docker-compose up -d'
                }
            }
        }
        stage('Clean Up Docker Containers') {
            steps {
                script {
                    // Clean up any unused containers after testing/deployment
                    //sh 'docker-compose down'
                    sh echo "not down"
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

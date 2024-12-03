pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'santoshnc26/taskmgr:latest'
        DOCKER_REGISTRY = 'docker.io'
    }
    stages {
        stage('Checkout SCM') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/Taskmgr_v2']],
                    doGenerateSubmoduleConfigurations: false,
                    extensions: [],
                    userRemoteConfigs: [[url: 'https://github.com/Santoshn26/Taskmgr.git']]
                ])
            }
        }

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
        }

        stage('Build Docker Images with Docker Compose') {
            steps {
                script {
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
                    sh 'docker-compose up -d'
                }
            }
        }

        stage('Clean Up Docker Containers') {
            steps {
                script {
                    // Uncomment below line to clean up after deployment
                    // sh 'docker-compose down'
                    echo "Cleanup Disabled"
                }
            }
        }
    }

    post {
        always {
            echo "Post-build cleanup disabled."
        }
    }
}

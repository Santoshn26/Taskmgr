pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'santoshnc26/taskmgr:latest'
        DOCKER_REGISTRY = 'docker.io'
        SONAR_PROJECT_KEY = 'TaskMgr'
        SONAR_HOST_URL = 'http://192.168.29.142:9000'
        SONAR_LOGIN = 'sqa_c32897d635f2e817fbf9bd67be5f8a42eefc86b3' // Replace with token
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
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                    sonar-scanner \
                        -Dsonar.projectKey=$SONAR_PROJECT_KEY \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=$SONAR_HOST_URL \
                        -Dsonar.login=$SONAR_LOGIN
                    '''
                }
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

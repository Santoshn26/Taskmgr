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
        stage('Push Docker Image to Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                    echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                    docker tag taskmgr santoshnc26/taskmgr:latest
                    docker push santoshnc26/taskmgr:latest
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


def getVersion(){
 commitid = sh returnStdout: true, script: '''git rev-parse HEAD'''
 return commitid
}
pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('3afb1223-a858-4b21-8c9b-0ea7b1a8cf77') // Replace with your Docker Hub credentials ID
        DOCKERHUB_REPO = '224574/todoapp' // Replace with your Docker Hub repository
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    env.commitId = getVersion()
                    env.imageName = "${env.DOCKERHUB_REPO}:${commitId}"
                    sh "docker build -t ${imageName} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh "echo ${DOCKERHUB_CREDENTIALS_PSW} | docker login -u ${DOCKERHUB_CREDENTIALS_USR} --password-stdin"
                    sh "docker push ${imageName}"
                }
            }
        }
    }

    post {
        always {
            sh 'docker logout'
        }
    }
}
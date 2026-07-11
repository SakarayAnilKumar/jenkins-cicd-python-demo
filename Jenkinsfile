pipeline {
    agent any
        // Replace the paths below with the exact paths returned by 'where python'
        withEnv([
            'PATH+PYTHON=C:\\Users\\sakar\\AppData\\Local\\Programs\\Python\\Python314',
            'PATH+PIP=C:\\Users\\sakar\\AppData\\Local\\Programs\\Python\\Python314\\Scripts'
        ])
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh 'pytest'
            }
        }
        stage('Build') {
            steps {
                echo 'Building application...'
                sh 'python app.py'
            }
        }
    }
}

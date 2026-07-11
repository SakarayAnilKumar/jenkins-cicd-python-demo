pipeline {
    agent any
    tools {
        // Specify the tool type and the exact label you gave it in the UI configuration
        python 'Python314' 
    }
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

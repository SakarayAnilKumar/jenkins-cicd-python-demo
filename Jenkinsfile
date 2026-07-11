pipeline {
    agent any
    
    environment {
        // 1. Swapped to Unix forward slashes (/) so 'sh' can read the folders
        // 2. Extended the path globally so every stage can see your files
        PATH = "C:/Users/sakar/AppData/Local/Programs/Python/Python314;C:/Users/sakar/AppData/Local/Programs/Python/Python314/Scripts;${env.PATH}"
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
                sh 'python -m pip install --upgrade pip'
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

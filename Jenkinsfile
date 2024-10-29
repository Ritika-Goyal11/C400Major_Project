pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/Ritika-Goyal11/C400Major_Project.git'
        SCRIPT_PATH = 'main.py'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: "${REPO_URL}"
            }
        }

        stage('Run Stress Test Script') {
            steps {
                sh "python3 ${SCRIPT_PATH}"
            }
        }
    }

    post {
        success {
            echo 'Script executed successfully!'
        }
        failure {
            echo 'Script execution failed!'
        }
    }
}

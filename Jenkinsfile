pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Ritika-Goyal11/C400Major_Project.git', branch: 'main' 
            }
        }
        stage('Run Stress Test Script') {
            steps {
                sh '''
                (
                    echo "1"  # Simulate pressing '1' for Memory Stress Testing
                    echo "6"  # Simulate pressing '6' to exit afterward
                ) | python3 main.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Stress test executed successfully!'
        }
        failure {
            echo 'Stress test execution failed.'
        }
    }
}

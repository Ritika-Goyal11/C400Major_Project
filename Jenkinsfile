pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Select Stress Test') {
            steps {
                script {
                    // Call main directly, which will handle user input
                    def response = sh(script: 'python3 main.py', returnStdout: true).trim()
                    echo "Response from script: ${response}"
                }
            }
        }

        stage('Run Stress Test Script') {
            steps {
                echo "Running the selected stress test..."
                // If you need to run a specific stress test, you can handle that in main.py as necessary
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}

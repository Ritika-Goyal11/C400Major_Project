pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Run Stress Test Script') {
            steps {
                // Directly feed input through a here-document
                script {
                    sh '''
                    echo -e "1\n" | python3 main.py
                    '''
                }
            }
        }
    }
    post {
        always {
            // Clean up any temporary files if necessary
            sh 'rm -f input.txt'
        }
    }
}

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
                script {
                    def choice = '1\n'
                    def input = "${choice}"
                    writeFile file: 'input.txt', text: input
                    sh "python3 main.py < input.txt"
                }
            }
        }
    }
    post {
        always {
            sh 'rm -f input.txt'
        }
    }
}

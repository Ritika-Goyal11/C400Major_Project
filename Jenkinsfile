pipeline {
    agent any

    parameters {
        choice(name: 'STRESS_TEST', choices: ['1', '2', '3', '4', '5', '6'], description: 'Select the type of stress test to run:\n1. Memory\n2. Disk\n3. Network\n4. CPU\n5. MySQL\n6. Exit')
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Run Stress Test Script') {
            steps {
                script {
                    // Pass the user choice as an argument to the script
                    sh "python3 main.py"
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}

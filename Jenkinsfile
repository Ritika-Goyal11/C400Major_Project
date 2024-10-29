pipeline {
    agent any
    parameters {
        choice(name: 'STRESS_TEST', choices: ['Memory', 'Disk', 'Network', 'CPU', 'MySQL'], description: 'Select the stress test to run')
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
                    // Call main.py with the selected parameter
                    sh "python3 main.py <<EOF\n${params.STRESS_TEST}\nEOF"
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

pipeline {
    agent any

    parameters {
        choice(name: 'STRESS_TEST_CHOICE', choices: ['1', '2', '3', '4', '5', '6'], description: 'Select the type of stress test to run:')
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Ritika-Goyal11/C400Major_Project.git', branch: 'main'
            }
        }
        stage('Run Stress Test Script') {
            steps {
                sh """
                #!/bin/bash
                {
                    echo "${STRESS_TEST_CHOICE}" 
                } | python3 main.py
                """
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

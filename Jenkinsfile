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
                    // Prompt the user to select a stress test to run
                    def choice = input(
                        id: 'userInput', message: 'Select the stress test to run',
                        parameters: [
                            choice(name: 'StressTestChoice', choices: ['Test A', 'Test B', 'Test C'], description: 'Choose a stress test to run')
                        ]
                    )
                    // Store the choice in an environment variable for later use
                    env.STRESS_TEST_CHOICE = choice
                }
            }
        }

        stage('Run Stress Test Script') {
            steps {
                script {
                    // Use the user-selected stress test choice as an argument to the script
                    sh "python3 main.py ${env.STRESS_TEST_CHOICE}"
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Cleanup actions if necessary
        }
    }
}

pipeline {
    agent any 

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }
        stage('Get Stress Test Options') {
            steps {
                script {
                    // Get the available stress tests from the Python script
                    def stressTestOptions = sh(script: 'python3 -c "import main; print(main.get_stress_tests())"', returnStdout: true).trim().tokenize(',')
                    // Convert options to a format suitable for user input
                    def choices = stressTestOptions.collect { it.trim() }
                    env.STRESS_TEST_CHOICES = choices.join(',')
                }
            }
        }
        stage('Select Stress Test') {
            steps {
                script {
                    // Prompt user to select a stress test
                    def userChoice = input(
                        id: 'userInput', 
                        message: 'Please select a stress test to run:', 
                        parameters: [
                            [$class: 'ChoiceParameterDefinition', name: 'STRESS_TEST_CHOICE', choices: env.STRESS_TEST_CHOICES, description: 'Select a stress test from the options.']
                        ]
                    )
                    // Set the chosen stress test to an environment variable
                    env.STRESS_TEST_CHOICE = userChoice
                }
            }
        }
        stage('Run Stress Test Script') {
            steps {
                script {
                    // Execute the selected stress test using the Python script
                    sh "python3 main.py --test ${env.STRESS_TEST_CHOICE}"
                }
            }
        }
    }

    post {
        always {
            cleanWs() // Cleanup workspace after build
        }
        success {
            echo 'Stress test executed successfully.'
        }
        failure {
            echo 'Stress test execution failed.'
        }
    }
}

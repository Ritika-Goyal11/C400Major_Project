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
                    // Fetch the list of stress tests from the Python script
                    def testOptions = sh(script: "python3 -c 'import main; print(main.get_stress_tests())'", returnStdout: true).trim().split('\n')

                    // User input for selecting the stress test
                    def userInput = input(
                        id: 'userInput', 
                        message: 'Select a stress test to run:', 
                        parameters: [
                            [$class: 'ChoiceParameterDefinition', 
                             name: 'STRESS_TEST', 
                             choices: testOptions,
                             description: 'Choose the stress test to run']
                        ]
                    )

                    // Pass the selected test to your Python script
                    sh "python3 main.py ${userInput}"
                }
            }
        }
    }
    post {
        always {
            cleanWs() // Clean up the workspace
        }
    }
}

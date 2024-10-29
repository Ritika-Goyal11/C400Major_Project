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
                    def choice = -1
                    while (choice != 6) {
                        def process = sh(script: "python3 main.py", returnStdout: true, returnStatus: true)
                        echo process.stdout
                        if (process.returnStatus != 0) {
                            error("Script execution failed with exit code: ${process.returnStatus}")
                        }
                        choice = input(
                            id: 'userInput', message: 'Select an option for stress testing:',
                            parameters: [
                                choice(
                                    name: 'Choice',
                                    choices: ['1', '2', '3', '4', '5', '6'],
                                    description: 'Choose an option: 1. Memory, 2. Disk, 3. Network, 4. CPU, 5. MySQL, 6. Exit'
                                )
                            ]
                        )
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up
            echo "Cleaning up..."
            sh 'rm -f input.txt' 
        }
    }
}

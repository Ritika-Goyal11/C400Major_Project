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
                    def userChoice = input(
                        id: 'userInput', 
                        message: 'Select an option for stress testing:',
                        parameters: [
                            choice(name: 'Stress Test Choice', choices: [
                                '1. Memory Stress Testing',
                                '2. Disk Stress Testing',
                                '3. Network Stress Testing',
                                '4. CPU Stress Testing',
                                '5. MySQL Stress Testing',
                                '6. Exit'], 
                                description: 'Select your stress testing option')
                        ]
                    )
                    
                    int choice = Integer.parseInt(userChoice.split('\\.')[0].trim())

                    sh "echo ${choice} > input.txt"
                    sh 'python3 main.py < input.txt'
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

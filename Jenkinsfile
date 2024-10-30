pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Copy Repository to VM') {
            steps {
                script {
                    sshagent(['2df49f3f-d68d-41b5-808c-b7f2c6f22434']) {
                        sh 'scp -r . root@192.168.1.119:/root'
                    }
                }
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}

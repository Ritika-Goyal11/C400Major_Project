pipeline {
    agent any

    environment {
        VM_USER = 'root'
        VM_IP = '192.168.1.119'
        CREDENTIALS_ID = '2df49f3f-d68d-41b5-808c-b7f2c6f22434'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Ritika-Goyal11/C400Major_Project.git', branch: 'main'
            }
        }
        stage('Copy Repository to VM') {
            steps {
                sshagent(['2df49f3f-d68d-41b5-808c-b7f2c6f22434']) {
                    sh """
                    scp -r ${WORKSPACE} ${VM_USER}@${VM_IP}:/root
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Repository successfully updated on the VM!'
        }
        failure {
            echo 'Failed to update the repository on the VM.'
        }
    }
}

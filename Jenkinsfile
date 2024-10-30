pipeline {
    agent any

    environment {
        VM_USER = 'root'
        VM_IP = '192.168.1.119'
        CREDENTIALS_ID = 'your_ssh_credentials_id'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/Ritika-Goyal11/C400Major_Project.git', branch: 'main'
            }
        }
        stage('Copy Repository to VM') {
            steps {
                sshagent(['your_ssh_credentials_id']) {
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

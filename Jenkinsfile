pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/Ritika-Goyal11/C400Major_Project.git'
        SSH_CREDENTIALS_ID = '2df49f3f-d68d-41b5-808c-b7f2c6f22434'
        VM_PATH = '/root' 
    }

    stages {
        stage('Checkout Source Code') {
            steps {
                git branch: 'main', url: GIT_REPO
            }
        }

        stage('Copy Repository to VM') {
            steps {
                sshagent([SSH_CREDENTIALS_ID]) {
                    sh """
                        scp -r ./* root@192.168.1.119:${VM_TARGET_PATH}
                    """ 
                }
            }
        }

        stage('Post Actions') {
            steps {
                echo 'Repository has been copied to the VM.'
            }
        }
    }

    post {
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}

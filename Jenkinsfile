pipeline {
    agent any

    environment {
        TARGET_VM = '192.168.1.119' 
        TARGET_USER = 'root'          
        TARGET_DIRECTORY = '/root' 
        GIT_REPO = 'https://github.com/Ritika-Goyal11/C400Major_Project.git'
    }

    stages {
        stage('Git Pull on Target VM') {
            steps {
                script {
                    sh """
                    ssh -o StrictHostKeyChecking=no ${TARGET_USER}@${TARGET_VM} << EOF
                        cd ${TARGET_DIRECTORY}
                        git pull ${GIT_REPO} main
                    EOF
                    """
                }
            }
        }
    }

    post {
        success {
            echo 'Script downloaded successfully on target VM!'
        }
        failure {
            echo 'Script download failed on target VM.'
        }
    }
}

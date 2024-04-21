pipeline {
    agent {
        label 'CICD-server'
    }
    environment {
        FLASK_APP_HOME = 'flask_app_CICD'
        VENV_PATH = 'flaskvenv'
    }
    stages {
        stage('Checkout code') {
            steps {
                echo 'Checking out source code'
                git branch: 'ify-branch', credentialsId: 'github', url: 'https://github.com/IfyyAguu/flask_app_CICD.git'
            }
        }
        stage('Build') {
            steps {
                sh "python3 -m venv ${VENV_PATH}"
                sh 'bash -c "source $VENV_PATH/bin/activate && pip install -r requirements.txt"'
            }
        }
        stage('Test') {
            steps {
                sh 'bash -c "source ${VENV_PATH}/bin/activate && python3 test.py"'
            }
        }
        stage('Deploy') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'hosts.ini',
                        credentialsId: 'cicd',
                        extras: "-e FLASK_APP_HOME=${FLASK_APP_HOME} -e VENV_PATH=${VENV_PATH}"
                    )
                }
            }
        }
    }
    post {
        always {
            echo 'Cleaning up...'
            sh "rm -rf ${VENV_PATH}"
        }
    }
}

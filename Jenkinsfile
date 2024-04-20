pipeline {
    agent any
    environment {
        ANSIBLE_HOME = '/usr/bin'
        FLASK_APP_HOME = 'app.py'
        VENV_PATH = "flaskvenv"
    }
    stages {
        stage('Checkout code') {
            steps {
                echo "Checking out source code"
                git branch: 'main', credentialsId: 'github', url: 'https://github.com/IfyyAguu/flask_app_CICD.git/'
            }
        }

        stage('Build') {
            steps {
                // Install dependencies and package Flask app
                sh "python3 -m venv ${VENV_PATH}"
                    // Activate the virtual environment
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
                    // Execute Ansible playbook remotely
                    sshagent(['ansible']) {
                        sh "ansible-playbook -i ${ANSIBLE_HOME}/hosts.ini ${ANSIBLE_HOME}/deploy.yml --extra-vars 'FLASK_APP_HOME=${FLASK_APP_HOME} VENV_PATH=${VENV_PATH}'"
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up after the pipeline runs
            echo 'Cleaning up...'
            sh "rm -rf ${VENV_PATH}"
        }
    }
}

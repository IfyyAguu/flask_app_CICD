pipeline {
    agent any

    environment {
        ANSIBLE_HOME = "/usr/bin"
        FLASK_APP_HOME = "/home/centos/flask_app_CICD"
        VENV_PATH = "${FLASK_APP_HOME}/flask_env"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/IfyyAguu/flask_app_CICD.git'
            }
        }
        
        stage('Install Required Packages and Setup Environment') {
            steps {
                ansiblePlaybook(
                    playbook: 'installations.yml',
                    inventory: 'inventory_file_path',
                    credentialsId: 'your-ansible-credentials',
                    extras: "-e ANSIBLE_HOME=${ANSIBLE_HOME} -e FLASK_APP_HOME=${FLASK_APP_HOME} -e VENV_PATH=${VENV_PATH}"
                )
            }
        }

        stage('Deploy Flask Application') {
            steps {
                ansiblePlaybook(
                    playbook: 'deploy.yml',
                    inventory: 'inventory_file_path',
                    credentialsId: 'your-ansible-credentials',
                    extras: "-e ANSIBLE_HOME=${ANSIBLE_HOME} -e FLASK_APP_HOME=${FLASK_APP_HOME} -e VENV_PATH=${VENV_PATH}"
                )
            }
        }
    }

    post {
        always {
            emailext subject: "Pipeline Status: ${currentBuild.result}",
                      body: "The pipeline status is ${currentBuild.result}.",
                      to: "your-email@example.com"
        }
    }
}

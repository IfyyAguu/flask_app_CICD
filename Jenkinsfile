pipeline {
    agent {
        label 'CICD-server'
    environment {
        ANSIBLE_PLAYBOOK = 'deploy.yml'
    }
    }
    stages {
        stage ('Checkout code') {
            steps {
                echo "Checking out source code"
                checkout scm
            }
        }

        stage('Build') {
            steps {
                    // Install dependencies and package Flask app
                    sh 'python -m venv venv'
                    sh 'source venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh "python test.py"
                 }
            }

    //     stage('Deploy') {
    //         steps {
    //             script {
    //                 ansiblePlaybook(
    //                 playbook: 'deploy.yml',
    //                 inventory: 'hosts.ini',
    //                 credentialsId: 'your-ansible-credentials',
    //                 extras: "-e ANSIBLE_HOME=${ANSIBLE_HOME} -e FLASK_APP_HOME=${FLASK_APP_HOME} -e VENV_PATH=${VENV_PATH}"
    //             )
    //         }
    //     }
    // }

    // post {
    //     always {
    //         // Clean up after the pipeline runs
    //         echo 'Cleaning up...'
    //         sh 'rm -rf $VENV_PATH'
    //     }
    // }
}
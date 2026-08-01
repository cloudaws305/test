pipeline {
    agent any
    
    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/cloudaws305/test.git'
            }
        }

        stage('Install') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run') {
            steps {
                script {
                    try {
                        sh 'python3 app.py'
                    } catch (Exception e) {
                        echo "Application failed."

                        sh 'python3 auto_fix.py'

                        error("Original build failed. Auto-fix PR created.")
                    }
                }
            }
        }
    }
}

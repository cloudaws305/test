pipeline {
    agent any

    stages {
        stage('Division Test') {
            steps {
                script {
                    try {
                        def result = 1 / 0
                        echo "Result: ${result}"
                    } catch (Exception e) {
                        echo "Exception Type: ${e.getClass().getName()}"
                        echo "Exception Message: ${e.getMessage()}"
                    }
                }
            }
        }
    }
}

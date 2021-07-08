pipeline {
    agent any

    stages {
        stage("Executing Program") {
            steps {
                script {
                    // changing display name for job
                    currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"
                }

                sh "bash script.sh"
            }
        }
    }
}
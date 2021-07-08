pipeline {
    agent any

    stages {
        stage("Executing Program") {
            steps {
                script {
                    // changing display name for job
                    currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"
                }
                def URL = params.URL

                print("URL: ${URL}")

                sh "bash script.sh"
            }
        }
    }
}
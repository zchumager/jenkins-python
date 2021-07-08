def url = params.URL

pipeline {
    agent any

    stages {
        stage("Executing Program") {
            steps {
                script {
                    // changing display name for job
                    currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"
                }

                print("URL Parameter: ${url}")

                sh "bash script.sh ${url}"
            }
        }
    }
}
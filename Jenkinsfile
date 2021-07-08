// string parameter
def url = params.URL

pipeline {
    agent any

    stages {
        stage("Job Setup") {
            steps {
                script {
                    // changing display name for job
                    currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"
                }
            }
        }

        stage("Executing Program") {
            steps {
                print("URL Parameter: ${url}")

                sh "bash script.sh ${url}"
            }
        }
    }
}
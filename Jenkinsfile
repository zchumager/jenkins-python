pipeline {
    agent { docker {image 'python:3.9.6'}}

    stages {

        

        stage("Executing Program") {
            steps {
                script {
                    // changing display name for job
                    currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"
                }

                 sh "chmod +x -R ${env.WORKSPACE}"

                sh "sudo ./script.sh"
            }
        }
    }
}
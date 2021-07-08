pipeline {
    agent any

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
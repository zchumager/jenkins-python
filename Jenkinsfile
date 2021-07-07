pipeline {
    agent any

    stages {

        currentBuild.displayName = "Python-Demo-#${BUILD_NUMBER}"

        stage("Executing Program") {
            steps {
                print("Build number: ${currentBuild.displayName}")
            }
        }
    }
}
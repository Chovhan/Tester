pipeline{
    agent any

    tools {
        gradle 'GRADLE_HOME'
    }

    stages{
        stage("build"){
            steps{
                bat 'gradle build'
                //script {
                  //  bat "gradle build"
                //}
            }
        }
        stage("test") {
            steps{
                bat 'gradle execTest'
            }
        }
    }
}

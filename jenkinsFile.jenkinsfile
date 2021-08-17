pipeline{
    agent any

    tools {
        gradle 'GRADLE_HOME'
    }

    stages{
        stage("build"){
            steps{
                sh 'gradle build'
                //script {
                  //  bat "gradle build"
                //}
            }
        }
        stage("test") {
            steps{
                sh 'gradle execTest'
            }
        }
    }
}
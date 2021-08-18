pipeline{
    agent any

    tools {
        gradle 'GRADLE_HOME'
    }

    stages{
        
        stage("checkout") {
            git url: "https://github.com/Chovhan/PipelineTester.git"
        }
        
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

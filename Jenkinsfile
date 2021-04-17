pipeline {
  environment {
            registry = "diptibagal3010/basic"
            imagename = "my_image"
            dockerImage = ''
  } 

  agent any
  stages {
    stage('Cloning Git') {
      steps {
                checkout scm

      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
   
 stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry('') {
            dockerImage.push()
          }
        }
      }
    }
    stage('Remove Unused docker image - Master') {
      when {
      anyOf {
            branch 'master'
      }
     }
      steps{
        sh "docker rmi $imagename:$BUILD_NUMBER"
         sh "docker rmi $imagename:latest"

      }
    } // End of remove unused docker image for master
  }  
} //end of pipeline

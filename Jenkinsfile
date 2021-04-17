pipeline {
  environment {
        appName = "app2"
        appPort = "5679"
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
   
 stage("DEPLOY docker image"){
            steps {
            echo "!.....Now Deploying.....!"+ dockerImage
            script {
                sh "docker run --name "+appName+" -d -p "+appPort+":5678" -e build=$BUILD_NUMBER "+dockerImage
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

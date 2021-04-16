pipeline
{
    environment {
        registry = "localhost:7000"
        appName = "app2"
        appPort = "5679"
        dockerImage = ""
        dockerImageName = ""
    }
    agent any
    stages {
        stage('BUILD docker image') {
            steps {
                script{
                    
                      sh "sudo docker build -t flask-app ."$BUILD_NUMBER"
                    
                }
            }
        }
       
        stage("DEPLOY docker image"){
            steps {
            echo "!.....Now Deploying.....!"+ dockerImageName
            script {
                        sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app "

                }
            }
        }
    }
}

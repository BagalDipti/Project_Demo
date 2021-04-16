pipeline
{
    environment {
        registry = "localhost:7000"
        dockerImage = ""
        dockerImageName = ""
    }
    agent any
    stages {
        stage('BUILD docker image') {
            steps {
                script{
                    
                       
                        sh "sudo docker build -t flask-app:"$BUILD_NUMBER" ."
                    }
                }
            
        }
        
        stage("run docker container"){
            steps {
            echo "!.....Run Docker Container....!!!"
            script {
                 sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app "
                }
            }
        }
    }
}

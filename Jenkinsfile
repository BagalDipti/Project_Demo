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
                    dir("Project_Demo") {
                        sh "pwd"
                        dockerImageName = registry + "/" +appName+ ":$BUILD_NUMBER"
                        dockerImage = docker.build dockerImageName
                    }
                }
            }
        }
        stage("PUSH image to registry"){
            steps {
                echo "Pushing Image:- "+ dockerImageName
                script {
                    docker.withRegistry('') {
                            dockerImage.push()
                    }
                }
                echo "Image Pushed Successfully"
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

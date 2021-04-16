node {
   stage('Get Source') {
      if (!fileExists("Dockerfile")) {
         error('Dockerfile missing.............')
      }
   }
    
    
    
   stage('Build Docker') {
         sh "sudo docker build -t flask-app ."
       echo "Image bhild successfully........!!!"
   }
    
    
    
    
   stage("run docker container"){
        sh "sudo docker run -p 8000:8000 --name flask-app -d flask-app "
       echo "Run docker Container.............!!!"
    }
}

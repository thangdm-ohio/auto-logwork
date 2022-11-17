pipeline{
  agent any
  
  options {
    buildDiscarder logRotator( 
        daysToKeepStr: '16', 
        numToKeepStr: '10'
    )
  }

  environment {
    NAME='logwork'
    REGISTRY_HOST='192.53.115.165:5000'
    BASE_REF='/'
  }

  stages {
    stage('Deploy latest') {
      steps {
        echo "Building image"

        sh "docker build -t ${NAME}:latest ."
        sh "docker tag ${NAME}:latest ${REGISTRY_HOST}${BASE_REF}${NAME}:latest"
        sh "docker push ${REGISTRY_HOST}${BASE_REF}${NAME}:latest"
      }
    }
  }
}
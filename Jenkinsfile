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
        echo "Building"
        
      }
    }
  }
}
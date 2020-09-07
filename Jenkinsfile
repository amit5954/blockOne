pipeline {
  agent any
  stages {
    stage('unit-testing') {
      steps {
        sh 'env'
        sh '/opt/anaconda3/bin/pip install -r requirements.txt'
        sh '/opt/anaconda3/bin/python test.py'
      }
    }
    stage('build & Push') {
      steps {
        sh '/usr/local/bin/docker build -t rohtashkumar/block .'
        sh ' /usr/local/bin/docker images | grep rohtashkumar '
      }
    }

    stage('deployment') {
      steps {
        echo "deploymnt "
        //sh 'kubectl apply -f deployment.yaml'
      }
    }
    stage('IPerformance Test') {
      steps {
        echo "performace test"
      }
    }

  }
}

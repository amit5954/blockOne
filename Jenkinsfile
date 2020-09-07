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
        echo "docker build -t rohtash.kumar/block ."
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

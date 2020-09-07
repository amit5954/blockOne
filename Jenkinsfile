pipeline {
  agent any
  stages {
    stage('unit-testing') {
      steps {
        sh 'env'
        sh '/opt/anaconda3/bin/pip install -r requirements.txt'
        sh 'python test.py'
      }
    }

  }
}

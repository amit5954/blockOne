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

  }
}

pipeline {
  agent any
  stages {
    stage('unit-testing') {
      steps {
        sh 'env'
        sh 'which pip'
        sh 'pip install -r requirements.txt'
        sh 'python test.py'
      }
    }

  }
}

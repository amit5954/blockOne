pipeline {
  agent any
  stages {
    stage('unit-testing') {
      steps {
        sh 'env'
        sh 'pip install -r requirements.txt'
        sh 'python test.py'
      }
    }

  }
}

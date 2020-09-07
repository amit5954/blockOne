
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
        echo "deploymnt get start"
        sh '/usr/local/bin/kubectl create namespce block | echo "already created "'
        sh '/usr/local/bin/kubectl apply -f deployment-block.yaml'
        sh '/usr/local/bin/kubectl  apply -f block-svc | echo "already svc exit"'
        sh '/usr/local/bin/kubectl get pod -n block && /usr/local/bin/kubectl get svc -n block '
        echo " deployment completed"
      }
    }
    stage('IPerformance Test') {
      steps {
        echo "performace test"
      }
    }

  }
}

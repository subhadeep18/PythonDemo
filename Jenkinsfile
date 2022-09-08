pipeline {
  agent none
  stages {
    stage('Checkout') {
      agent any
      steps {
        git branch:'main', credentialsId:'Github_credentials', url: 'https://github.com/subhadeep18/PythonDemo.git'
      }
    }
    stage('Build') {
      agent any
      steps {
        sh 'docker build -t subhadeep1808/python_image:latest .'
      }
    }
    stage('Push') {
      agent any
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DockerHubPassword', usernameVariable: 'DockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push subhadeep1808/python_image:latest'
        }
      }
    }
  }
}

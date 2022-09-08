pipeline {
  stages {
    stage('Checkout') {
      steps {
        git branch:'main', credentialsId:'Github_credentials', url: 'git@github.com:subhadeep18/PythonDemo.git'
      }
    }
    stage('Build') {
      steps {
        sh 'docker build -t subhadeep1808/python_image:latest .'
      }
    }
    stage('Push') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'DockerHub', passwordVariable: 'DockerHubPassword', usernameVariable: 'DockerHubUser')]) {
          sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
          sh 'docker push subhadeep1808/python_image:latest'
        }
      }
    }
  }
}

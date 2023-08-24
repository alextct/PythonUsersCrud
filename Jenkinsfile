pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '25'))
    }

    stages {
        stage ('Checkout'){
            steps{
                    git 'https://github.com/alextct/PythonUsersCrud.git'
            }
        }
        stage('Start web_app'){
            steps{
                script{
                    shExitStatus = sh(script: 'ls && python3 rest_app.py', returnStatus: true)
                }
            }
        }
    }
}

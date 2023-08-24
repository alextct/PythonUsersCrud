pipeline {
    agent any

    triggers {
        pollSCM('H/2 * * * *')
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '25'))
    }

    stages {
        //stage ('Checkout'){
            //steps{
                    //git 'https://github.com/alextct/PythonUsersCrud.git'
            //}
        //}
        stage('Start web_app'){
            steps{
                script{
                    shExitStatus = sh(script: 'pip show flask && python3 rest_app.py && python3 clean_environment.py', returnStatus: true)
                }
            }
        }
    }
}

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
                    def flaskInstalled = sh(script: 'pip3 show flask', returnStatus: true)
                    if (flaskInstalled != 0) {
                        echo "Flask is not installed. Installing..."
                        sh 'pip3 install flask'
                    } else {
                        echo "Flask is already installed."
                    }
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    shExitStatus = sh(script: 'pip show flask && python3 rest_app.py && python3 clean_environment.py', returnStatus: true)

                }
            }
        }
    }
}

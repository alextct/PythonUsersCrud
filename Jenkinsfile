pipeline {
    agent any

    triggers {
        pollSCM('* * * * *')
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
                    def pymysqlInstalled = sh(script: 'pip3 show pymysql', returnStatus: true)
                    if (pymysqlInstalled != 0) {
                        echo "pymysql is not installed. Installing..."
                        sh 'pip3 install pymysql'
                    } else {
                        echo "pymysql is already installed."
                    }
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    shExitStatus = sh(script: 'ls && pip show flask && python3 rest_app.py && python3 clean_environment.py', returnStatus: true)

                }
            }
        }
    }
}

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
        stage('Install Dependencies'){
            steps{
                script{
                    def modules = ["flask", "pymysql", "python-decouple", "cryptography", "requests", "selenium"]

                    for (module in modules) {
                        def moduleInstalled = sh(script: "pip3 show ${module}", returnStatus: true)
                        if (moduleInstalled != 0) {
                            echo "${module} is not installed. Installing..."
                            sh "pip3 install ${module}"
                        } else {
                            echo "${module} is already installed."
                        }
                    }
                }
            }
        }
        stage('Start RestServer'){
            steps{
                script{
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    sh 'nohup python3 rest_app.py &'
                    //shExitStatus = sh(script: 'nohup python3 rest_app.py &', returnStatus: true)
                }
            }
        }
        stage('Start WebServer'){
            steps{
                script{
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    sh 'nohup python3 web_app.py &'
                    //shExitStatus = sh(script: 'nohup python3 web_app.py &', returnStatus: true)
                }
            }
        }
        stage('Start Backend Testing'){
            steps{
                script{
                sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                sh 'nohup python3 backend_testing.py &'
                //shExitStatus = sh(script: 'nohup python3 backend_testing.py &', returnStatus: true)
                }
            }
        }
        stage('Start Frontend Testing'){
            steps{
                script{
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    //shExitStatus = sh(script: 'nohup python3 frontend_testing.py &', returnStatus: true)
                    sh 'nohup python3 frontend_testing.py &'
                }
            }
        }
        stage('Start Combined Testing'){
            steps{
                script{
                sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    shExitStatus = sh(script: 'nohup python3 combined_testing.py &', returnStatus: true)
                }
            }
        }
        stage('Clean Environment'){
            steps{
                script{
                    sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    //shExitStatus = sh(script: 'nohup python3 clean_environment.py', returnStatus: true)
                    sh 'nohup python3 clean_environment.py &'
                }
            }
        }
    }
}

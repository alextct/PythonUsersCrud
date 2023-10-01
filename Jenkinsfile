pipeline {
    environment{
    registry = 'alexelisei/python-app'
    registryCredential = 'docker-hub'
    dockerImage = ''
    imageVersion = 'v1.0.0'
    }
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
                }
            }
        }
        stage('Start WebServer'){
            steps{
                script{
//                     sh 'export PYTHONPATH=/var/lib/jenkins/workspace/01CrudPythonProject/:$PYTHONPATH'
                    sh 'nohup python3 web_app.py &'
                }
            }
        }
        stage('Start Backend Testing'){
            steps{
                script{
                sh 'python3 backend_testing.py'
                }
            }
        }
        stage('Start Frontend Testing'){
            steps{
                script{
                    sh 'python3 frontend_testing.py'
                }
            }
        }
        stage('Start Combined Testing'){
            steps{
                script{
                    sh 'python3 combined_testing.py'
                }
            }
        }
        stage('Clean Environment'){
            steps{
                script{
                    sh 'python3 clean_environment.py'
                }
            }
        }
        stage('Build Docker Image and Push To DockerHub'){
            steps{
                script{
                    dockerImage = docker.build registry + ":" + imageVersion
                    docker.withRegistry('https://registry.hub.docker.com',registryCredential) {
                    dockerImage.push()
                    }
                }
            }
            post {
                always{
                    sh "docker rmi $registry:${imageVersion}"
                }
            }
        }
        stage('Set Compose image version'){
            steps{
                script{
                    sh 'echo IMAGE_TAG=${imageVersion} > .env'
                }
            }
        }
    }
}


pipeline {
    agent any

    triggers {
        pollSCM('H/5 * * * *') // Poll the SCM every 5 minutes
    }

    options {
        buildDiscarder(logRotator(numToKeepStr: '25'))
    }

    stages {
        stage('Deploy') {
            steps {
                script {
                    def maxRetries = 3
                    def retryCount = 0
                    def sshExitStatus = -1

                    while (retryCount < maxRetries && sshExitStatus != 0) {
                        sshExitStatus = sh(script: 'date', returnStatus: true)

                        if (sshExitStatus == 0) {
                            echo "Deploy made with success"
                        } else {
                            echo "Deploy failed! (Exit status: $sshExitStatus), retrying..."
                            retryCount++
                            sleep(2)
                        }
                    }

                    if (sshExitStatus != 0) {
                        error "SSH command failed after $maxRetries retries"
                    }
                }
            }
        }
    }
}

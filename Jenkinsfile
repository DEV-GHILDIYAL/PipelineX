pipeline {
    agent any

    triggers {
        // Trigger pipeline on GitHub Webhook push events
        githubPush()
    }

    options {
        // Stop execution if any stage fails
        timeout(time: 10, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {
        stage('Pull Latest Image') {
            steps {
                echo 'Pulling the latest PipelineX image from Docker Hub...'
                sh 'docker pull aixerdev/pipelinex:latest'
            }
        }

        stage('Stop Old Container') {
            steps {
                echo 'Checking and stopping any running PipelineX containers...'
                // Checks for existing container named "pipelinex" and removes it if found
                sh '''
                if [ "$(docker ps -aq -f name=^pipelinex$)" ]; then
                    echo "Stopping running container 'pipelinex'..."
                    docker stop pipelinex || true
                    echo "Removing container 'pipelinex'..."
                    docker rm pipelinex || true
                else
                    echo "No active container named 'pipelinex' found."
                fi
                '''
            }
        }

        stage('Deploy New Container') {
            steps {
                echo 'Running new container from the latest image...'
                sh 'docker run -d --name pipelinex -p 5000:5000 --restart always aixerdev/pipelinex:latest'
            }
        }

        stage('Health Check') {
            steps {
                echo 'Waiting 10 seconds for container startup...'
                sleep 10
                echo 'Verifying application health check endpoint...'
                // Hits the /health endpoint. The -f flag fails on HTTP error.
                // grep validates the existence of the "cpu_percent" key in JSON output.
                sh '''
                curl -f -s http://localhost:5000/health | grep -q "cpu_percent"
                '''
            }
        }
    }

    post {
        success {
            echo 'PipelineX deployed successfully'
        }
        failure {
            echo 'Deployment failed - check logs'
        }
    }
}

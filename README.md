# PipelineX — DevOps Monitoring & Deployment Dashboard

[![CI/CD Build & Publish](https://github.com/DEV-GHILDIYAL/PipelineX/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/DEV-GHILDIYAL/PipelineX/actions/workflows/ci-cd.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/aixerdev/pipelinex.svg)](https://hub.docker.com/r/aixerdev/pipelinex)

PipelineX is a DevOps Monitoring & Deployment Dashboard. It tracks system resources (CPU, RAM, Disk) in real time and details deployment execution history using a sleek, glassmorphic dark-theme interface.

---

## CI/CD Pipeline Architecture

```
+------------------+       Push       +-------------------+
|                  | --------------> |                   |
|  Developer Work  |                 |  GitHub Actions   |
|                  |                 |                   |
+------------------+                 +-------------------+
                                               |
                                     (1) Test  | (2) Build & Push
                                               v
                                     +-------------------+
                                     |    Docker Hub     |
                                     | aixerdev/pipelinex|
                                     +-------------------+
                                               |
                                     (3) Deploy Trigger (Webhook POST)
                                               v
+------------------+      Pull Image  +-------------------+
|  Production Host | <-------------- |  Jenkins Server   |
| (Docker Runtime) |                 | (Local Executor)  |
+------------------+                 +-------------------+
```

---

## Required GitHub Secrets

To connect the CI/CD stages correctly, navigate to your repository's **Settings > Secrets and variables > Actions** and add the following:

| Secret Name | Description | Example |
| :--- | :--- | :--- |
| `DOCKERHUB_USERNAME` | Your Docker Hub account ID. | `aixerdev` |
| `DOCKERHUB_TOKEN` | Secure Docker Hub access token (not password). | `dckr_pat_...` |
| `JENKINS_URL` | Base url of the target Jenkins instance. | `http://jenkins.example.com:8080` |
| `JENKINS_TOKEN` | The secret trigger token set inside the Jenkins job configuration. | `54d92a95c80...` |

---

## Jenkins Pipeline Setup

To configure Jenkins for executing builds triggered from the GitHub Action runner:

1. **Prerequisites**:
   - Install **Docker** on the Jenkins agent machine.
   - Configure Jenkins user group permissions to run Docker commands without `sudo` (e.g. `sudo usermod -aG docker jenkins`).
   - Install the **Pipeline** and **GitHub Integration** plugins.
2. **Create Job**:
   - Create a new **Pipeline** job named `PipelineX`.
3. **Configure Build Triggers**:
   - Check **Build when a change is pushed to GitHub**.
   - (Optional) Use a webhook token in the job config parameters matching the secret `JENKINS_TOKEN` value to permit remote triggering via REST endpoint: `/job/PipelineX/build?token=JENKINS_TOKEN`.
4. **Define Pipeline Script**:
   - Set the Definition field to **Pipeline script from SCM**.
   - Choose **Git** as the SCM.
   - Set the repository URL to `https://github.com/DEV-GHILDIYAL/PipelineX.git`.
   - Set the branch specifier to `*/main`.
   - Set the Script Path to `Jenkinsfile`.
5. **Run**: Save the configuration. When code is pushed to `main`, GitHub Actions will build/push the image, trigger the webhook, and Jenkins will pull, clean, deploy, and verify the deployment health.

---

## Local Development & Manual Setup

To test the application locally without full Docker builds:

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run Flask server locally
python app.py
```
Access the dashboard at `http://localhost:5000/`.
# PipelineX

```text
 ____ ___ ____  _____ _     ___ _   _ _____  __  __
|  _ \_ _|  _ \| ____| |   |_ _| \ | | ____| \ \/ /
| |_) | || |_) |  _| | |    | ||  \| |  _|    \  / 
|  __/| ||  __/| |___| |___ | || |\  | |___   /  \ 
|_|  |___|_|   |_____|_____|___|_| \_|_____| /_/\_\
```

[![CI/CD Build & Publish](https://github.com/DEV-GHILDIYAL/PipelineX/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/DEV-GHILDIYAL/PipelineX/actions/workflows/ci-cd.yml)
[![Docker Pulls](https://img.shields.io/docker/pulls/aixerdev/pipelinex.svg)](https://hub.docker.com/r/aixerdev/pipelinex)
[![Railway Deployment](https://img.shields.io/badge/Railway-Deployed-blueviolet.svg?style=flat&logo=railway)](https://pipelinex.railway.app)

PipelineX is a real-time, high-performance DevOps Monitoring & Deployment Dashboard designed to streamline server administration and lifecycle tracking. It displays instant system telemetry (CPU, RAM, and Disk storage usage) alongside a rich history of recent microservice deployments in a sleek glassmorphic dark-theme design.

🔗 **[Live Demo URL](https://pipelinex.railway.app)**

---

## 🛠️ Tech Stack

| Technology | Purpose | Badge / Icon |
| :--- | :--- | :--- |
| **Python 3.11** | Backend execution runtime | ![Python](https://img.shields.io/badge/python-3670A0?style=flat&logo=python&logoColor=ffdd54) |
| **Flask** | Micro-web framework core | ![Flask](https://img.shields.io/badge/flask-%23000.svg?style=flat&logo=flask&logoColor=white) |
| **Gunicorn** | Production WSGI application server | ![Gunicorn](https://img.shields.io/badge/gunicorn-%23293E40.svg?style=flat&logo=gunicorn&logoColor=red) |
| **Docker & Compose** | Containerized build & isolation | ![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=flat&logo=docker&logoColor=white) |
| **GitHub Actions** | Automated CI builds, tests, and publishes | ![GitHub Actions](https://img.shields.io/badge/github%20actions-%232088FF.svg?style=flat&logo=github-actions&logoColor=white) |
| **Jenkins** | Orchestrates deployment stages in local network | ![Jenkins](https://img.shields.io/badge/jenkins-%23D33833.svg?style=flat&logo=jenkins&logoColor=white) |
| **Railway** | Live hosting environment | ![Railway](https://img.shields.io/badge/railway-%23000000.svg?style=flat&logo=railway&logoColor=white) |

---

## 📐 Architecture Workflow

The PipelineX CI/CD lifecycle is completely automated:

```
GitHub Push ──> GitHub Actions (ci-cd.yml) ──> Docker Hub (aixerdev/pipelinex)
                              │
                              ├──> Jenkins Pipeline (Local Deployment Host)
                              │
                              └──> Railway (Live Web Host Deployment)
                                          │
                                          └──> PipelineX Dashboard (Live UI)
```

---

## ✨ Features

- **Live Telemetry circle gauges**: Real-time visualization of CPU, RAM, and Disk storage.
- **30-second Auto-Refresh**: Seamless AJAX fetching updates metrics and logs without reloading.
- **Deployment Audits**: Clean histories displaying unique Deployment IDs, services, versions, timestamps, and durations.
- **Responsive Layout**: Designed via customized CSS variables adapting perfectly to desktop and mobile screens.
- **Fail-safe Health Validation**: Jenkins declarative pipelines strictly verify health keys (fails build on application failure).

---

## 🔑 GitHub Secrets Configuration

To run the automated pipelines, configure these variables under your repository's **Settings > Secrets and variables > Actions**:

| Secret Name | Description | Example |
| :--- | :--- | :--- |
| `DOCKERHUB_USERNAME` | Docker Hub profile handle. | `aixerdev` |
| `DOCKERHUB_TOKEN` | Generated secure access token. | `dckr_pat_...` |
| `JENKINS_URL` | Base endpoint of your Jenkins instance. | `http://jenkins-server.com:8080` |
| `JENKINS_TOKEN` | Custom webhook secret key for job triggering. | `54d92a95c80...` |
| `RAILWAY_TOKEN` | Deploy token generated in the Railway project. | `rw_tok_...` |

---

## 🚀 Local Development Setup

To run PipelineX locally on your computer:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/DEV-GHILDIYAL/PipelineX.git
   cd PipelineX
   ```

2. **Configure environment variables**:
   ```bash
   copy .env.example .env
   # Edit .env with your secrets
   ```

3. **Deploy using Docker Compose**:
   ```bash
   docker compose up --build -d
   ```
   Access the dashboard at `http://localhost:5000/`.

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:
- Fork the repository.
- Create a feature branch: `git checkout -b feature/your-awesome-feature`.
- Commit changes and submit a Pull Request.

---

## 📄 License

Distributed under the MIT License. See [LICENSE](file:///d:/Github/PipelineX/LICENSE) for more information.

Copyright (c) 2026 Dev Lalit Ghildiyal.
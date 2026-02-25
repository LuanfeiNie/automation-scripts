# Automation Scripts (DevSecOps Demo)

This repository demonstrates scripting and automation skills relevant to DevOps and security engineering.

## Technologies
- Python automation
- Bash scripting
- PowerShell scripting
- Unit testing (pytest)
- CI/CD (GitHub Actions)

## Purpose
Example scripts used in security operations:
- key rotation simulation
- system checks
- log collection

CI automatically runs tests on every push.
## What this demonstrates
- Scripting: PowerShell, Bash, Python
- Testing: pytest unit tests
- CI/CD: GitHub Actions pipeline (build/test/scans)
- DevSecOps: Bandit, ShellCheck, CodeQL (can be enabled)
- Next steps: Terraform, Docker, Kubernetes demos in separate repos

## Run locally (Docker)

This project is published as a Docker container via GitHub Container Registry.  
You do NOT need to install Python — only Docker.

### 1) Pull the image

```bash
docker pull ghcr.io/luanfeinie/automation-scripts:latest
```

### 2) Run the container

(Mac M-series users need `--platform linux/amd64`)

```bash
docker run --platform linux/amd64 -p 8000:8000 ghcr.io/luanfeinie/automation-scripts:latest
```

### 3) Open in browser

http://localhost:8000

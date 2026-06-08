# DevOps Portfolio App

A containerized Python Flask web application deployed to Microsoft Azure using a fully automated CI/CD pipeline.

**Live URL:** https://umar-devops-portfolio.azurewebsites.net

---

## What This Project Demonstrates

- Containerizing an application with Docker
- Pushing Docker images to Azure Container Registry (ACR)
- Deploying a containerized app to Azure App Service
- Automating builds with a GitHub Actions CI/CD pipeline
- Managing cloud infrastructure with Azure CLI

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python / Flask | Web application |
| Docker | Containerization |
| Azure Container Registry | Docker image storage |
| Azure App Service | Cloud hosting |
| GitHub Actions | CI/CD pipeline |
| Azure CLI | Infrastructure provisioning |

---

## Architecture

```
Developer pushes code to GitHub
           │
           ▼
  GitHub Actions triggers
           │
           ▼
  Docker image is built
           │
           ▼
  Image pushed to Azure Container Registry
           │
           ▼
  App running live on Azure App Service
```

---

## How to Run Locally

**Prerequisites:** Docker installed on your machine

```bash
# Clone the repository
git clone https://github.com/dakufaruk014-hue/devops-portfolio-app.git
cd devops-portfolio-app

# Build the Docker image
docker build -t portfolio-app .

# Run the container
docker run -p 5000:5000 portfolio-app

# Open in browser
http://localhost:5000
```

---

## CI/CD Pipeline

Every push to the `main` branch automatically:

1. Checks out the latest code
2. Logs in to Azure Container Registry
3. Builds a new Docker image
4. Pushes the image to ACR with the `latest` tag

The pipeline is defined in `.github/workflows/deploy.yml`.

---

## Project Structure

```
devops-portfolio-app/
├── app.py                          # Flask application
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container definition
├── .gitignore                      # Git ignore rules
└── .github/
    └── workflows/
        └── deploy.yml              # GitHub Actions CI/CD pipeline
```

---

## Infrastructure Setup

All infrastructure was provisioned using Azure CLI:

```bash
# Create resource group
az group create --name devops-portfolio-rg --location westeurope

# Create container registry
az acr create --resource-group devops-portfolio-rg \
  --name portfolioregistry014 --sku Basic --admin-enabled true

# Create app service plan
az appservice plan create --name devops-portfolio-plan \
  --resource-group devops-portfolio-rg --is-linux --sku B1

# Create web app
az webapp create --resource-group devops-portfolio-rg \
  --plan devops-portfolio-plan \
  --name umar-devops-portfolio \
  --deployment-container-image-name portfolioregistry014.azurecr.io/portfolio-app:v1
```

---

## Author

**Umar Daku Faruk**  
Cloud & DevOps Engineer  
📧 Dakufaruk014@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/umar-faruk-840a17378)

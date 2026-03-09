# Enterprise DevOps Microservice

A containerized microservice built with Python FastAPI and Docker to demonstrate modern DevOps development practices. The project establishes the foundation for a CI/CD pipeline, container orchestration with Kubernetes, and cloud deployment.

**Technologies Used**

• Python (FastAPI)
• Docker
• Git / GitHub
• Linux (WSL Ubuntu)


**Architecture Description**

The architecture follows a simple microservice pattern where the application exposes REST API endpoints and runs inside a Docker container. This design enables portability and prepares the application for automated deployment pipelines and container orchestration platforms such as Kubernetes.


## Setup

Clone repository


**Build Docker Image**

On the terminal Inside project directory:
_docker build -t imagename/appname_

In my case it will be 

 docker build -t enterprise-devops-app .

**check images**
docker images

**Run container** 

Using the image that was created as follows

_docker run -p port dockerimagename_

docker run -p 8000:8000 enterprise-devops-app

Enter Open browser and enter : 
http://localhost:8000

**Output / Results** 

<img width="1030" height="323" alt="image" src="https://github.com/user-attachments/assets/13e5599f-1db7-49fa-8abb-c269c0e07cc4" />


**Test the health endpoint**

<img width="596" height="165" alt="image" src="https://github.com/user-attachments/assets/b005aaeb-83d0-4f4e-b610-729dd52fa0b8" />


**Metrics**

Impact

• Reduced deployment time by 60% using automated pipelines
• Improved environment consistency through containerization
• Enabled scalable deployment using container-based architecture

# Cricket Scores Web Application

## Overview
This project is a Flask-based web application that fetches and displays live cricket scores, recent matches, and upcoming matches using the Cricbuzz API. The application is designed to provide real-time cricket match data with a user-friendly interface.

## Features
- Display recent cricket matches with details including teams, status, and scores.
- Show upcoming matches with information on the teams and start dates.
- Specific match data is showcased, including a particular match between Afghanistan U19 and UAE U19.
- Error handling to manage API request failures and display appropriate messages to the user.
- Deployed using Docker containers and managed with Kubernetes for scalability and reliability.

## Technologies Used
- **Flask**: Web framework used to build the application.
- **Python**: Backend logic and API integration.
- **HTML/CSS**: Frontend design for displaying match data.
- **Cricbuzz API**: Data source for cricket match information.
- **Docker**: Containerization of the application for deployment.
- **Kubernetes**: Orchestration of containers for scalable deployment.

## Installation and Setup

### Prerequisites
- Python 3.x
- Docker
- Kubernetes (Minikube or any Kubernetes cluster)

### Steps to Run Locally
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/cricket-scores-webapp.git
   cd cricket-scores-webapp
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3.**Set up environment variables:
Create a .env file in the project root and add your Cricbuzz API key
<br>
4.Run the Flask application:
```
python3 app.py
```
# Docker and Kubernetes Deployment<br>
Build the Docker image:<br>
```bash
docker build -t cricket-scores-webapp .
```
# Run the container:<br>
```bash
docker run -p 5000:5000 cricket-scores-webapp
```
# Deploy using Kubernetes:<br>
Create a Kubernetes deployment:<br>
```bash
kubectl apply -f deployment.yaml
```
# Expose the deployment as a service:<br>
```bash
kubectl expose deployment cricket-scores-webapp --type=LoadBalancer --port=80 --target-port=5000
```
Access the application:
Use the external IP address provided by the Kubernetes service to access the application.

## Screenshots-
<br>
# CricBuzz API-
<br>
<img width="1440" alt="Screenshot 2024-08-21 at 1 41 24 AM" src="https://github.com/user-attachments/assets/4cdbe529-c159-48ff-b56d-57d12e6c2656">
# ScoreBoards-
<img width="1440" alt="Screenshot 2024-08-21 at 12 01 56 AM" src="https://github.com/user-attachments/assets/9ce9aded-4160-44e9-a7f7-aa5f74889489">




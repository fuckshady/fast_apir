# FAST_APIR - User and Alert Management

This project was developed for the third term of the Software Engineering course.  
It is an API designed to manage users and their associated alerts, built with FastAPI, Redis, Docker, Traefik, and GitHub Actions for CI/CD deployment.

## 🚀 Technologies Used

- Python 3.12
- FastAPI
- Redis (Database)
- Docker & Docker Compose
- Traefik (Load Balancer and Reverse Proxy)
- GitHub Actions (Continuous Integration and Deployment)

## 🛠️ Project Structure

--------------------------------------------
FAST_APIR/
├── .github/
│   └── workflows/
│       └── deploy.yml
├── .venv/                # (virtual environment, ignored in .gitignore)
├── app/
│   ├── db/
│   │   └── redis_conn.py
│   ├── models/
│   │   ├── Alert.py
│   │   ├── User.py
│   │   └── dtos/
│   │       ├── AlertDTOs.py
│   │       └── UserDTOs.py
│   └── main.py
├── docker/
│   ├── docker-compose.yml
│   ├── traefik.yml
│   └── traefik_dynamic.yml
├── .env                  # Environment variables (ignored in .gitignore)
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
-----------------------------------------------

## 👽 Step by Step to Install this project (LINUX) 

- git clone https://github.com/fuckshady/fast_apir.git
- cd fast_apir
- python3 -m venv .venv
- source .venv/bin/activate
- pip install fastapi uvicorn redis
- pip install python-dotenv

Only if you have error to interpreter
- Control + Shift + P -> Python:Select Interpreter ('venv') and solve this problem 

and create with touch .env, and create internal variables

Good bye and good luck.



# GitHub-Actions-CI-CD-Pipeline

A simple Todo SaaS application built with Flask, demonstrating CI/CD pipelines using GitHub Actions.

## Features

- REST API for managing todos
- Automated CI/CD with GitHub Actions
- Docker containerization

## API Endpoints

- `GET /` - Home
- `GET /todos` - Get all todos
- `POST /todos` - Add a new todo (JSON: {"task": "description"})

## Setup

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python app.py`

## CI/CD

- CI: Runs on push/PR to main/dev - linting and tests
- CD: Runs on release - builds and pushes Docker image to DockerHub

## Secrets Required for CD

Add to GitHub Secrets:
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN`
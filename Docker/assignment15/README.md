# Dockerized Python Version Application

## Objective

Create a Dockerized Python application using the python:3.12-slim image.

The application displays:

- Current Python version
- Current date and time

---

## Project Structure

assignment4/

├── app.py

├── Dockerfile

├── requirements.txt

├── README.md

└── screenshot.png

---

## Build Docker Image

```bash
docker build -t python-version-app .
```

## Run Docker Container

```bash
docker run python-version-app
```

## Sample Output

```text
===== Docker Python Application =====

Python Version: 3.12.x

Current Date and Time: 2026-06-24 22:35:42
```

## Screenshot

See screenshot.png
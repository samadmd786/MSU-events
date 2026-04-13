# MSU Events

A **Flask** web application for managing and displaying MSU events, fully containerized with Docker and Docker Compose for consistent local and production deployments.

## Features

| Feature | Description |
|---------|-------------|
| **Flask Backend** | Modular application factory pattern (`flask_app/create_app`) |
| **Docker Ready** | Separate `Dockerfile` and `Dockerfile-dev` for prod and dev environments |
| **Docker Compose** | One-command local startup with `docker-compose up` |
| **Configurable Port** | Port set via `PORT` environment variable (default: 8080) |

## Getting Started

### Prerequisites

- [Docker](https://www.docker.com/) and [Docker Compose](https://docs.docker.com/compose/)
- *Or* Python 3.x for running without Docker

### Running with Docker *(Recommended)*

```bash
# Clone the repo
git clone https://github.com/samadmd786/MSU-events.git
cd MSU-events

# Build and start
docker-compose up --build
```

Navigate to **http://localhost:8080** in your browser.

To stop: press `Ctrl+C` or run `docker-compose down`.

### Running Locally *(without Docker)*

```bash
pip install -r requirements.txt
python app.py
```

### Dev Mode *(with hot-reloading)*

```bash
docker build -f Dockerfile-dev -t msu-events-dev .
docker run -p 8080:8080 msu-events-dev
```

## Project Structure

| Path | Description |
|------|-------------|
| `app.py` | Application entry point |
| `flask_app/` | Flask app factory and route blueprints |
| `Dockerfile` | Production container image |
| `Dockerfile-dev` | Development container with live reload |
| `docker-compose.yml` | Multi-container orchestration config |
| `requirements.txt` | Python dependencies |

## Tech Stack

- **Language:** Python 3.x
- **Framework:** [Flask](https://flask.palletsprojects.com/)
- **Containerization:** Docker, Docker Compose
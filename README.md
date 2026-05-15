# Cloud DevOps Engineering Midterm

This project is a small multi-container Flask and Redis application built for a Cloud DevOps Engineering midterm. It contains two Flask services that share a Redis database:

- `app1`: a message collector that accepts messages and stores them in Redis.
- `app2`: a dashboard that displays the total number of messages and visits.

## Collaborators

| Collaborator | Responsibility |
| --- | --- |
| student1 | `app1` - Message Collector |
| stident2 | `app2` - Dashboard |

## Project Structure

```text
.
├── app1/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
├── app2/
│   ├── app.py
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── static/
│   │   └── style.css
│   └── templates/
│       └── dashboard.html
├── docker-compose.yaml
└── README.md
```

## Services

### App 1: Message Collector

`app1` runs on port `8000`. It provides a simple form where users can submit messages.

When a user visits or submits the form:

- The visit counter is incremented in Redis.
- Submitted messages are stored in a Redis list named `messages`.

URL:

```text
http://localhost:8000
```

### App 2: Dashboard

`app2` runs on port `8001`. It reads data from Redis and displays:

- Total messages submitted.
- Total visits to the message collector.

URL:

```text
http://localhost:8001
```

### Redis

Redis is used as the shared data store for both Flask applications. The Redis container uses a named Docker volume, `redis_data`, so data can persist across container restarts.

## Requirements

To run this project, you need:

- Docker
- Docker Compose

## How to Run

From the project root, start all services with:

```bash
docker compose up --build
```

After the containers start:

1. Open the message collector at `http://localhost:8000`.
2. Submit one or more messages.
3. Open the dashboard at `http://localhost:8001` to view the message and visit counts.

## How to Stop

Stop the running containers with:

```bash
docker compose down
```

To stop the containers and remove the Redis volume data:

```bash
docker compose down -v
```

## Application Ports

| Service | Container Name | Port |
| --- | --- | --- |
| Redis | `redis_server` | `6379` |
| App 1 | `message_collector` | `8000` |
| App 2 | `dashboard_app` | `8001` |

## Technologies Used

- Python 3.11
- Flask
- Redis
- Docker
- Docker Compose

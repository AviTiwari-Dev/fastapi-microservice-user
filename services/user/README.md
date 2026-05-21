# User Microservice

This microservice provides CRUD operations for user entities with a FastAPI-based REST API.

## Overview

- Microservice implementation using FastAPI and asynchronous SQLAlchemy
- FastAPI application: `services/user/src/main.py`
- Dockerfile: `services/user/Dockerfile`
- PostgreSQL async database using SQLAlchemy + `asyncpg`
- Git and GitHub workflows for CI/CD
- WIF/OIDC-based GCP authentication for secure deployment
- Custom documentation endpoints:
  - `/documentation/Swagger`
  - `/documentation/ReDoc`
  - `/documentation/openapi.json`

## CI/CD and GCP Deployment

- GitHub workflow: `.github/workflows/deploy-user.yml`
- Uses `google-github-actions/auth@v2` and workload identity provider for GCP auth
- Pushes Docker image to Google Artifact Registry repository `user-repo`
- Deploys service to Cloud Run as `user-service`
- Configures Cloud Run access to Cloud SQL instance `user-instance`
- GCP setup scripts:
  - `services/user/scripts/gcp_setup_using_wif.sh`
  - `services/user/scripts/gcp_setup_using_keys.sh`

## Environment Configuration

Create a `.env` file in `services/user/` with:

```env
DEBUG=true
URL=postgresql+asyncpg://username:password@hostname:5432/database
ECHO=false
POOL_SIZE=5
MAX_OVERFLOW=10
POOL_TIMEOUT=30
POOL_RECYCLE=1800
FUTURE=true
```

## Run Locally

```bash
cd services/user
uvicorn src.main:user_api --host 0.0.0.0 --port 8080
```

## Docker

Build:

```bash
docker build -t project024-user .
```

Run:

```bash
docker run --env-file .env -p 8080:8080 project024-user
```

## API Endpoints

- `POST /user/` — Create user
- `GET /user/?user_id={UUID}` — Read user
- `PATCH /user/?user_id={UUID}` — Update user
- `DELETE /user/?user_id={UUID}` — Delete user

## API Documentation

- Swagger UI: `http://localhost:8080/documentation/Swagger`
- ReDoc: `http://localhost:8080/documentation/ReDoc`
- OpenAPI JSON: `http://localhost:8080/documentation/openapi.json`

## Images and Architecture Docs

The following image files are stored in `services/user/docs/`:


- `swagger_ui.png`
![Swagger UI](docs/swagger_ui.png)

- `gcp_cloud_run_container.png`
![GCP Cloud Run Container](docs/gcp_cloud_run_container.png)

- `gcp_cloud_sql_postgresql.png`
![GCP Cloud SQL PostgreSQL](docs/gcp_cloud_sql_postgresql.png)

- `gcp_cloud_artifact_repository.png`
![GCP Artifact Repository](docs/gcp_cloud_artifact_repository.png)

- `gcp_cloud_artifact_image.png`
![GCP Artifact Image](docs/gcp_cloud_artifact_image.png)

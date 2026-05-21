# FastAPI User Microservice

A lightweight user management microservice built with FastAPI, async SQLAlchemy, and PostgreSQL. The service is containerized with Docker and designed for cloud deployment, with GCP architecture, images included in the microservice docs folder.

## Project Structure

- `services/user/` — User microservice implementation.
- `services/user/src/` — FastAPI app, routers, data models, DB configuration, and operations.
- `services/user/docs/` — Architecture and deployment images used by the README.


## Highlights

- Microservice architecture with isolated user service implementation
- FastAPI REST API for user CRUD operations
- Async SQLAlchemy + `asyncpg` PostgreSQL backend
- Dockerized service for local development and cloud deployment
- Git and GitHub-based version control with GitHub Actions CI/CD
- Workload Identity Federation (WIF) / OIDC authentication for GCP deployments
- Google Cloud Run deployment with Cloud SQL integration
- Google Artifact Registry for Docker image storage
- Swagger and ReDoc documentation exposed at custom endpoints

## CI/CD and Cloud Integration

- GitHub Actions workflow: `.github/workflows/deploy-user.yml`
- Uses `google-github-actions/auth@v2` with a workload identity provider for OIDC-based GCP auth
- Builds and pushes Docker images to Artifact Registry in `asia-south1`
- Deploys the service to Cloud Run as `user-service`
- Connects Cloud Run to Cloud SQL instance `user-instance`
- Includes GCP setup scripts in `services/user/scripts/`:
  - `gcp_setup_using_wif.sh`
  - `gcp_setup_using_keys.sh`

## Quick Start

### 1. Prepare environment variables

Create a `.env` file in `services/user/` with values for:

- `DEBUG`
- `URL` (e.g. `postgresql+asyncpg://user:password@host:5432/dbname`)
- `ECHO`
- `POOL_SIZE`
- `MAX_OVERFLOW`
- `POOL_TIMEOUT`
- `POOL_RECYCLE`
- `FUTURE`

### 2. Run locally

```bash
cd services/user
uvicorn src.main:user_api --host 0.0.0.0 --port 8080
```

### 3. Build and run with Docker

```bash
docker build -t project024-user ./services/user

docker run --env-file services/user/.env -p 8080:8080 project024-user
```

### 4. Access API docs

- Swagger UI: `http://localhost:8080/documentation/Swagger`
- ReDoc: `http://localhost:8080/documentation/ReDoc`
- OpenAPI JSON: `http://localhost:8080/documentation/openapi.json`

## User API Endpoints

All endpoints are under the `/user` prefix.

- `POST /user/` — Create a new user
- `GET /user/` — Retrieve user details
- `PATCH /user/` — Update user details
- `DELETE /user/` — Delete a user

## Service Documentation Images

![Swagger UI](services/user/docs/swagger_ui.png)
- `swagger_ui`

![GCP Cloud Run Container](services/user/docs/gcp_cloud_run_container.png)
- `gcp_cloud_run_container`

![GCP Cloud SQL PostgreSQL](services/user/docs/gcp_cloud_sql_postgresql.png)
- `gcp_cloud_sql_postgresql`

![GCP Artifact Repository](services/user/docs/gcp_cloud_artifact_repository.png)
- `gcp_cloud_artifact_repository`

![GCP Artifact Image](services/user/docs/gcp_cloud_artifact_image.png)
- `gcp_cloud_artifact_image`

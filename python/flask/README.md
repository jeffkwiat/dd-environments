# Python / Flask
This environment deploys a Datadog-ready Python/Flask application.

## Versions
These are the default versions

The following can be adjusted in the [requirements.txt](services/web/requirements.txt):
- Flask 1.1.2
- Gunicorn 20.0.4
- ddtrace [0.43.0](https://github.com/DataDog/dd-trace-py/releases/tag/v0.43.0)

The following can be adjusted in their respective Dockerfiles:
- Python 3.8 [dev](services/web/Dockerfile.dev) | [prod](services/web/Dockerfile.prod)
- NGINX 1.19.2 [prod](services/nginx/Dockerfile.prod)
- Postgres 13.0 [prod](services/postgresql/Dockerfile)

## Development Environment
### Description
This environment deploys a Python/Flask web application to a Gunicorn application server, behind an NGINX reverse-proxy, with a PostgreSQL database.

### Bring it Up
```
docker-compose -f docker-compose.dev.yaml up --build -d
```
### Bring it Down
To bring down the environment:
```
docker-compose -f docker-compose.dev.yaml down -v
```

## Production Environment
To bring up the environment:
```
docker-compose -f docker-compose.prod.yaml up --build -d
```

To bring down the environment:
```
docker-compose -f docker-compose.prod.yaml down -v
```

## Integrations enabled

- Gunicorn
- NGINX
- PostgreSQL

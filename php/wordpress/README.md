# PHP / Wordpress
This environment deploys a Datadog-ready PHP/Wordpress application.

## Versions
These are the default versions.

The following can be adjusted in their respective Dockerfiles:
- PHP 7.4.12 [prod](services/web/Dockerfile.prod)
- Wordpress 5.5.3 [prod](services/web/Dockerfile.prod)
- Apache 2.4.38 (Debian) [prod](services/web/Dockerfile.prod)
- MySQL 5.7 [prod](services/mysql/Dockerfile)

NOTE: PHP, Wordpress, and Apache2 are all baked into the same Dockerfile

## Production Environment
To bring up the environment:
```
docker-compose up --build -d
```

To bring down the environment:
```
docker-compose down
```

## Integrations Enabled

- Apache
- MySQL
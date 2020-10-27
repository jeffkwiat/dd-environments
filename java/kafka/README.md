# Java / Kafka
This environment deploys a Datadog-ready Java / Kafka application.

## Versions
These are the default versions

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

- Kafka
- Zookeeper
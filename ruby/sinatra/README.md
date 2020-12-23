# Sinatra 2.0 example

A web application built on Sinatra. This version is meant to test
tracing compatibility issues with Sinatra and Redis.

## Compatibility stack

* Ruby 2.7.1
* Sinatra 2.0.8.1

# How To: Datadog APM on Docker on Ruby/Sinatra

### Build the application container
`sudo docker build -t jeffkwiat/app-sinatra:latest .`

### Run the application on the same network as the Datadog Agent
```
sudo docker stop app-sinatra
sudo docker rm app-sinatra
sudo docker run -d -p 8090:8090 \
              --name app-sinatra \
              --network network-apm \
              -e DD_APM_ENABLED=true \
              -e DD_APM_NON_LOCAL_TRAFFIC=true \
              -e DD_AGENT_HOST=datadog-agent \
              -e DD_AGENT_PORT=8126 \
              jeffkwiat/app-sinatra:latest
```

Access the application at http://localhost:8090/.

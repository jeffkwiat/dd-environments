# Datadog APM Environments

This repository includes production-ready examples of various customer environments.

The target audience is two-fold:
- Sales Engineers can quickly spin up an environment, similar to a customer, for either a live demo, or during a POV.

- Customers can quickly see how their environment should appear, once everything is up-and-running.  They can also use these to help troubleshoot.

## Example
Say, a customer has a Python / Flask web application.  It runs on Gunicorn application server, with an NGINX reverse-proxy, and hits a PostgreSQL database.

They want to monitor this in Datadog.

The [Python/Flask environment](./python/) shows them:
- How to collect APM traces
- How to generate APM traffic
- How to enable App Analytics
- How to enable Code Profiling
- How to ingest Logs from all sources
- How to enable Trace/Log Correlation
- How to use Unified Service Tagging
- How to setup the Agent for Infrastructure metrics
- How to setup the Agent for Live Processes
- How to setup the Agent for Network Perofrmance Monitoring
- Sets up an out-of-the-box dashboard

This environment can be deployed as host-based, docker-based, or Kubernetes-based.

## The Goal(s)
- Provide the above example for multiple environments, across all APM-supported languages.
- Provide Terraform scripts to deploy the environment, across multiple Infrastructure stacks
- Provide plug-in-play ability to link multiple environments together with distributed tracing

## How to use it?

- Clone the repository
`git clone https://github.com/jeffkwiat/dd-environments.git`

- Set your DD_API_KEY
`echo DD_API_KEY=<YOUR-DD-API-KEY> .env`

- Start up the agent
`docker-compose -f agent-compose.yaml up -d --build`

- `cd` into the environment directory you wish to spin up

- Follow the instructions in `README.md` for that environment

## What is locustfile.py?
[Locust.io](https://locust.io/) is a utility I use to generate realistic traffic to an endpoint, or many endpoints.

Each environment includes a configuration file that hits multiple endpoints.

See their [documentation](https://docs.locust.io/en/stable/) for how to use.
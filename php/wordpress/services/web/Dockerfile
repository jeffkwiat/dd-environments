FROM wordpress:latest

RUN apt-get update
RUN apt-get install -y wget
RUN wget https://github.com/DataDog/dd-trace-php/releases/download/0.47.0/datadog-php-tracer_0.47.0_amd64.deb && dpkg -i ./datadog-php-tracer_0.47.0_amd64.deb


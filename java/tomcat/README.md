# How to Setup Tomcat, Solr, with Datadog Java APM

## Tomcat
#### APM

- Install the Datadog Agent on your Tomcat application server
```
wget -O dd-java-agent.jar https://dtdg.co/latest-java-tracer
```
- Enable Datadog Java APM for automatic instrumentation of all Java applications running on Tomcat
```
echo "export CATALINA_OPTS='-javaagent:./dd-java-agent.jar -Ddd.trace.debug=true'" >> bin/setenv.sh
```
NOTE: You'll want to change `-Ddd.trace.debug=false` once you see APM working

- Set the following environment variables on your Tomcat server, so the Java tracer can talk to the Datadog Agent
```
DD_AGENT_HOST=datadog-agent
DD_AGENT_PORT=8126
DD_ENV=prod
DD_SERVICE=app-java
DD_VERSION=1.0
DD_LOGS_INJECTION=true
```
- Restart Tomcat 
```
/usr/local/tomcat/bin/startup.sh
```
#### Metrics
- Enable JMX Remote on your Tomcat Application server 

```
JAVA_OPTS=-Xms256m -Xmx6144m -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.port=9012 -Dcom.sun.management.jmxremote.rmi.port=9012 -Djava.rmi.server.hostname=tomcat
```

##### Documentation
- [Tomcat Integration](https://docs.datadoghq.com/integrations/tomcat/)
- [Monitoring JMX](https://docs.oracle.com/en/java/javase/14/management/monitoring-and-management-using-jmx-technology.html#GUID-6F896ED5-D517-4825-869B-BB045AF51A92)

      - JAVA_OPTS= >-
          -Xms256m
          -Xmx6144m
          -Dcom.sun.management.jmxremote
          -Dcom.sun.management.jmxremote.authenticate=false
          -Dcom.sun.management.jmxremote.ssl=true
          -Dcom.sun.management.jmxremote.local.only=false
          -Djava.rmi.server.hostname=tomcat
          -Dcom.sun.management.jmxremote.port=9012
          -Dcom.sun.management.jmxremote.rmi.port=9012
          
## Solr
#### Metrics
#### APM

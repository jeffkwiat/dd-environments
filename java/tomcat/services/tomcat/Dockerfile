FROM tomcat

# Uncomment to install netsat to verify JMX port
# RUN apt-get update \
#    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
#    net-tools \
#    && apt-get clean \
#    && rm -rf /var/lib/apt/lists/*

# Copy Datadog sample app to Tomcat
COPY ./app/target/app-datadog-0.1.0.jar /usr/local/tomcat/webapps/app-datadog-0.1.0.jar
COPY ./tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

RUN wget -O sample.war https://tomcat.apache.org/tomcat-7.0-doc/appdev/sample/sample.war && mv sample.war ./webapps/

RUN wget -O dd-java-agent.jar https://dtdg.co/latest-java-tracer

EXPOSE 8080
# && echo "export CATALINA_OPTS='-Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=9000 -Dcom.sun.management.jmxremote.ssl=false -Dcom.sun.management.jmxremote.authenticate=false -javaagent:./dd-java-agent.jar -Ddd.trace.debug=true'" >> bin/setenv.sh
#FROM openjdk:8-jre
FROM openjdk:8-alpine

#RUN mkdir /usr/src/myapp
#COPY crawlerEventi.jar /usr/src/myapp
#WORKDIR /usr/src/myapp

RUN mkdir app
COPY crawlerEventi.jar /app
WORKDIR /app
ENV JAVA_TOOL_OPTIONS -Dfile.encoding=UTF8

#RUN apt-get update && apt-get -y install cron && apt-get -y install busybox-static
# copy crontabs for root user
COPY cronjobs /etc/crontabs/root

# start crond with log level 8 in foreground, output to stderr
CMD ["crond", "-f", "-d", "8"]
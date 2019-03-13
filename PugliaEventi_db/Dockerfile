FROM postgres:9.1
MAINTAINER Giuseppe Perniola <g.perniola22@gmail.com>

EXPOSE 5432

# Set the locale

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    locale-gen
RUN localedef -i en_US -c -f UTF-8 -A /usr/share/locale/locale.alias en_US.UTF-8
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8 


ENV POSTGRES_PASSWORD postgres
ENV POSTGRES_DB PugliaEventi
ADD dump/pugliaeventi.sql /docker-entrypoint-initdb.d

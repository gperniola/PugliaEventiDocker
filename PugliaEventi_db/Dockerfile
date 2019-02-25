FROM postgres:latest
MAINTAINER Giuseppe Perniola <g.perniola22@gmail.com>

EXPOSE 5432
ENV POSTGRES_PASSWORD postgres
ADD dump/pugliaeventi.sql /docker-entrypoint-initdb.d
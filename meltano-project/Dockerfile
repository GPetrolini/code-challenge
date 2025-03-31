FROM meltano/meltano:latest
WORKDIR /app
COPY . /app
RUN ls -l /app
RUN meltano
CMD ["meltano", "run"]
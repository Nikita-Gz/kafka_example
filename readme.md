# This is an example uf using Kafka for publishing and consuming messages
Producer app publishes random names, consumer app processes names and uses an API to guess their gender

To launch the project, run `docker-compose up -d --build` in root directory. Consumer and producer containers both write to log. It is normal for them to occasionally throw exceptions about broker being unavailable

# This is an example uf using Kafka for publishing and consuming messages
Producer app publishes random names, consumer app processes names and uses an API to guess their gender

To launch the project, run "docker-compose up -d --build" in root directory. Consumer and producer containers both write to log. It is normal for them to occasionally throw exceptions about broker being unavailable

Containers
1. Broker - Kafka broker container
2. Zookeper - required for Kafka
3. Init_broker - initializes Kafka topics
4. Producer - generates random names and publishes them to Kafka
5. Consumer - consumes names, sends them to an API that guesses their gender, prints it out

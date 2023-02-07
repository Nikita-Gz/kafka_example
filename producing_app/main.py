# this program generates random names with some random delay,
# and publishes them to kafka

import time
import random
from faker import Faker
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='broker:29092')

fake = Faker()

while True:
  name = fake.first_name()
  print(f'Publishing name: {name}')
  future = producer.send('my_topic', name.encode('utf-8'))
  result = future.get()
  print(f'Published name: {name}')
  time.sleep(random.randint(1, 5))

# this program recieves a message with a name,
# and uses API to guess name's gender

import json
import requests
import time
import logging
from kafka import KafkaConsumer
from kafka import TopicPartition
consumer = KafkaConsumer(bootstrap_servers='broker:29092', group_id=None)
consumer.subscribe(['my_topic'])

def process_name(name: str) -> str:
  print(f'Processing name: {name}')
  api_url = 'https://api.genderize.io/?name='
  response = requests.get(api_url + name.lower())
  json_response = json.loads(response.text)
  gender = json_response['gender']
  return gender

# main loop, waits for messages and processes them
while True:
  message_dict = consumer.poll() # type: dict

  if not message_dict:
    continue

  # gets values (names) from all partitions
  values = []
  for partition in message_dict.values():
    for message in partition:
      values.append(message.value.decode('utf-8'))

  for name in values:
    try:
      gender = process_name(name)
      print(f"{name}'s gender is probably {gender}")
    except Exception as e:
      print(f'Error: {e}')

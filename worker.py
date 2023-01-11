# Work needed
from aistorytelling import aistorytelling

# Background app running
from rq import Queue, Worker, Connection
import redis
import os

listen = ["default"]
# Redis server from Heroku Add-on
conn = redis.Redis(
  host='redis-15847.c258.us-east-1-4.ec2.cloud.redislabs.com',
  port=15847,
  password = os.environ["redisapikey"])
# # Localhost Redis server using wsl
# conn = redis.Redis(host='localhost', port=6379, db=0)
# listen = ['high','default','low']
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# conn = redis.from_url(redis_url)
# q = Queue(connection=conn)

# Variable 'prompt' passed from webapp (user input on index.html)
# import sys
# prompt = sys.argv[1]
# print(prompt)

# Worker doin' work
if __name__ == '__main__':
    with Connection(conn):
        worker = Worker(listen)
        # worker = Worker(map(Queue, listen))
        worker.work()
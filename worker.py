# Work needed
from aistorytelling import aistorytelling

# Background app running
from rq import Queue, Worker, Connection
import redis
import os

# Redis server from Heroku Add-on
r = redis.Redis(
  host='redis-15847.c258.us-east-1-4.ec2.cloud.redislabs.com',
  port=15847,
  password = os.environ["redisapikey"])
# # Localhost Redis server using wsl
# r = redis.Redis(host='localhost', port=6379, db=0)
# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
# conn = redis.from_url(redis_url)
q = Queue(connection=r)
listen = ['default']

# Variable 'prompt' passed from webapp (user input on index.html)
import sys
prompt = sys.argv[1]
print(prompt)

# Worker doin' work
if __name__ == '__main__':
    with Connection(r):
        worker = Worker(listen)
        worker.work()
        q.enqueue(aistorytelling, prompt)
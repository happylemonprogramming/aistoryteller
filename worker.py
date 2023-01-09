import os
from rq import Worker, Queue, Connection
import redis

# Background app running
from rq import Queue, Worker, Connection
import subprocess
import random
import redis

r = redis.Redis(
  host='redis-15847.c258.us-east-1-4.ec2.cloud.redislabs.com',
  port=15847,
  password='SQr6LnwBbwNWkdZSSfTksNw1BAzZBQgR')
# r = redis.Redis(host='localhost', port=6379, db=0)
q = Queue(connection=r)


listen = ['default']

# redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')

# conn = redis.from_url(redis_url)

if __name__ == '__main__':
    with Connection(r):
        worker = Worker(listen)
        worker.work()
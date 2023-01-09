# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import aistorytelling

# Web Server Library
from flask import Flask, render_template, request, url_for
from forms import CommentForm
import os

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

# Flask convention and key to avoid CSRF attacks
app = Flask(__name__)
# app.config["SECRET_KEY"] = "mysecret"
app.secret_key = os.environ["flasksecret"]

# Route for AI generated tweet and image generation
@app.route('/', methods=["GET", "POST"])
def storyteller():
  # Commenting function
  comments = []
  comment_form = CommentForm(csrf_enabled=False)

  # Select random file from library of videos
  randomfile = random.choice(os.listdir('static/movie'))
  randomurl = url_for('static', filename=f'movie/{randomfile}')

  # Set variable temporarily utnil prompt submitted
  videourl = randomurl

  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data

    # # Won't work because windows/needs ubuntu... MIGHT WORK ON HEROKU
    subprocess.call(['python', 'worker.py'])

    # Background job for creating the story
    job = q.enqueue(aistorytelling, prompt)
    # from delay import delay
    # job = q.enqueue(delay)
    # q_len = len(q)
    # print(q_len)

    # # untested MIGHT WORK ON HEROKU
    # with Connection():
    #   worker = Worker(q)
    #   worker.work()

    # If comment generated then, post video
    comments.append(prompt)
    videourl = url_for('static', filename=f'movie/{prompt[:30]}.mp4')

  # return f"Task {job.id} added to queue at {job.enqueued_at}. {q_len} tasks in queue."
  return render_template('index.html', template_comments=comments, template_form=comment_form,videourl=videourl, randomurl=randomurl)

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) #Change host back to 0.0.0.0, if needed
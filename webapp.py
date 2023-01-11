# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import aistorytelling

# Web Server Library
from flask import Flask, render_template, request, url_for
from forms import CommentForm
import os

# Background app running
import random
from rq import Queue
from worker import conn
q = Queue(connection=conn)


# Flask convention and key to avoid CSRF attacks
app = Flask(__name__)
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

  # Set variable temporarily until prompt submitted
  videourl = randomurl

  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data
    # If comment generated then, post video
    comments.append(prompt)
    videourl = url_for('static', filename=f'movie/{prompt[:30]}.mp4')

    # # Background job for creating the story
    q.enqueue(aistorytelling, prompt)

    # # For testing functionality and avoiding charges
    # from delay import delay
    # job = q.enqueue(delay)

  return render_template('index.html', template_comments=comments, template_form=comment_form,videourl=videourl, randomurl=randomurl)

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) # Change host, if needed
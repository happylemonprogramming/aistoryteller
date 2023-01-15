# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import *
import json

# Web Server Library
from flask import Flask, render_template, request, url_for
from forms import CommentForm
import os

# Flask convention and key to avoid CSRF attacks
app = Flask(__name__)
app.secret_key = os.environ["flasksecret"]

# Route for AI generated tweet and image generation
@app.route('/', methods=["GET", "POST"])
def storyteller():
  # Commenting function
  comments = []
  comment_form = CommentForm(csrf_enabled=False)

  # Placeholder values prior to content submission
  storysections = 'Pending submission'
  imagepathlist = 'Pending submission'
  firstimage = 'Pending submission'
  nextimageslist=[]
  i=0

  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data

    # Create story content
    functionreturn= aistorytelling(prompt)
    storysections = functionreturn[0]
    imagepathlist = functionreturn[2]
    # Might be able to use a worker file for the images so that the first image generates and goes to the user without waiting on the rest

    # Iterate over images in path to create file URL for Javascript to parse
    for file in imagepathlist:
      nextimageslist.append(url_for('static', filename=f'stories/{prompt[:30]}/{i}.png'))
      i=i+1
    firstimage = url_for('static', filename=f'stories/{prompt[:30]}/0.png')

    # If comment generated then, post video
    # comments.append(prompt)
    # For testing functionality and avoiding charges
    # from delay import delay
    # delay()

    # Story webpage
    return render_template('story.html', storysections=storysections, firstimage=firstimage, nextimageslist=nextimageslist)
  # Home landing page
  return render_template('index.html', template_comments=comments, template_form=comment_form)

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) # Change host, if needed
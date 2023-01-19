# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import *
import secrets

# Web Server Library
from flask import Flask, render_template, url_for
from forms import CommentForm
import os

# Flask convention and key to avoid CSRF attacks
app = Flask(__name__)
app.secret_key = os.environ["flasksecret"]

# Route for AI generated story and image generation
@app.route('/', methods=["GET", "POST"])
def storyteller():
  # Commenting function
  comment_form = CommentForm(csrf_enabled=False)

  # Variable initialization (placeholder values prior to content submission)
  storysections = 'Pending submission'
  imagepathlist = 'Pending submission'
  firstimage = 'Pending submission'
  nextimageslist=[]
  newimages = []
  comments = []
  newstory = []
  i=0
  state = 0

  # Unique identifier folder creation for HTTP GET request to store text files
  filepath = f'/app/static/stories' #Change to 'filestorage' and sync with storypath
  print('Confirmed Textpath for File Storage: ', filepath)
  
  # Take in User Input via HTTP POST
  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data
    comments = []
    state = 1
    # Create story content
    functionreturn= aistorytelling(prompt, filepath)
    storysections = functionreturn[0]
    imagepathlist = functionreturn[2]
    # Might be able to use a worker file for the images so that the first image generates and goes to the user without waiting on the rest

    # Iterate over images in path to create file URL for Javascript to parse
    for file in imagepathlist:
      nextimageslist.append(url_for('static', filename=f'stories/{i}.png'))
      i=i+1

    # Create file path for first image reference
    firstimage = url_for('static', filename=f'stories/0.png')
    comments.append(prompt)
    state = 2
    return render_template('main.html', template_form=comment_form, template_comments=comments, state=state, storysections=storysections, imagepathlist=imagepathlist, firstimage=firstimage, nextimageslist=nextimageslist, newimages=newimages, newstory=newstory)

  # Home landing page
  return render_template('main.html', template_comments=comments, template_form=comment_form, state=state, storysections=storysections, nextimageslist=nextimageslist)

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) # Change host, if needed
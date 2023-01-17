# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import *
import secrets

# Web Server Library
from flask import Flask, render_template, url_for
from forms import CommentForm, WhatNext
import os

# Flask convention and key to avoid CSRF attacks
app = Flask(__name__)
app.secret_key = os.environ["flasksecret"]

# Route for AI generated story and image generation
@app.route('/', methods=["GET", "POST"])
def storyteller():
  # Commenting function
  comments = []
  comment_form = CommentForm(csrf_enabled=False)
  what_next = WhatNext(csrf_enabled=False)

  # Variable initialization (placeholder values prior to content submission)
  storysections = 'Pending submission'
  imagepathlist = 'Pending submission'
  firstimage = 'Pending submission'
  nextimageslist=[]
  newimages = []
  newstory = []
  i=0
  # Unique identifier folder creation for HTTP GET request to store text files
  textfilepath = f'/app/static/stories/{secrets.token_hex(16)}'
  os.makedirs(textfilepath)
  print('Created Textpath for File Storage: ', textfilepath)
  # Take in User Input via HTTP POST
  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data

    # Create story content
    functionreturn= aistorytelling(prompt, textfilepath)
    storysections = functionreturn[0]
    imagepathlist = functionreturn[2]
    # Might be able to use a worker file for the images so that the first image generates and goes to the user without waiting on the rest

    # Iterate over images in path to create file URL for Javascript to parse
    for file in imagepathlist:
      # nextimageslist.append(url_for('static', filename=f'stories/{prompt[:30]}/{i}.png'))
      nextimageslist.append(url_for('static', filename=f'{textfilepath}/{i}.png'))
      i=i+1
    # firstimage = url_for('static', filename=f'stories/{prompt[:30]}/0.png')
    firstimage = url_for('static', filename=f'{textfilepath}/0.png')
    return render_template('story.html', template_form=what_next, storysections=storysections, imagepathlist=imagepathlist, firstimage=firstimage, nextimageslist=nextimageslist, newimages=newimages, newstory=newstory)
    
  # MIGHT RUN INTO AN ERROR HERE ON HEROKU NEED TO MONITOR
  # Make it scary
  # Make it funny
  # Make it epic
  if what_next.validate_on_submit():
    # Store tonality input
    tone = what_next.radio.data
    # Pull story text data and store to variable
    # storypath = f'/app/static/stories/{prompt[:30]}' #issue with referencing path when path is defined earlier, need a different unique foldername (maybe random)
    with open(f'{textfilepath}/storytext.txt', "r") as storytext:
      storytext = storytext.read()
    # Pull prompt text data and store to variable
    with open(f'{textfilepath}/prompt.txt', "r") as prompttext:
      prompt = prompttext.read()
    # List storytext into sections
    storysections = storytext.split('\n\n')
    storysections.pop(0)
    # Limit next section to 3 scenes
    if len(storysections) < 6:
      max = len(storysections)
    else:
      max = 6
    restofstory = storysections[3:max]
    # Create new story path based on user input
    from whathappensnext import whathappensnext
    upnext = whathappensnext(prompt,restofstory, tone)
    newstory = upnext[0]
    firststory = newstory[0]
    newimages = upnext[2]
    
    # Variable initialization
    nextimageslist = []
    i = 3
    # Add image links to nextimageslist variable above
    for file in newimages:
      # nextimageslist.append(url_for('static', filename=f'stories/{prompt[:30]}/{i}.png'))
      nextimageslist.append(url_for('static', filename=f'{textfilepath}/{i}.png'))
      i=i+1
    # Link to first image
    # firstimage = url_for('static', filename=f'stories/{prompt[:30]}/3.png')
    firstimage = url_for('static', filename=f'{textfilepath}/0.png')

    return render_template('newstory.html', storysections=storysections, firstimage=firstimage, newimages=newimages, newstory=newstory, firststory=firststory, nextimageslist=nextimageslist)

  # Home landing page
  return render_template('index.html', template_comments=comments, template_form=comment_form, storysections=storysections, nextimageslist=nextimageslist)


# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) # Change host, if needed
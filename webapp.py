# AI powered webapp that creates storybook videos
# Other Python files and functions
from aistorytelling import aistorytelling

# Web Server Library
from flask import Flask, render_template
from forms import CommentForm
import os

app = Flask(__name__)
# app.config["SECRET_KEY"] = "mysecret"
app.secret_key = os.environ["flasksecret"]

# Route for AI generated tweet and image generation
@app.route('/', methods=["GET", "POST"])
def storyteller():
  #Commenting function
  comments = []
  comment_form = CommentForm(csrf_enabled=False)

  if comment_form.validate_on_submit():
    # Add text memo to notification screen of Strike invoice
    prompt = comment_form.comment.data
    # Create story
    aistorytelling(prompt)
    # If comment generated then, post video
    comments.append(prompt)
  return render_template('index.html', template_comments=comments, template_form=comment_form)

# Run app on server (must be at end of code)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5500, debug=True, threaded=True) #Change host back to 0.0.0.0, if needed
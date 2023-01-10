# aistoryteller
AI-powered webapp that creates short stories for kids

webapp.py is the Flask app that calls index.html and passes the user input from HTTP POST to worker.py through the use of forms.py
worker.py queues aistorystelling
aistorytelling.py is the workhorse that:
  -creates working directories for temporary file storage
  -calls Open API GPT3 text completion to create the story (storygenerator.py)
  -slices the story into sections
  -for each section Open API DALL-E creates an image for the story (texttoimage.py)
  -saves the image to a directory folder (saveimagetodir.py)
  -takes the text completion section and converts it to speech (texttospeech.py)
  -takes the GPT3 text and adds it to each DALL-E image (imposetextonimage.py)
  -converts image to video with repeating frames (audioonimage.py)
  -adds speech audio file to new video file (audioimage.py)
  -combines all video scenes for each story section into a single larger video about 1-minute in length (combinevideos.py)
  -then deletes all files that aren't the main story video (filecleanup.py)
  
Procfile is to define webapp and worker for Heroku
requirements.txt is pip freeze of the virtual environment
delay.py is solely for testing purposes


from gtts import gTTS

# Using Google Text To Speech library a function is created to turn text to MP3
def texttospeech(text,path,name):
    # Create a gTTS object
    tts = gTTS(text)
    # Save the audio to an MP3 file
    tts.save(str(path)+str(name)+'.mp3')
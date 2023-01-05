# Receive user input (e.g. 'bears doing karate')
import os

# Total Webapp logic path
def aistorytelling(prompt):
    # Confirm that directories have been set up, if not then create them
    # Check if the directory exists
    if not os.path.exists('images'):
        # Create the directory
        os.makedirs('images')
    if not os.path.exists('story talk'):
        os.makedirs('story talk')
    if not os.path.exists('story images'):
        os.makedirs('story images')
    if not os.path.exists('videos'):
        os.makedirs('videos')
    if not os.path.exists('scenes'):
        os.makedirs('scenes')
    if not os.path.exists('static/movie'):
        os.makedirs('static/movie')

    # Set file paths relative to current directory
    current_dir = os.getcwd()
    imagepath = os.path.join(current_dir, 'images/')
    mp3path = os.path.join(current_dir, 'story talk/')
    textimagespath = os.path.join(current_dir, 'story images/')
    vidpath = os.path.join(current_dir, 'videos/')
    scenepath = os.path.join(current_dir, 'scenes/')
    storyvideopath = os.path.join(current_dir, 'static/movie/')

    # Feed to chat to create story
    from storygenerator import textgenerator
    story = textgenerator('Write a short childrens story about '+prompt,)

    # Trim story sections to give to image generator
    storysections = story[0].split('\n\n')
    storysections.pop(0)
    i=0

    # Create a clip for each section of the story
    for sections in storysections:
        keywords = textgenerator('List the key words in order separated by commas in the following text: '+sections)[0]

        # Create story images
        from texttoimage import text_to_image
        imageinput = "Cartoon storybook painting about: " + str(prompt) + ', ' + str(keywords[2:])
        storyimagelink = text_to_image(imageinput)[0]
        print(storyimagelink)
        # # Alternative image generator
        # storyimagelink = text_to_image('LEARN THIS CONTEXT:' +str(prompt)+', THEN CREATE AN CHILDRENS BOOK IMAGE ABOUT THIS SECTION OF THE STORY: ' + str(sections))[0]

        # Save story image to path
        from saveimagetodir import saveimagetodir
        saveimagetodir(storyimagelink,imagepath,i)

        # Create mp3 of story section
        from texttospeech import texttospeech
        texttospeech(sections,mp3path,i)

        # Take story trim and impose it on to each respective image
        from imposetextonimage import imposetextonimage
        storyimage=str(imagepath)+str(i)+'.png'
        imposetextonimage(sections,storyimage,textimagespath,i)

        # Make video from image
        from audioonimage import imagetovideo,audioonvideo
        imagetovideo(str(textimagespath)+str(i)+'.png',vidpath,i)

        # Add audio to new video
        audio = str(mp3path)+str(i)+'.mp3'
        input_video = str(vidpath)+str(i)+'.mov'
        audioonvideo(audio,input_video,scenepath,i)

        # Stop the app early so we don't go broke
        i+=1
        print('Sucessfully Completed Scenes: '+str(i))
        # if i == 1:
        #     break

    # Stitch it all together into a single file
    from combinevideos import combinevideos
    combinevideos(scenepath,storyvideopath)

    # Delete all files that are not the movie to save space
    from filecleanup import delete_files
    delete_files(imagepath)
    delete_files(mp3path)
    delete_files(textimagespath)
    delete_files(vidpath)
    delete_files(scenepath)
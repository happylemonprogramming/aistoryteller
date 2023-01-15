# Receive user input (e.g. 'bears doing karate')
import os

# Total Webapp logic path
def aistorytelling(prompt):
    # Confirm that directories have been set up, if not then create them
    # Set file paths relative to current directory
    workingdir = os.getcwd()
    # Not sure this is necessary for Heroku
    # os.chdir(r'C:\Users\clayt\Documents\Programming\aistoryteller')
    # Keep for Heroku
    print(workingdir)

    # Check if the sub-directory exists
    if not os.path.exists('static'):
        # Create the directory
        os.makedirs('static')

    # Change directory and define path
    os.chdir('static')
    # Check if the sub-directory exists
    if not os.path.exists('stories'):
        # Create the directory
        os.makedirs('stories')

    # Change directory and define path
    os.chdir('stories')
    storypath = os.path.join(os.getcwd(), f'{prompt[:30]}/')
    
    if not os.path.exists(storypath):
        # Create the directory and change directory
        os.makedirs(storypath)
        os.chdir(storypath)

        # Feed to chat to create story
        from storygenerator import textgenerator
        story = textgenerator('Write a short childrens story about '+prompt,)
        with open('storytext.txt', "w") as storytext:
            storytext.write(story[0])
        print("Text Created")

        # Trim story sections to give to image generator
        storysections = story[0].split('\n\n')
        storysections.pop(0)
        i=0
        imagepathlist = []
        print("Sections Divided",storysections)

        # Create image for each section of the story
        for sections in storysections:
            # Gotta be a more efficient way to do this (I'm calling the API to make a key words list, which costs more money)
            keywords = textgenerator('List the key words in order separated by commas in the following text: '+sections)[0]

            # Create story images
            from texttoimage import text_to_image
            # Gotta be another input that won't leave that weird text, maybe user can select style (radio buttons?)
            imageinput = "Cartoon storybook painting about: " + str(prompt) + ', ' + str(keywords[2:])
            storyimagelink = text_to_image(imageinput)[0]
            print("Image Created")
            # # Alternative image generator
            # storyimagelink = text_to_image('LEARN THIS CONTEXT:' +str(prompt)+', THEN CREATE AN CHILDRENS BOOK IMAGE ABOUT THIS SECTION OF THE STORY: ' + str(sections))[0]

            # Save story image to path
            from saveimagetodir import saveimagetodir
            location = saveimagetodir(storyimagelink,storypath,i)[1]
            imagepathlist.append(location)
            print('File Saved Here: '+str(location))

            # Stop the app early so we don't go broke
            i+=1
            print('Sucessfully Completed Scenes: '+str(i))
            # if i == 1:
            #     break

    else:
        # Change to the appropriate directory
        os.chdir(storypath)

        # Read the text file
        textpath = f'{storypath}/storytext.txt'
        with open(textpath, "r") as storybody:
            body=storybody.read()

        # Trim existing story sections
        storysections = body.split('\n\n')
        storysections.pop(0)
        i=0
        imagepathlist = []

        for stories in storysections:
            imagepathlist.append(f"{storypath}\{i}.png")
            i=i+1

    return storysections, storypath, imagepathlist
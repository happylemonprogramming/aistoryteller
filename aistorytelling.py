# Receive user input (e.g. 'bears doing karate')
import os

# Total Webapp logic path
def aistorytelling(prompt):
    # Confirm that directories have been set up, if not then create them
    storypath = f'/app/static/stories/{prompt[:30]}'
    # Host path creation
    if os.path.exists(storypath):
        print('Story Path Exists')
        print(os.getcwd())
    else:
        os.makedirs(storypath)
    os.chdir(storypath)
    

    # Store prompt for reference later [NEED TO CONFIRM THIS IS REFERENCED]
    with open('prompt.txt', "w") as prompttext:
        prompttext.write(prompt)
    print("Prompt Text Created")
    # Feed to chat to create story
    from storygenerator import textgenerator
    story = textgenerator('Write a short childrens story about '+prompt,)
    with open('storytext.txt', "w") as storytext:
        storytext.write(story[0])
    print("Story Text Created")

    # Trim story sections to give to image generator
    storysections = story[0].split('\n\n')
    storysections.pop(0)
    i=0
    imagepathlist = []
    print("Sections Divided",storysections)

    # Create image for each section of the story
    for sections in storysections:
        # Create story images
        from texttoimage import text_to_image
        imageinput = "Given this context: " + str(prompt) + ', create a cartoon book image about this story' + str(sections)
        storyimagelink = text_to_image(imageinput)[0]
        print("Image Created")

        # Save story image to path
        from saveimagetodir import saveimagetodir
        location = saveimagetodir(storyimagelink,storypath,i)[1]
        imagepathlist.append(location)
        print('File Saved Here: '+str(location))

        # Limit to 3 scenes/panels so that we don't trigger HTTP Timeout
        i+=1
        print('Sucessfully Completed Scenes: '+str(i))
        if i == 3:
            break

    # [CONSIDER REMOVING] This ELSE statement is for existing content stored on the server for immediate loading (No new AI interaction)
    # else:
    #     # Change to the appropriate directory
    #     os.chdir(storypath)

    #     # Read the text file
    #     textpath = f'{storypath}/storytext.txt'
    #     with open(textpath, "r") as storybody:
    #         body=storybody.read()

    #     # Trim existing story sections
    #     storysections = body.split('\n\n')
    #     storysections.pop(0)
    #     i=0
    #     imagepathlist = []

    #     for stories in storysections:
    #         imagepathlist.append(f"{storypath}\{i}.png")
    #         i=i+1

    return storysections, storypath, imagepathlist
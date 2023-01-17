# Receive user input (e.g. 'bears doing karate')
import os

# Total Webapp logic path
def aistorytelling(prompt, textfilepath):
    # Confirm that directories have been set up, if not then create them
    # storypath = f'/app/static/stories/{prompt[:30]}'
    storypath = textfilepath
    # Host path change
    os.chdir(storypath)
    
    # Store prompt for reference later [NEED TO CONFIRM THIS IS REFERENCED]
    with open(f'{textfilepath}/prompttext.txt', "w") as prompttext:
        prompttext.write(prompt)
    print("Prompt Text Created")
    # Feed to chat to create story
    from storygenerator import textgenerator
    story = textgenerator('Write a short childrens story about '+prompt,)
    with open(f'{textfilepath}/storytext.txt', "w") as storytext:
        storytext.write(story[0])
    print("Story Text Created by AI")

    # Trim story sections to give to image generator
    storysections = story[0].split('\n\n')
    storysections.pop(0)
    i=0
    imagepathlist = []
    print("Sections Divided")

    # Create image for each section of the story
    for section in storysections:
        # Create story images
        from texttoimage import text_to_image
        imageinput = f"Given this context: {prompt}. Create a storybook image about the following story: {section}"
        storyimagelink = text_to_image(imageinput)[0]
        print("Image Created by AI")

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

    return storysections, storypath, imagepathlist
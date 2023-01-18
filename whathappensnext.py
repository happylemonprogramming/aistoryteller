# Receive user input (e.g. 'bears doing karate')
import os

# Total Webapp logic path
def whathappensnext(prompt,restofstory, tone):
    # Confirm that directories have been set up, if not then create them
    # storypath = f'/app/static/stories/{prompt[:30]}'
    storypath = f'/app/static/stories/testfolder'
    # Host path creation
    if os.path.exists(storypath):
        print('Story Path Exists')
        print(os.getcwd())
    else:
        os.makedirs(storypath)
    os.chdir(storypath)

    # if not os.path.exists(nextimagepath):
    # Feed to chat to create story
    from storygenerator import textgenerator
    # Make it scary
    # result = ' '.join(restofstory)
    story = textgenerator(f'Given this context: {prompt}. Change this story to make it {tone}: {restofstory}')[0]
    with open(f'{tone}text.txt', "w") as storytext:
        storytext.write(story)
    print("Next Story Text Created")


    # Remove /n/n spacing
    story = story[2:].replace("/n/n", " ")
    # Alternative split method that takes every two sentences that ends in .!?
    import re
    sentences = re.split(r'(?<=[.!?])\s+', story)
    storysections = [sentences[n] + sentences[n+1] for n in range(0, len(sentences)-1, 2)]

    # Trim story sections to give to image generator
    storysections = story[0].split('/n/n')
    storysections.pop(0) # Is this needed?

    i=3 # First 3 were already made
    imagepathlist = []

    print("Sections Divided: ", len(storysections))

    # Create image for each section of the story
    for sections in storysections:
        # Create story images
        from texttoimage import text_to_image
        # AI INTERFACE!
        imageinput = f"Given this context: {prompt}. Create a {tone} image about this story: {sections}"
        storyimagelink = text_to_image(imageinput)[0]
        print("Image Created")

        # Save story image to path
        from saveimagetodir import saveimagetodir
        location = saveimagetodir(storyimagelink,storypath,i)[1]
        imagepathlist.append(location)
        print('File Saved Here: '+str(location))

        # Limit to 3 scenes/panels to avoid HTTP Timeout
        i+=1
        print('Sucessfully Completed Scenes: '+str(i))
        if i == 6:
            break

    # [CONSIDER REMOVING] This ELSE statement is for existing content stored on the server for immediate loading (No new AI interaction)
    # else:
    #     # Path for demo purposes to show flow and for existing content
    #     nextimagepath = f'{storypath}/3.png'
    #     with open(f'{tone}text.txt', "r") as storytext:
    #         storytext = storytext.read()
    #     print("Next Story Text Found")

    #     # Remove /n/n spacing
    #     story = storytext[2:].replace("/n/n", " ")
    #     # Alternative split method that takes every two sentences that ends in .!?
    #     import re
    #     sentences = re.split(r'(?<=[.!?])\s+', story)
    #     storysections = [sentences[n] + sentences[n+1] for n in range(0, len(sentences)-1, 2)]
    #     imagepathlist = [f'{storypath}/3.png', f'{storypath}/4.png', f'{storypath}/5.png']

    #     print("Sections Divided: ", len(storysections))

    return storysections, storypath, imagepathlist

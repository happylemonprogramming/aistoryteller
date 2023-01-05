import cv2
from moviepy.editor import VideoFileClip, AudioFileClip

# Function to turn an image .png into a video .mov by repeating frames
def imagetovideo(imagepath,vidpath,name):
    # Read the image file
    image = cv2.imread(imagepath)

    # Check if image was successfully read
    if image is None:
        print("Error: Could not read image")
        exit()

    # Create a VideoWriter object to write the video file
    output = cv2.VideoWriter(
        str(vidpath)+str(name)+'.mov',
        cv2.VideoWriter_fourcc('M','J','P','G'),
        30,
        (image.shape[1], image.shape[0])
        )

    # Write the image to the video file
    output.write(image)

    # Release the VideoWriter object
    output.release()

# Function to add MP3 audio to video
def audioonvideo(mp3path,vidpath,scenepath,name):
    # # Add audio to the video clip made earlier
    # Load the audio clip
    audio_clip = AudioFileClip(mp3path)
    # Load the video clip
    video_clip = VideoFileClip(vidpath)
    # Combine the audio and video clips
    final_clip = video_clip.set_audio(audio_clip)
    # Save the combined video and audio to the output file
    final_clip.write_videofile(str(scenepath)+str(name)+".mp4", codec='libx264')
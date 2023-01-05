from moviepy.editor import *
import os

# Function to combine scenes or clips together into on film or movie
def combinevideos(scenepath,storyvideopath):
    # List of scenes
    sceneslist = [scene for scene in os.listdir(scenepath) if scene.endswith('.mp4')]
    
    # List of video clips to concatenate
    video_clips = []
    for vid in sceneslist:
        video_clips.append(VideoFileClip(str(scenepath)+str(vid)))

    # Concatenate the video clips
    final_clip = concatenate_videoclips(video_clips)
    # Save the final clip
    final_clip.write_videofile(str(storyvideopath)+"movie.mp4")

# Download this video to downloads https://www.learningcontainer.com/bfd_download/sample-mp4-file/
# Have images in your downloads directory.
import moviepy.editor as mp
import os

images = [image for image in os.listdir(os.path.expanduser("~/Downloads")) if image.endswith(".jpg")]

for image in images:
    video = mp.VideoFileClip(os.path.expanduser("~/Downloads/sample-mp4-file.mp4"))

    logo = (mp.ImageClip(os.path.expanduser(f"~/Downloads/{image}"))
              .set_duration(video.duration)
              .resize(height=150) # if you need to resize...
              .set_pos(("center","center")))

    final = mp.CompositeVideoClip([video, logo])
    final.write_videofile(f"test{image}.mp4")

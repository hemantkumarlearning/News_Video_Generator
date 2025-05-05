from moviepy.editor import *
from gtts import gTTS

def create_video(script):
    image_files = ["assets/images/bg.jpg","assets/images/bg.jpg","assets/images/bg.jpg","assets/images/bg.jpg","assets/images/bg.jpg","assets/images/bg.jpg"] 
    clips = []
    
    for i, (line, img) in enumerate(zip(script, image_files)):
        tts = gTTS(text=line)
        audio_path = f"line_audio_{i}.mp3"
        tts.save(audio_path)
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        image = ImageClip(img).set_duration(duration).resize(height=720)
        text = TextClip(line, fontsize=28, color='white', size=image.size, method='caption').set_duration(duration).set_position('bottom')

        scene = CompositeVideoClip([image, text]).set_audio(audio)
        clips.append(scene)

    final = concatenate_videoclips(clips)
    final.write_videofile("synced_video.mp4", fps=24)






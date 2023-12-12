'''
This will be a project to download yt videos and songs
I'm going to be able to seperate between mp4 and mp3 files and download the video to my computer
''' 
from pytube import YouTube
from moviepy.editor import AudioFileClip
import os
import re

def get_video(yt):
    print(f'Downloading {yt.title}....')
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download()
    print('Download completed!')

def clean_filename(filename):
    # Remove invalid characters from the filename
    cleaned_filename = re.sub(r'[\\/*?:"<>|]', '', filename)
    return cleaned_filename

def get_audio(yt):
    print(f'Downloading {yt.title}....')
    audio_stream = yt.streams.filter(only_audio=True).first()
    audio_file_path = audio_stream.download()

    cleaned_title = clean_filename(yt.title)
   
    # converting to mp3 
    clip = AudioFileClip(audio_file_path)
    mp3_file_path = f"{cleaned_title}.mp3"
    clip.write_audiofile(mp3_file_path, codec='mp3')
    os.remove(audio_file_path)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    video_choice = input('Enter yt video link: ')
    
    # YouTube(f'{video_choice}').streams.first().download()
    yt = YouTube(f'{video_choice}')
    stream_choice = 0
    
    stream_choice = int(input('1 for Video, 2 for Audio: '))

    if stream_choice == 1: get_video(yt)
    elif stream_choice == 2: get_audio(yt)
    else: print('choose a valid option')

if __name__ == '__main__':
    main()


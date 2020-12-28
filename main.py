"""
YouTube Downloader in Python
Based on tutorial video by NeuralNine
https://www.youtube.com/watch?v=UM6YDJ2aalU
"""

import pytube
import os

# url = ''
# for stream in pytube.YouTube(url).streams.filter(progressive=True):
#     print(stream)

video_list = []

print("YouTube Downloader\n======================")
audio_or_video = input("[A]udio or [V]ideo: ")
print("Enter URLs (Terminate by 'STOP')")

while True:
    url = input("")
    if url == 'stop' or url == 'STOP':
        break
    video_list.append(url)

for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    if audio_or_video == 'A':
        msg = 'audio'
        stream = v.streams.get_audio_only()

    else:
        msg = 'video'
        stream = v.streams.get_by_itag(22)
        if stream == None:
            print("720p 30fps not available, trying 360p 30fps")
            stream = v.streams.get_by_itag(18)
        else:
            print("720p 30fps available")
    
    print(f"Downloading " + msg + " #" + str(x + 1) + "...")
    output = os.getcwd() +  "/Downloads"
    stream.download(filename=v.title, output_path=output)
    print("Done")

print("======================\nAll downloaded!")
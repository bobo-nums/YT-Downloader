"""
YouTube Downloader in Python
Based on tutorial video by NeuralNine
https://www.youtube.com/watch?v=UM6YDJ2aalU

"""

import pytube
import os

# ----------------- Youtube downloader ----------------- 
video_list = []
itags = [37, 22, 18] # 1080p, 720p, 360p audio/video tracks together

print("======================\nYouTube Downloader\n======================")

# query audio or video
audio_or_video = input("[A]udio or [V]ideo: ").upper()
while audio_or_video != 'A' and audio_or_video != 'V':
    print("Invalid option")
    audio_or_video = input("[A]udio or [V]ideo: ").upper()

# query single video or playlist
video_or_playlist = input("[V]ideo or [P]laylist: ").upper()
while video_or_playlist != 'V' and video_or_playlist != 'P':
    print("Invalid option")
    video_or_playlist = input("[V]ideo or [P]laylist: ").upper()

# download individual video(s)
if video_or_playlist == "V":
    print("Enter URLs (Terminate with 'STOP')")
    while True:
        url = input("")
        if url.lower() == 'stop':
            break
        try:
            v = pytube.YouTube(url)
            print("Title: " + v.title)
            video_list.append(url)
        except:
            print("Not a valid URL, ignoring")

# download entire playlist
else:
    playlist_url = input("Enter playlist URL: ")
    while True:
        playlist = pytube.Playlist(playlist_url)
        try:
            print("Playlist title: " + playlist.title)
            for x, url in enumerate(playlist.video_urls):
                try:
                    v = pytube.YouTube(url)
                    print(str(x) + " | " + url + " | " + v.title)
                    video_list.append(url)
                except:
                    print("Video unavailable (" + url + ")")
            break
        except:
            print("Not a valid playlist URL, try again (is it private?)")
            playlist_url = input("Enter playlist URL: ")

# download, remove non-filename friendly chars, and append proper format
for x, video in enumerate(video_list):
    v = pytube.YouTube(video)
    if audio_or_video == 'A':
        msg = 'audio'
        stream = v.streams.get_audio_only()
    else:
        msg = 'video'
        for itag in itags:
            stream = v.streams.get_by_itag(itag)
            if stream != None:
                break
    title = "".join(x for x in v.title if (x.isalnum() or x in "._- ()"))
    print("Downloading " + msg + " #" + str(x + 1) + " | " + v.title)
    output = os.getcwd() + "\Downloads"
    if audio_or_video == 'A':
        title += ".mp3"
    else:
        title += ".mp4"
    try:
        stream.download(filename=title, output_path=output)
    except:
        print("Unable to download")
    print("Done")

print("======================\nFinished!")

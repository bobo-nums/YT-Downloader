"""
YouTube Downloader in Python
Based on tutorial video by NeuralNine
https://www.youtube.com/watch?v=UM6YDJ2aalU

Make sure ffmpeg is installed
https://www.ffmpeg.org/

Make sure ffmpeg.exe is in script directory
"""

import pytube
import os
import subprocess

# ----------------- Stream testing ----------------- 
# url = ''
# for stream in pytube.YouTube(url).streams.filter(progressive=True):
#     print(stream)

# ----------------- Playlist testing ----------------- 
# p = Playlist("https://www.youtube.com/playlist?list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n")
# print(f'Downloading: {p.title}')
# output = os.getcwd() + "\Downloads"
# for video in p.videos:
#     video.streams.first().download(output_path=output)

# ----------------- Youtube downloader ----------------- 

video_list = []
success = []
fail = []

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
            print(v.title)
            video_list.append(url)
        except:
            print("Not a valid URL, ignoring")
        

# download entire playlist
elif video_or_playlist == "P":
    playlist_url = input("Enter playlist URL: ")
    while True:
        playlist = pytube.Playlist(playlist_url)
        try:
            print("Playlist title: " + playlist.title)
            for url in playlist.video_urls:
                try:
                    v = pytube.YouTube(url)
                except:
                    print("Video unavailable (" + url + ")")
                else:
                    print(url + " | " + v.title)
                    video_list.append(url)
            break
        except:
            print("Not a valid playlist URL, try again (is it private?)")
            playlist_url = input("Enter playlist URL: ")
else:
    print("How did you even get here?") # should never get here
    quit()

# for x, video in enumerate(video_list):
#     v = pytube.YouTube(video)
#     if audio_or_video == 'A':
#         msg = 'audio'
#         stream = v.streams.get_audio_only()

#     else:
#         msg = 'video'
#         stream = v.streams.get_by_itag(22)
#         if stream == None:
#             print("720p 30fps not available, trying 360p 30fps")
#             stream = v.streams.get_by_itag(18)
#         else:
#             print("720p 30fps available")
    
#     # title = input("Enter title: ")
#     title = v.title
#     title = str(x + 1)
#     title += (".mp3")
#     print(f"Downloading " + msg + " #" + str(x + 1) + "...")
#     output = os.getcwd() + "\Downloads"
#     stream.download(filename=title, output_path=output)
#     if audio_or_video == 'A':
#         print(f"Converting " + msg + " #" + str(x + 1) + "...")
#         try:
#             try:
#                 os.remove(os.path.join(output, title + ".mp3")) # removes old mp3 file if exists
#                 print("Removing old mp3 file...")
#             except:
#                 print("No previously existing mp3 file...")
#             finally:
#                 cmd = [r'ffmpeg','-i', os.path.join(output, title + ".mp4"), os.path.join(output, title + ".mp3")]
#                 # subprocess.run(cmd, shell=True)
#                 subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT) # additional args suppresses terminal output
#                 os.remove(os.path.join(output, title + ".mp4")) # removes old mp4 file
#                 success.append(title)
#         except:
#             print(f"Converting " + msg + " #" + str(x + 1) + " failed!")
#             fail.append(title)
#     else:
#         success.append(title)
#     print("Done")

# print("======================\nFinished!")

# print("Successes: ")
# for i in success:
#     print("     " + i)

# print("Failures: ")
# for i in fail:
#     print("     " + i)
# print("======================\n")
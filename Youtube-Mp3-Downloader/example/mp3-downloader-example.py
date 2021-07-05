import pytube
import os

url = 'https://www.youtube.com/watch?v=kxSXz9VaIA8' ## your url 

youtube = pytube.YouTube(url)
video = youtube.streams.filter(only_audio = True).first()
out_file = video.download()

base, ext = os.path.splitext(out_file)
new_file = base + '.mp3'
os.rename(out_file,new_file)

print(youtube.title + "It has been a success")

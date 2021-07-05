import pytube

url = 'https://www.youtube.com/watch?v=4SFhwxzfXNc' ## your url 

youtube = pytube.YouTube(url)
video = youtube.streams.first()
video.download()

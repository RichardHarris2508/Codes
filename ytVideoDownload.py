from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dISNgvVpWlo')
myStream = yt.streams
(myStream.filter(mime_type="video/webm", res="720p")).first().download()
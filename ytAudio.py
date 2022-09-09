from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=zuaLWHiRXkg')
myStream = yt.streams
print(yt.streams)
"""myStream.filter(type='audio', abr='128kbps').last().download()"""
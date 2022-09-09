from pytube import YouTube

yt = YouTube('https://www.youtube.com/watch?v=dISNgvVpWlo')
print(yt.title)
print(yt.views)
print(yt.length)
print(yt.rating)
print(yt.description)
print(yt.video_id)
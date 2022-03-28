from os import link
from pytube.cli import on_progress
from pytube import YouTube
link = str(input("Introducir el enlace por favor: "))
yt = YouTube(link, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
ys.download()

s = 1
for v in ys:
    print(str(s)+". "+str(v))
    s += 1

numero = int(input("Enter the number of the video: "))
videos = ys[numero-1]

videos.download("C:/Users/user/Downloads/")

print(yt.title,"\nvideos bajados")

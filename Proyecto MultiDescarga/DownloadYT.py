from os import link
from pytube.cli import on_progress
from pytube import YouTube
link = str(input("Introducir el enlace por favor: "))
yt = YouTube(link, on_progress_callback=on_progress)
ys = yt.streams.get_highest_resolution()
ys.download()

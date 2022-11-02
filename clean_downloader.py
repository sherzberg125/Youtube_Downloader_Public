from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import pyperclip
import os
from pytube.helpers import safe_filename

# import subprocess
import time

# import AudioConverter
# import sys
from moviepy.editor import *

# import django
import pathlib

# django-admin startproject musicDownloader

root = Tk()
root.title("Youtube Video Downloader")
root.geometry("500x200")

# Copy and Paste Code


class StationaryFunctions:
    def __init__(self, text):
        self.text = text
        self.create_binding_keys()
        # self.binding_functions_config()
        self.join_function_with_main_stream()

    def join_function_with_main_stream(self):
        self.text.storeobj["Copy"] = self.copy
        self.text.storeobj["Paste"] = self.paste
        self.text.storeobj["SelectAll"] = self.select_all
        self.text.storeobj["DeselectAll"] = self.deselect_all
        return

    # def binding_functions_config(self):
    #     self.text.tag_configure("sel", background = "skyblue")
    #     return

    def copy(self, event):
        self.text.event_generate("&lt;&lt;Copy>>")
        return

    def paste(self, event):
        self.text.event_generate("&lt;&lt;Cut>>")
        return

    def create_binding_keys(self):
        for key in ["&lt;Control-a>", "&lt; Control-A>"]:
            self.text.master.bind(key, self.select_all)
        for key in ["&lt;Button-1>", "&lt;Return>"]:
            self.text.master.bind(key, self.deselect_all)

    def select_all(self, event):
        self.text.tag_remove("sel", "1.0", "end")
        return

    def deselect_all(self, event):
        self.text.tag_remove("sel", "1.0", "end")
        return


# Check Box
# yt = YouTube("http://youtube.com/watch?v=dQw4w9WgXcQ") #Rick Roll video as intial

# def check():
#     if checked == True:
#         #do just audio
#         yt = YouTube(entryBox.get())
#         getEntry
#         name = (safe_filename(yt.title) + ".mp3")
#         yt.streams.filter(only_audio = True).first().download(filename= name)
#         print("Downloaded Audio")
#     else:
#         #do whole video
#         yt = YouTube(entryBox.get())
#         getEntry
#         name = (safe_filename(yt.title) + ".mp4")
#         yt.streams.first().download(filename=name)
#         print("Downloaded All")


# Store the entry when you hit button


input1 = StringVar()
# checked = BooleanVar()

#  http://youtube.com/watch?v=dQw4w9WgXcQ
newDirectory = ""


def getDirectory():
    global directory
    directory = filedialog.askdirectory()
    newDirectory = []
    for i in range(len(str(directory))):
        if directory[i] == "\\":
            newDirectory.append("\\")
        else:
            newDirectory.append(directory[i])


"""
def getEntry():
    yt = YouTube(entryBox.get())
    # do just audio
    name = safe_filename(yt.title)
    stream = yt.streams.filter(only_audio = True).first().download(filename= name + ".mp3")
    # stream = yt.streams.first()
    # stream.download(filename=name)
    # time.sleep(1)
    # mp4 = "'%s'.mp4" % name
    # mp3 = "'%s'.mp3" % name
    # ffmpeg = ('ffmpeg -i %s ' % mp4 + mp3)
    # subprocess.call(ffmpeg, shell = True)
    name1 = name + ".mp4"
    # path = "C:\\Users\\Scott\\Desktop\\Youtube_Downloader\\" + str(name1)
    path = str(newDirectory) + str(name1)
    video = VideoFileClip(path)
    name2 = name + ".mp3"
    # path2 = "C:\\Users\\Scott\\Desktop\\Youtube_Downloader\\" + str(name2)
    path2 = str(newDirectory) + str(name2)
    video.audio.write_audiofile(path2)
    time.sleep(1)
    name3 = str(newDirectory) + str(name1)
    pathlib.Path.unlink(name3)
    os.remove(path)

    print("Downloaded Audio")
"""


def getEntry():
    yt_aud = YouTube(entryBox.get())
    # do whole video
    name = safe_filename(yt_aud.title)
    # downloads the highest res version on the video
    yt_aud.streams.filter(only_audio=True).first().download(filename=name + ".mp3")
    # line below just gets the first instance of the video
    # yt.streams.first().download(filename=name + ".mp4")
    print("Downloaded All Audio")


def downloadVideo():
    yt = YouTube(entryBox.get())
    # do whole video
    name = safe_filename(yt.title)
    # downloads the highest res version on the video
    yt.streams.get_highest_resolution().download(filename=name + ".mp4")
    # line below just gets the first instance of the video
    # yt.streams.first().download(filename=name + ".mp4")
    print("Downloaded All Video")


# Clear out box when you click on it
def clear_search(event):
    entryBox.delete(0, END)


# Make box and put text in, then clear it when clicked
entryBox = Entry(width=45)
entryBox.insert(0, "Paste Youtube link in here")
if len(entryBox.get()) == 26:
    entryBox.bind("<Button-1>", clear_search)

# buttonthat gets info
entryButton = Button(text="Click to download the audio", command=getEntry)
entryButtonVideo = Button(text="Click to download the video", command=downloadVideo)
directoryButton = Button(
    text="click to select where the file is downloaded", command=getDirectory
)

for key in ["&lt;Control-C>", "&lt; Control-C>"]:
    pyperclip.copy(entryBox.get())

for key in ["&lt;Control-C>", "&lt; Control-C>"]:
    entryButton.text = pyperclip.paste()

entryBox.storeobj = {}
StationaryFunctions(entryBox)

# checked.set(False)
# checkbutton1 = Checkbutton(root, text = "Check me to just download the video", variable = checked)

# checkbutton1.grid(row = 0,column = 0)
entryBox.grid(row=0, column=1)
entryButton.grid(row=2, column=1)
entryButtonVideo.grid(row=3, column=1)
directoryButton.grid(row=1, column=1)

root.mainloop()

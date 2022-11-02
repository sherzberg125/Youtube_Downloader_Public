from pytube import YouTube
from tkinter import *
from tkinter import filedialog
import pyperclip
from pytube.helpers import safe_filename
from moviepy.editor import *

# Create Tkinter Window
root = Tk()
root.title("Youtube Video Downloader")
root.geometry("500x200")

# Code to Copy and Paste
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


input1 = StringVar()
# Test Link to make sure it works (Rick Rokk)
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


def getEntry():
    yt_aud = YouTube(entryBox.get())
    # do whole video
    name = safe_filename(yt_aud.title)
    # downloads the first audio only version on the video
    yt_aud.streams.filter(only_audio=True).first().download(filename=name + ".mp3")
    print("Downloaded All Audio")


def downloadVideo():
    yt = YouTube(entryBox.get())
    name = safe_filename(yt.title)
    # downloads the highest res version on the video
    yt.streams.get_highest_resolution().download(filename=name + ".mp4")
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

entryBox.grid(row=0, column=1)
entryButton.grid(row=2, column=1)
entryButtonVideo.grid(row=3, column=1)
directoryButton.grid(row=1, column=1)

root.mainloop()

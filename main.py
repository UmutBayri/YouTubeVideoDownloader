from pytube import YouTube
from tkinter import Tk, Button, Label, Entry, mainloop, UNDERLINE, X, BOTTOM, CENTER

class VideoDownloader(Tk):
    def __init__(self):
        super().__init__()

        self.geometry("700x400")
        self.font = ("Times", 15)
        self.font_und = ("Times", 15, UNDERLINE)

        self.create_entry()
        self.create_btn()
        self.create_lbl()

        self.locate()

    def create_entry(self):
        self.entry = Entry(
            self, bd = 1, font = self.font
        )

    def create_lbl(self):
        self.h1 = Label(
            self, text = "Video Downloader for YouTube", font = self.font_und
        )

    def create_btn(self):
        self.btn = Button(
            self, text = "Convert", width = 20, 
            font = self.font, command = self.show_video
        )

    def show_video(self):
        try :
            self.url =YouTube(str(self.entry.get()))
            self.video = self.url.streams.filter(file_extension = "mp4").get_by_itag(22)

            title = self.url.title
            views = self.url.views
            length = self.url.length

            self.stats = f"""\
            Title : {title}
            Views : {views}
            Length : {length / 60}.{(str((length % 60)))[:2]}"""
            
            self.desc = Label(
                self,
                text = self.stats,
                font = self.font
            )
            self.desc.pack(side = BOTTOM, expand = True, anchor = CENTER)
            self.btn.config(text = "Download", command = self.download)

        except:
            pass

    def locate(self):
        self.h1.pack()
        self.entry.pack(fill = X, pady = 10)
        self.btn.pack()

    def download(self):
        try :
            self.video.download()
            self.btn.config(text = "Convert", command = self.show_video)
            self.desc.destroy
     
        except:
            pass

root = VideoDownloader()
root.mainloop()
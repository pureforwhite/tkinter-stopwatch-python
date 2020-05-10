#It is 05:00 am now my status seems bad. But I still completed it.
#Really Thanks for watching
#Subscribe my youtube channel
#Like and share my videos
#Follow me on reddit
#Join my discord server and every question and chat are welcome there.
#buymeacoffee if you want
#Hope you guys have a great day, Bye
from tkinter import *
import time
def Main():
    global root

    root = Tk()
    root.title("stopwatch by PureForWhite")
    width = 600
    height = 200
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    Top = Frame(root, width = 600)
    Top.pack(side=TOP)
    Stopwatch = stopwatch(root)
    Stopwatch.pack(side=TOP)
    Bottom = Frame(root, width = 600)
    Bottom.pack(side=BOTTOM)
    Start = Button(Bottom, text = "start", command = Stopwatch.Start, width = 10, height = 2)
    Start.pack(side=LEFT)
    Stop = Button(Bottom, text = "stop", command = Stopwatch.stop, width = 10, height = 2)
    Stop.pack(side=LEFT)
    Reset = Button(Bottom, text = "reset", command = Stopwatch.Reset, width = 10, height = 2)
    Reset.pack(side=LEFT)
    Exit = Button(Bottom, text = "exit", command = Stopwatch.Exit, width = 10, height = 2)
    Exit.pack(side=LEFT)
    Title = Label(Top, text="stopwatch", font=("arial", 30), fg="White", bg = "black")
    Title.pack(fill = X)
    root.config(bg = "black")
    root.mainloop()


class stopwatch(Frame):
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self.startTime = 0.0
        self.nextTime= 0.0
        self.onRunning = 0
        self.timestr = StringVar()
        self.MakeWidget()
    def MakeWidget(self):
        timeText = Label(self, textvariable = self. timestr, font = ("times new roman", 50), fg = "green", bg = "black")
        self.SetTime(self.nextTime)
        timeText.pack(fill=X, expand=NO, pady = 2, padx = 2)
    def Updater(self):
        self.nextTime = time.time() - self.startTime
        self.SetTime(self.nextTime)
        self.timer = self.after(50, self.Updater)
    def Start(self):
        if not self.onRunning:
            self.startTime = time.time() - self.nextTime
            self.Updater()
            self.onRunning = 1
    def stop(self):
        if self.onRunning:
            self.after_cancel(self.timer)
            self.nextTime = time.time() - self.startTime
            self.SetTime(self.nextTime)
            self.onRunning = 0
    def Exit(self):
        root.destroy()
        exit()
    def Reset(self):
        self.startTime = time.time()
        self.nextTime = 0.0
        self.SetTime(self.nextTime)

    def SetTime(self, nextElap):
        minutes = int(nextElap / 60)
        seconds = int(nextElap - minutes * 60.0)
        miliSeconds = int((nextElap - minutes * 60.0 - seconds) * 100)
        self.timestr.set("%02d:%02d:%02d" % (minutes, seconds , miliSeconds))


if __name__ == '__main__':
    Main()
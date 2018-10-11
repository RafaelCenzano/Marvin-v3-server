from tkinter import *
import time

class StopWatch(Frame):
    """ Implements a stop watch frame widget. """
    def __init__(self, parent=None, **kw):
        Frame.__init__(self, parent, kw)
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.makeWidgets()

    def makeWidgets(self):
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
    def Start(self):
        """ Start the stopwatch, ignore if running. """
        if not self._running:
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1
    
    def Stop(self):
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):
        """ Reset the stopwatch. """
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)

if __name__ == "__main__":
    # create a GUI window
    gui = Tk()
    gui.configure(background="light green")     # set the background colour of GUI window
    gui.title("Marvin Stopwatch") # set the title of GUI window
    gui.geometry("280x200") # set the configuration of GUI window

    sw = StopWatch(gui)
    sw.grid(row=0, column=0, columnspan=2)

    Button(gui, text='Start', height=5, width=15, highlightbackground='light green',command=sw.Start).grid(row=1, column=0)
    Button(gui, text='Stop', height=5, width=15, highlightbackground='light green',command=sw.Stop).grid(row=1, column=1)
    Button(gui, text='Reset', height=5, width=15, highlightbackground='light green',command=sw.Reset).grid(row=2, column=0)
    Button(gui, text='Quit', height=5, width=15, highlightbackground='light green',command=gui.quit).grid(row=2, column=1)

    gui.resizable(width=False, height=False)
    gui.mainloop()
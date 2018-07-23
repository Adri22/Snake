from tkinter import *

class Window:
    tileSize = 10

    def __init__(self, worldSize):
        self.master = Tk()
        self.master.title("Snake")
        self.master.resizable(False, False)
        self.canvas = Canvas(
            self.master,
            width = worldSize * self.tileSize,
            height = worldSize * self.tileSize,
            highlightthickness = 0)
        self.canvas.pack()
        #self.master.update_idletasks()
        
    def open(self):
        self.master.mainloop()

    def close(self):
        self.master.quit()
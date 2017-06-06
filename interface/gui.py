from tkinter import *

sys.path.append('../')

from engine.coordinator import run
from engine.Action import Action


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title("Network Analyzer")
        self.master.minsize(400, 400)
        self.pack()
        self.createWidgets()

    def run_spm(self):
        print(run(action=Action.SPM, start=0, target=3))

    def createWidgets(self):
        # button quit
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit

        self.QUIT.pack({"side": "left"})

        self.run_spm_button = Button(self)
        self.run_spm_button["text"] = "RUM_SPM",
        self.run_spm_button["command"] = self.run_spm

        self.run_spm_button.pack({"side": "left"})


root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()

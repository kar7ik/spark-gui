from tkinter import *
from subprocess import *


def func():
    proc = Popen("sudo /home/kar7ik/Documents/Apps/spark/person.py",
                 stdout=PIPE, shell=True)
    proc = proc.communicate()
    output.insert(END, proc)


Master = Tk()
Check = Button(Master, text="Display output", command=func)
Quit = Button(Master, text="Exit", fg="red", command=Master.quit)
output = Text(Master, width=40, height=8)

Check.pack(padx=20, pady=8)
Quit.pack(padx=20, pady=18)
output.pack()

Master.mainloop()

import os
import tkinter as tk
from tkinter import messagebox
from subprocess import *
from tkinter.constants import END


SPARK_SUBMIT_PATH = 'sh /home/kar7ik/Documents/AppsMediators/spark-gui/spark-submit/spark-submit.sh '

# /home/kar7ik/Documents/Apps/spark/person.py


def submit():
    try:
        job_name = name_var.get()
        job_name = job_name.strip()
        print(job_name)
        if job_name[0] == '/':
            proc = Popen(SPARK_SUBMIT_PATH+job_name, stdout=PIPE, shell=True)
            proc = proc.communicate()
            textbox.insert(END, proc)
        else:
            messagebox.showerror("Error", "Please check the input!")
        name_var.set("")
    except:
        messagebox.showerror("Error", "Please check the input!")


window = tk.Tk()
window.geometry("600x400")
window.title('SPARK SUBMIT GUI')

name_var = tk.StringVar()


label_1 = tk.Label(text="Submit a spark job",
                   fg="green",
                   bg="black",
                   width=20,
                   height=2)
label_1.pack()


label_2 = tk.Label(text="Enter below the absolute path below of the job",

                   width=50,
                   height=1)
label_2.pack(padx=10, pady=10)


entry = tk.Entry(fg="black", bg="white", width=50,
                 highlightthickness=2, font=('calibre', 10, 'normal'),
                 textvariable=name_var)
entry.config(highlightbackground="white", highlightcolor="black")
# entry.insert(0)
entry.pack(padx=10, pady=10)


button = tk.Button(
    text="SUBMIT",
    width=10,
    height=1,
    bg="black",
    fg="white",
    command=submit
).pack(padx=10, pady=10)

textbox = tk.Text(window, fg="green",
                  bg="black",)
textbox.bind("<Key>", lambda e: "break")
textbox.pack()


window.mainloop()

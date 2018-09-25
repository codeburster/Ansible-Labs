#!/usr/bin/python
import subprocess
from Tkinter import *

p = subprocess.Popen(["diff -B ansible.cfg Solution_files/ansible.cfg"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
(output,err) = p.communicate()
p_status = p.wait()
print p_status
window = Tk()
window.title("Verifying Ansible configuration file.")
window.geometry("+270+180")
if err :
    lbl = Label(window,text="Ooops !!\nLooks like you missed something in configuration. \n"+err,font=("Arial Black", 16),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
else :
    if output == "" :
        lbl = Label(window,text="Wonderfull !!\nYou seem to have a good understanding of Anisble configuration.!!\n"+output,font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
        lbl.pack(side="top",padx=10,pady=100)
    else:
        lbl = Label(window,text="Ooops !!\nLooks like you missed something in configuration. \n"+err,font=("Arial Black", 16),bg="yellow",fg="Dark Blue")
        lbl.pack(side="top",padx=10,pady=100)

window.mainloop()

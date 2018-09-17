#!/usr/bin/python
import subprocess
from Tkinter import *

p = subprocess.Popen(["ansible dev -i inventory --list-hosts"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
(output,err) = p.communicate()
print output
print err
p_status = p.wait()
print p_status
window = Tk()
window.title("Verifying Ansible Inventory")
window.geometry("+450+180")
if err :
    lbl = Label(window,text="Ooops !!\nThat didn't work !!",font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
else :
    lbl = Label(window,text="Congratulations !!\nYou did it, You are a freaking Genius !!",font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)

window.mainloop()

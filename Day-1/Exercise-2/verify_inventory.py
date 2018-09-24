#!/usr/bin/python
import subprocess
from Tkinter import *

pdev = subprocess.Popen(["ansible dev -i inventory --list-hosts"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
pweb = subprocess.Popen(["ansible web -i inventory --list-hosts"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
(output_dev,err_dev) = pdev.communicate()
(output_web,err_web) = pweb.communicate()
print output_dev
print err_dev
print output_web
print err_web
p_status_dev = pdev.wait()
p_status_web = pweb.wait()
print p_status_dev
print p_status_web
window = Tk()
window.title("Verifying Ansible Inventory")
window.geometry("+450+180")
if err_dev and err_web :
    lbl = Label(window,text="Ooops !!\nNone of group is correct: \n"+err_dev+"/n"+err_web,font=("Arial Black", 16),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
elif err_dev :
    lbl = Label(window,text="Ooops !!\nDev Group is Incorrect: \n"+err_dev+"\nweb Group is correct.",font=("Arial Black", 16),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
elif err_web :
    lbl = Label(window,text="Ooops !!\nWeb Group is Incorrect: \n"+err_web+"\ndev Group is correct.",font=("Arial Black", 16),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
else :
    lbl = Label(window,text="Congratulations !!\nYou did it, You are a freaking Genius !!\n"+output_dev+"\n"+output_web,font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)

window.mainloop()

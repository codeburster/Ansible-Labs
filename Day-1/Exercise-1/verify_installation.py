#!/usr/bin/python
## get subprocess module 
import subprocess
from Tkinter import *
## call date command ##
p = subprocess.Popen(["ansible --version"], stderr=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

#print p.communicate()
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
## or None, if no data should be sent to the child.
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
#print err
#print output
#print p_status
window = Tk()
window.title("Verifying Ansible Installation")
window.geometry("+450+180")
if p_status != 0 :
    lbl = Label(window,text="Ooops !!\nThat didn't work !!",font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)
else :
    lbl = Label(window,text="Congratulations !!\nYou did it, You are a freaking Genius !!",font=("Arial Black", 20),bg="yellow",fg="Dark Blue")
    lbl.pack(side="top",padx=10,pady=100)

window.mainloop()
#print "Command output : ", output
#print "Command exit status/return code : ", p_status

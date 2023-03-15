from tkinter import *
from MarkAttendance import *
from RegisterFace import *
from RegisterName import *

root=Tk()
root.title("Attendance System")
root.minsize(width=600,height=400)
root.maxsize(width=600,height=400)
root.configure(bg="blue")

def func():
    root.destroy()
def NewUser():
    RegisterFace()
    RegisterName()


b1=Button(root,text="New User Registration",height=3,width=20,bd=2,font=3,command=NewUser)
b1.place(x=65,y=130)
b2=Button(root,text="Mark Attendance",height=3,width=20,font=3,bd=2,command=MarkAttendance)
b2.place(x=350,y=130)
e=Button(root,text="Exit",bg="#db312e",bd=2,height=2,width=10,font=3,command=func)
e.place(x=250,y=300)



root.mainloop()
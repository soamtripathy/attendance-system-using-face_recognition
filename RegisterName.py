import os
from tkinter import *

def RegisterName():
    win=Tk()
    win.title("Register Name")
    win.minsize(width=600,height=400)
    win.maxsize(width=600,height=400)
    win.configure(bg="blue")

    def func():
        update.config(text="Name Submitted Successfully",bg="blue",fg="white",font=3)
        name=t.get(1.0, "end-1c")
        cur=os.getcwd()
        newdir=cur+"\\"+"photos"
        os.chdir(newdir)
        old_name='img.png'
        new_name=f'{name}.png'
        os.rename(old_name,new_name)
        os.chdir("..")
    def func2():
        win.destroy()
    t=Text(win,height=2,bd=2,width=25,font=3)
    t.place(x=250,y=100)    
    l=Label(win,text="Enter Your Name :",font=3,height=2)
    l.place(x=100,y=100)

    update=Label(win,text="",bg='blue')
    update.place(x=180,y=200)

    s=Button(win,text="Submit",font=3,height=2,bd=2,width=10,bg="#2cbd22",command=func)
    s.place(x=175,y=250)
    e=Button(win,text="Exit",font=3,height=2,bd=2,width=10,bg="#d92c29",command=func2)
    e.place(x=300,y=250)

    win.mainloop()

# RegisterName()    
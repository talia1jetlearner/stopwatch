from tkinter import*
import tkinter as tk
import time
import tkinter.messagebox
window= Tk()
hour= StringVar()
minute= StringVar()
second= StringVar()
hour.set("00")
minute.set("00")
second.set("00")
hours_1= Entry(window,textvariable= hour)
hours_1.place(x=20,y=10)
minutes_1= Entry(window,textvariable= minute)
minutes_1.place(x=100,y=10)
seconds_1= Entry(window,textvariable= second)
seconds_1.place(x=180,y=10)
def submit():
    #try and except is used when the user writes something wrong but instead of the code stopping,they get an error message
    try:
        set_time= int(hours_1.get())*3600 + int(minutes_1.get())*60 + int(seconds_1.get())
    except:
        print("Please input the right value")
    while set_time>-1:
        minutes,seconds= divmod(set_time,60)
        hours=00
        if minutes>60:
            hours,minutes= divmod(minutes,60)
        hour.set("{00:2d}".format(hours))
        minute.set("{00:2d}".format(minutes))
        second.set("{00:2d}".format(seconds))
        window.update()
        time.sleep(1)
        
        if set_time==0:
            tkinter.messagebox.showinfo("times up","times up!")
        set_time-=1

    
window.geometry("300x150")
window.title("stopwatch")

enter= Button(window,text="Set timer",command=submit)
enter.place(x=100,y=120)
window.mainloop()
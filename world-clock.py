from tkinter import *
from PIL import Image , ImageTk
from datetime import datetime
import pytz
import time

root = Tk()

root.title("World Clock")
root.geometry("600x450")

clock_img = ImageTk.PhotoImage(Image.open("clock.jpg"))


india_label = Label(root,text="India")

india_clock = Label(root)
india_clock['image'] = clock_img

india_time = Label(root)


india_label.place(relx=0.2,rely=0.05,anchor=CENTER)

india_clock.place(relx=0.2,rely=0.35,anchor=CENTER)

india_time.place(relx=0.2,rely=0.65,anchor=CENTER)



usa_label = Label(root,text="USA")

usa_clock = Label(root)
usa_clock['image'] = clock_img

usa_time = Label(root)


usa_label.place(relx=0.7,rely=0.05,anchor=CENTER)

usa_clock.place(relx=0.7,rely=0.35,anchor=CENTER)

usa_time.place(relx=0.7,rely=0.65,anchor=CENTER)


uk_label = Label(root,text="UK")

uk_clock = Label(root)
uk_clock['image'] = clock_img

uk_time = Label(root)


uk_label.place(relx=0.25,rely=0.5,anchor=CENTER)

uk_clock.place(relx=0.25,rely=0.65,anchor=CENTER)

uk_time.place(relx=0.25,rely=0.95,anchor=CENTER)


australia_label = Label(root,text="UK")

australia_clock = Label(root)
australia_clock['image'] = clock_img

australia_time = Label(root)


australia_label.place(relx=0.30,rely=0.5,anchor=CENTER)

australia_clock.place(relx=0.30,rely=0.65,anchor=CENTER)

australia_time.place(relx=0.30,rely=0.95,anchor=CENTER)


class India():
    def times(self):
        home = pytz.timezone('Asia/Kolkata')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        india_time['text'] = "Time: "+current_time
        india_time.after(200,self.times)


class USA():
    def times(self):
        home = pytz.timezone('US/Central')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        usa_time['text'] = "Time: "+current_time
        usa_time.after(200,self.times)


class UK():
    def times(self):
        home = pytz.timezone('Europe/Great Britan')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        uk_time['text'] = "Time: "+current_time
        uk_time.after(200,self.times)


class Australia():
    def times(self):
        home = pytz.timezone('Australia/ACT')
        local_time = datetime.now(home)
        current_time = local_time.strftime("%H:%M:%S")
        australia_time['text'] = "Time: "+current_time
        australia_time.after(200,self.times)
        

object_india = India()

object_usa = USA()

object_uk = UK()

object_australia = Australia()

usa_btn = Button(root,text="Show Time",command=object_usa.times)

india_btn = Button(root,text="Show Time",command=object_india.times)

uk_btn = Button(root,text="Show Time",command=object_uk.times)

australia_btn = Button(root,text="Show Time",command=object_australia.times)


usa_btn.place(relx=0.7,rely=0.8,anchor=CENTER)

india_btn.place(relx=0.2,rely=0.8,anchor=CENTER)

uk_btn.place(relx=0.25,rely=0.92,anchor=CENTER)

australia_btn.place(relx=0.30,rely=0.92,anchor=CENTER)

root.mainloop()
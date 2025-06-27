user_name = "<>"
user_password = "<>"

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk #
import os

from instabot import Bot 
instabot = Bot()

instabot.login(username = user_name,  
          password = user_password) 


def showimage():
    global file
    file = tk.filedialog.askopenfilename(initialdir = os.getcwd(),title="select image file", filetype = (("JPG File","*.jpg"),("PNG file","*.png")))
    image = Image.open(file)
    
    #Resize the image 
    resized = image.resize((480,480), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(resized)
    label.configure(image = image)
    label.image = image
    

def addimage():
    instabot.upload_photo(file,caption = entry.get())
    print("Post-Report:")
    print("File:"+ str(file))
    print("Comment:"+str(entry.get()))
    return True
    
root = tk.Tk()
root.title("Instagram-Post-App")
root.iconbitmap("insta_24.ico")
root.geometry("500x700")


label = tk.Label(root)
label.place(x = 10, y = 10, width=50, height=50)
label.pack()

frame = tk.Frame(root)
frame.pack(side = tk.BOTTOM, padx = 15, pady = 15)


entry = tk.Entry(root)
entry.place(x = 10, y = 500, width=480, height=120)




button_1 = tk.Button(frame, text = "Browse Image", command=showimage)
button_1.pack(side = tk.LEFT,padx = 10)

button_2 = tk.Button(frame, text = "Add", command=addimage)
button_2.pack(side = tk.LEFT, padx = 10)

button_3 = tk.Button(frame, text = "Close", command=root.destroy)
button_3.pack(side = tk.LEFT, padx = 10)

root.mainloop()
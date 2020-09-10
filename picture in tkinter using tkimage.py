from PIL import ImageTk, Image as image
from tkinter import *

root = Tk()
root.title("Image")
root.iconbitmap("new_pic.ico")
root.geometry("550x450")



img = image.open("my_image.jpg")
resized = img.resize((500,400), image.ANTIALIAS)
exten = "new.jpg"
hi = PhotoImage(file=exten)
picture = ImageTk.PhotoImage(resized)


close = Button(root, text="close", command=root.destroy)
close.pack()


root.mainloop()
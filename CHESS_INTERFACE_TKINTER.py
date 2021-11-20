# ## Stand alone apps interface with tkinter based on Romans Prototype :)

####################################################################################################
# CHESS INTERFACE USING PYQT5
####################################################################################################

import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
a = ("Comic Sans MS", 15, "bold")
b = ("Andale Mono", 20, "bold")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("chess_piece_knight.ico")
img = ImageTk.PhotoImage(Image.open("chess_img.jpg"))
imagelabel = tk.Label(root, image=img).grid(row=0, column=0, columnspan=2, rowspan=4)


class FirstPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Widgets()
        root.columnconfigure(0, weight=1)  # Set weight to row and
        root.rowconfigure(0, weight=1)  # column where the widget is

    # first page consists only of a start button
    def Widgets(self):
        self.StartBtn = tk.Button(root, text='START ➤', command=self.StartFunc, font=b, bg='black', fg="white")

        self.StartBtn.grid(row=0, column=0, ipady=15, ipadx=20)

    # removes button and moves to second page
    def StartFunc(self):
        self.StartBtn.destroy()
        SecondPage(root)


FirstPage(root)


class SecondPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Widgets()
        # root.columnconfigure(0, weight=1)  # Set weight to row and
        # root.rowconfigure(0, weight=1)  # column where the widget is

    # second page consists of 2 frames
    def Widgets(self):

    # MAKING BASIC LAYOUT;
        framebox_object0 = tk.Frame(root, width=500, height=50, bg="green")
        framebox_object1 = tk.Frame(root, width=100, height=500, bg="red")
        framebox_object2 = tk.Frame(root, width=400, height=500, bg="blue")
        framebox_object3 = tk.Frame(root, width=500, height=50, bg="purple")

        framebox_object0.grid_propagate(False)
        framebox_object1.grid_propagate(False)
        framebox_object2.grid_propagate(False)
        framebox_object3.grid_propagate(False)

        framebox_object0.grid(row=0, column=0, sticky="nswe", columnspan=2)
        framebox_object1.grid(row=1, column=0, sticky="nswe")
        framebox_object2.grid(row=1, column=1, sticky="nswe")
        framebox_object3.grid(row=2, column=0, sticky="nswe", columnspan=2)

    # LABELING:
        Label1 = tk.Label(framebox_object0, text="Player Movements", font=b)
        Label1.grid(row=0, column=0, sticky="nswe", columnspan=1)

        Label2 = tk.Label(framebox_object0, text="Player Prediction", font=b)
        Label2.grid(row=0, column=1, sticky="nswe", columnspan=1,padx=326)

    # BUTTONS:
        Button1 = tk.Button(framebox_object3, text='↩Restart', font=b)
        Button1.grid(row=2, column=0, sticky="nswe", columnspan=1)

        Button2 = tk.Button(framebox_object3, text='  Help  ', font=b)
        Button2.grid(row=2, column=1, sticky="nswe", columnspan=1, padx= 210)

        Button3 = tk.Button(framebox_object3, text='  End > ', font=b)
        Button3.grid(row=2, column=2, sticky="nswe", columnspan=1, padx=2)
        
    




root.mainloop()

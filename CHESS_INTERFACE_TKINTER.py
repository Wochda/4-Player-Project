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
        self.n = 0
        # root.columnconfigure(0, weight=1)  # Set weight to row and
        # root.rowconfigure(0, weight=1)  # column where the widget is

    # second page consists of 2 frames
    def Widgets(self):
        # MAKING BASIC LAYOUT:
        self.framebox_object0 = tk.Frame(root, width=500, height=50, bg="green")
        self.framebox_object1 = tk.Frame(root, width=100, height=500, bg="red")
        self.framebox_object2 = tk.Frame(root, width=400, height=500, bg="blue")
        self.framebox_object3 = tk.Frame(root, width=500, height=50, bg="purple")

        self.framebox_object0.grid_propagate(False)
        self.framebox_object1.grid_propagate(False)
        self.framebox_object2.grid_propagate(False)
        self.framebox_object3.grid_propagate(False)

        self.framebox_object0.grid(row=0, column=0, sticky="nswe", columnspan=2)
        self.framebox_object1.grid(row=1, column=0, sticky="nswe")
        self.framebox_object2.grid(row=1, column=1, sticky="nswe")
        self.framebox_object3.grid(row=2, column=0, sticky="nswe", columnspan=2)

        # LABELING:
        Label1 = tk.Label(self.framebox_object0, text="Player Movements", font=b)
        Label1.grid(row=0, column=0, sticky="nswe", columnspan=1)

        Label2 = tk.Label(self.framebox_object0, text="Player Prediction", font=b)
        Label2.grid(row=0, column=1, sticky="nswe", columnspan=1, padx=326)

        # BUTTONS:
        Button1 = tk.Button(self.framebox_object3, text='↩Restart', font=b)
        Button1.grid(row=2, column=0, sticky="nswe", columnspan=1)

        Button2 = tk.Button(self.framebox_object3, text='  Help  ', font=b)
        Button2.grid(row=2, column=1, sticky="nswe", columnspan=1, padx=210)

        Button3 = tk.Button(self.framebox_object3, text='  End > ', font=b)
        Button3.grid(row=2, column=2, sticky="nswe", columnspan=1, padx=2)

        EnterButton = tk.Button(self.framebox_object1, text='SUBMIT', font=b, command=self.EnterFunc)
        EnterButton.grid(row=2, column=0, sticky="nswe")

        # ENTRY:
        self.MoveEntry = tk.Entry(self.framebox_object1, bg="white", font=b, justify='center', width=26)
        self.MoveEntry.grid(row=1, column=0, sticky='nswe', ipady=50, pady=100)

        # SCROLLBAR:

    # scrollbars can only be made on canvas and listbox
        self.Canvas = tk.Canvas(self.framebox_object2, bg="orange", height=500)
        self.Canvas.grid(row=0, column=0, sticky="nsew")

        # then i add a frame on the  canvas
        self.canvasFrame = tk.Frame(self.Canvas, bg="#EBEBEB")
        self.Canvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')

    # scrollbar:
        Scroll = tk.Scrollbar(self.framebox_object2, orient=tk.VERTICAL)
        Scroll.grid(row=0, column=1, sticky="ns")

    # additional configurations:
        Scroll.config(command=self.Canvas.yview)
        self.Canvas.config(yscrollcommand=Scroll.set)

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)
        self.Canvas.grid_propagate(False)

    def update_scrollregion(self, event):
        self.Canvas.configure(scrollregion=self.Canvas.bbox("all"))

    def EnterFunc(self):
        # move or whatever is entered in entry:
        self.Move = self.MoveEntry.get()

        # Clear entry box to enter new word;
        self.MoveEntry.delete(0, tk.END)

        result = self.Algorithm(self.Move)

        self.n += 1

        print(self.n)
        tk.Label(self.canvasFrame, text=result + "\npercent\n", font=b).grid(row=self.n, column=0, sticky="nswe", columnspan=1)

    def Algorithm(self, move):
        return "prediction"


root.mainloop()

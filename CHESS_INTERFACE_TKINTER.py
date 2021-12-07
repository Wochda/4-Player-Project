####################################################################################################
# CHESS INTERFACE USING TKINTER
####################################################################################################

import tkinter as tk
from PIL import ImageTk, Image
from Chess_Algorithms import *

root = tk.Tk()
a = ("Courier New", 15, "bold")
b = ("Courier New", 20, "bold")
root.geometry("800x600")
root.resizable(False, False)
root.iconbitmap("chess_piece_knight.ico")
img = ImageTk.PhotoImage(Image.open("chess_img.jpg"))
imagelabel = tk.Label(root, image=img).grid(row=0, column=0, columnspan=2, rowspan=4)


# HOME PAGE - CONTAINING START OPTION
class FirstPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Widgets()
        root.columnconfigure(0, weight=1)  # Set weight to row and
        root.rowconfigure(0, weight=1)  # column where the widget is

    # START BUTTON WHICH TAKES US TO THE SECOND PAGE WHERE PREDICTIONS ARE MADE
    def Widgets(self):
        self.StartBtn = tk.Button(root, text='START ➤', command=self.StartFunc, font=b, bg='black', fg="white")

        self.StartBtn.grid(row=0, column=0, ipady=15, ipadx=20)

    # FUNCTION CALLED WHEN START  BUTTON IS CLICKED: MOVES USER TO SECOND PAGE
    def StartFunc(self):
        self.StartBtn.destroy()
        SecondPage(root)


FirstPage(root)


class SecondPage(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.Widgets()
        self.n = 0

    # SECOND PAGE
    # CONSISTS OF 2 FRAMES; ONE FOR ENTERING USER MOVES AND THE OTHER GIVES PREDICTIONS
    def Widgets(self):
        # BASIC LAYOUT SETUP:
        self.framebox_object0 = tk.Frame(root, width=500, height=50, bg='black')
        self.framebox_object1 = tk.Frame(root, width=100, height=500, bg='black')
        self.framebox_object2 = tk.Frame(root, width=400, height=500, bg='black')
        self.framebox_object3 = tk.Frame(root, width=500, height=50, bg='black')

        self.framebox_object0.grid_propagate(False)
        self.framebox_object1.grid_propagate(False)
        self.framebox_object2.grid_propagate(False)
        self.framebox_object3.grid_propagate(False)

        self.framebox_object0.grid(row=0, column=0, sticky="nswe", columnspan=2)
        self.framebox_object1.grid(row=1, column=0, sticky="nswe")
        self.framebox_object2.grid(row=1, column=1, sticky="nswe")
        self.framebox_object3.grid(row=2, column=0, sticky="nswe", columnspan=2)

        # LABELING:
        self.Label1 = tk.Label(self.framebox_object0, text="Player Movements", font=b, bg='black', fg="white")
        self.Label1.grid(row=0, column=0, sticky="nswe", columnspan=1)

        self.Label2 = tk.Label(self.framebox_object0, text="Player Prediction", font=b, bg='black', fg="white")
        self.Label2.grid(row=0, column=1, sticky="nswe", columnspan=1, padx=250)

        # BUTTONS:
        self.Button1 = tk.Button(self.framebox_object3, text='↩Restart', font=b, command=self.RestartFunc, bg='black',
                                 fg="white")
        self.Button1.grid(row=2, column=0, sticky="nswe", columnspan=1)

        self.Button2 = tk.Button(self.framebox_object3, text='  Help  ', font=b, command=self.HelpFunc, bg='black',
                                 fg="white")
        self.Button2.grid(row=2, column=1, sticky="nswe", columnspan=1, padx=173)

        self.Button3 = tk.Button(self.framebox_object3, text='  End > ', font=b, command=self.EndFunc, bg='black',
                                 fg="white")
        self.Button3.grid(row=2, column=2, sticky="nswe", columnspan=1)

        self.EnterButton = tk.Button(self.framebox_object1, text='SUBMIT', font=b, command=self.EnterFunc, bg="grey")
        self.EnterButton.grid(row=2, column=0, sticky="nswe")

        # ENTRY:
        self.MoveEntry = tk.Entry(self.framebox_object1, bg="white", font=b, justify='center', width=26)
        self.MoveEntry.grid(row=1, column=0, sticky='nswe', ipady=50, pady=100)

        # SCROLLBAR:

        # SCROLLBARS ARE MADE ON CANVAS AND LISTBOXES
        self.Canvas = tk.Canvas(self.framebox_object2, bg="black", height=500)
        self.Canvas.grid(row=0, column=0, sticky="nsew")

        # ADDING FRAME ON CANVAS
        self.canvasFrame = tk.Frame(self.Canvas, bg="black")
        self.Canvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')

        # SCROLLBAR:
        Scroll = tk.Scrollbar(self.framebox_object2, orient=tk.VERTICAL)
        Scroll.grid(row=0, column=1, sticky="ns")

        # ADDITIONAL CONFIGURATIONS:
        Scroll.config(command=self.Canvas.yview)
        self.Canvas.config(yscrollcommand=Scroll.set)

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)
        self.Canvas.grid_propagate(False)

    def update_scrollregion(self, event):
        self.Canvas.configure(scrollregion=self.Canvas.bbox("all"))

    # FUNCTION CALLED WHEN SUBMIT BUTTON IS CALLED
    # IT CLEARS ENTRY BOX AND CALLS ALGORITHM FUNCTION WITH THE USERS MOVE ENTERED
    def EnterFunc(self):
        # move or whatever is entered in entry:
        self.Move = self.MoveEntry.get()

        # Clear entry box to enter new word;
        self.MoveEntry.delete(0, tk.END)

        result = self.Algorithm(self.Move)

        self.n += 1

        print(self.n)
        tk.Label(self.canvasFrame, text=result[0], font=b, bg='black', fg="white").grid(row=self.n + 1, column=0,
                                                                                        sticky="nswe", columnspan=1)
        tk.Label(self.canvasFrame, text=result[1], font=b, bg='black', fg="white").grid(row=self.n + 2, column=0,
                                                                                        sticky="nswe", columnspan=1)
        tk.Label(self.canvasFrame, text=result[2], font=b, bg='black', fg="white").grid(row=self.n + 3, column=0,
                                                                                        sticky="nswe", columnspan=1)

    # FUNCTION CALLED WHEN HELP BUTTON IS CALLED
    def HelpFunc(self):
        # DESTROY PREVIOUS WINDOW:
        self.framebox_object2.destroy()
        self.framebox_object1.destroy()
        self.framebox_object0.destroy()

        self.Label1.destroy()
        self.Label2.destroy()

        self.Button1.destroy()
        self.Button2.destroy()
        self.Button3.destroy()
        self.EnterButton.destroy()

        self.Canvas.destroy()

        # framebox
        self.framebox_object2 = tk.Frame(root, width=400, height=500, bg='black')
        self.framebox_object2.grid(row=0, column=0, sticky="nswe")

        # Scrollbars can only be made on canvas and listbox
        self.Canvas = tk.Canvas(self.framebox_object2, bg='black', height=550, width=780)
        self.Canvas.grid(row=0, column=0, sticky="nsew")

        # then i add a frame on the  canvas
        self.canvasFrame = tk.Frame(self.Canvas, bg='black')
        self.Canvas.create_window(0, 0, window=self.canvasFrame, anchor='nw')

        # scrollbar:
        Scroll = tk.Scrollbar(self.framebox_object2, orient=tk.VERTICAL)
        Scroll.grid(row=0, column=1, sticky="ns")

        # additional configurations:
        Scroll.config(command=self.Canvas.yview)
        self.Canvas.config(yscrollcommand=Scroll.set)

        self.canvasFrame.bind("<Configure>", self.update_scrollregion)
        self.Canvas.grid_propagate(False)

        # LABELING:
        self.Label1 = tk.Label(self.canvasFrame, text="Documentation", font=b, bg='black', fg="white")
        self.Label1.grid(row=0, column=0, sticky="nswe", columnspan=1)

        # BUTTONS:
        self.Button1 = tk.Button(self.framebox_object3, text='↩Return', font=b, command=self.ReturnToGameFunc,
                                 bg='black', fg="white")
        self.Button1.grid(row=2, column=0, sticky="nswe", columnspan=1)

        with open('documentation.txt', 'r') as f:
            file_contents = f.read()
            tk.Label(self.canvasFrame, text=file_contents, font=a, bg='black', fg="white").grid(row=1, column=0, sticky="nswe", columnspan=2)

    # RETURNS USER TO START PAGE
    def EndFunc(self):
        # DESTROY PREVIOUS WINDOW:
        self.framebox_object2.destroy()
        self.framebox_object1.destroy()
        self.framebox_object0.destroy()
        self.framebox_object3.destroy()

        self.Label1.destroy()
        self.Label2.destroy()

        self.Button1.destroy()
        self.Button2.destroy()
        self.Button3.destroy()
        self.EnterButton.destroy()

        self.Canvas.destroy()
        FirstPage(self)

    def RestartFunc(self):
        # DESTROY PREVIOUS WINDOW:
        self.framebox_object2.destroy()
        self.framebox_object1.destroy()
        self.framebox_object0.destroy()
        self.framebox_object3.destroy()

        self.Label1.destroy()
        self.Label2.destroy()

        self.Button1.destroy()
        self.Button2.destroy()
        self.Button3.destroy()
        self.EnterButton.destroy()

        self.Canvas.destroy()

        FirstPage(self)

    # CALLED USER WANTS TO LEAVE THE HELP PAGE BACK TO SECOND PAGE
    def ReturnToGameFunc(self):
        # DESTROY PREVIOUS WINDOW:
        self.framebox_object3.destroy()
        self.framebox_object2.destroy()
        self.Canvas.destroy()

        self.Label1.destroy()

        self.Button1.destroy()

        SecondPage(self)

# FUNCTION IS CALLED FROM ENTERFUNC WHEN USER ENTERS MOVE
# FUNCTION TAKES MOVES FROM USERS AND MAKES POSSIBLE PREDICTIONS USING ALGORITHM
    def Algorithm(self, move):
        # "Algorithm"

        feeds = set()
        feed = ""
        predictions = {}

        totalpoints = 0
        while feed != "EXIT":

            feed = move

            # iterate pandas df by rows
            for entry in df_raw.itertuples():

                if feed == entry[2]:
                    feeds.add(feed)

                    # check if player is already in dict
                    if entry[1] not in predictions.keys():
                        predictions[entry[1]] = 1
                    else:
                        pass
                    # found move -> +1
                    predictions[entry[1]] = predictions.get(entry[1]) + 1

                    # sort dict descending
            predictions2 = dict(sorted(predictions.items(), key=lambda x: x[1], reverse=True))

            # get total amount of points

            # calculate percentage

            for key, value in predictions2.items():
                totalpoints += value

            for key, value in predictions2.items():
                predictions2[key] = round(((100 * value) / totalpoints) * 100, 2)

            print(sorted(predictions2.items(), key=operator.itemgetter(1), reverse=True)[:3])

            return (sorted(predictions2.items(), key=operator.itemgetter(1), reverse=True)[:3])



root.mainloop()

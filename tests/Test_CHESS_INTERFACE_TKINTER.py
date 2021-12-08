import pytest
import tkinter as tk
from PIL import ImageTk, Image
from CHESS_INTERFACE_TKINTER import FirstPage, SecondPage

#creating a fixture for the root
@pytest.fixture
def root():
    root = tk.Tk()
    a = ("Courier New", 15, "bold")
    b = ("Courier New", 20, "bold")
    root.geometry("800x600")
    root.resizable(False, False)
    root.iconbitmap(r"C:\Users\Iulia\PycharmProjects\SoftwareEngineeringProject\chess_piece_knight.ico")
    img = ImageTk.PhotoImage(Image.open(r"C:\Users\Iulia\PycharmProjects\SoftwareEngineeringProject\chess_img.jpg"))
    imagelabel = tk.Label(root, image=img).grid(row=0, column=0, columnspan=2, rowspan=4)
    yield root

@pytest.mark.usefixtures("root")
class TestFirstPage(tk.Frame):
    # create first page
    fp = FirstPage(root)
    def test_Widgets(self):
        TestFirstPage.fp.Widgets()
        # testing the text of the start button
        assert TestFirstPage.fp.StartBtn["text"] == "START ➤"
    def test_StartFunc(self):
        TestFirstPage.fp.StartFunc()
        # check if the start button exists
        assert not TestSecondPage.fp.StartButton

@pytest.mark.usefixtures("root")
class TestSecondPage(tk.Frame):
    # create second page
    sp=SecondPage(root)
    def test_Widgets(self):
        TestSecondPage.sp.Widgets()

        # checking if the framebox objects exist on the page
        assert TestSecondPage.sp.framebox_object0 != None
        assert TestSecondPage.sp.framebox_object1 != None
        assert TestSecondPage.sp.framebox_object2 != None
        assert TestSecondPage.sp.framebox_object3 != None

        # check if the labels exist and also their text message
        assert TestSecondPage.sp.Label1 != None
        assert TestSecondPage.sp.Label1["text"] == "Player Movements"
        assert TestSecondPage.sp.Label2 != None
        assert TestSecondPage.sp.Label2["text"] == "Player Prediction"

        # check if the buttons exist and also their text message
        assert TestSecondPage.sp.Button1 != None
        assert TestSecondPage.sp.Button1["text"] == '↩Restart'
        assert TestSecondPage.sp.Button2 != None
        assert TestSecondPage.sp.Button2["text"] == '  Help  '
        assert TestSecondPage.sp.Button3 != None
        assert TestSecondPage.sp.Button3["text"] == '  End > '
        assert TestSecondPage.sp.EnterButton != None
        assert TestSecondPage.sp.EnterButton["text"] == 'SUBMIT'

        # check if the MoveEntry, Canvas, canvasFrame, scroll objects appear
        assert TestSecondPage.sp.MoveEntry != None

        assert TestSecondPage.sp.Canvas != None
        assert TestSecondPage.sp.Canvas['height'] == 500

        assert TestSecondPage.sp.canvasFrame != None

        assert TestSecondPage.sp.Scroll != None

    def test_EnterFunc(self):
        TestSecondPage.sp.EnterFunc()
        assert TestSecondPage.sp.result != None
        assert TestSecondPage.sp.result != None
        assert TestSecondPage.sp.result in TestSecondPage.sp.Label['text']

        assert not TestSecondPage.sp.Button2

        assert TestSecondPage.sp.Label1['text'] == "Documentation"


    def test_EndFunc(self):
        # check if the objects disappeared
        assert not TestSecondPage.sp.Button1
        assert not TestSecondPage.sp.Button2
        assert not TestSecondPage.sp.Button3
        assert not TestSecondPage.sp.EnterButton
        assert not TestSecondPage.sp.Label1
        assert not TestSecondPage.sp.Label2
        assert not TestSecondPage.sp.Canvas
        assert not TestSecondPage.sp.framebox_object0
        assert not TestSecondPage.sp.framebox_object1
        assert not TestSecondPage.sp.framebox_object2
        assert not TestSecondPage.sp.framebox_object3


    def test_ReturnToGame(self):
        # check if the objects disappeared
        assert not TestSecondPage.sp.Button1
        assert not TestSecondPage.sp.Canvas
        assert not TestSecondPage.sp.framebox_object3
        assert not TestSecondPage.sp.framebox_object2


import tkinter
from tkinter import messagebox
window = tkinter.Tk()
window.geometry('480x480')
window.iconbitmap("tic3.ico")

window.title("TIC TAC TOE GAME")

label_1 = tkinter.Label(window, text="Tic Tac Toe Game", fg='black', bg='cyan', font=("Helvetica", 18))
label_1.grid(row=0, column=0, sticky='e')
label_2 = tkinter.Label(window, text="                 ").grid(row=1, column=0)


label_3 = tkinter.Label(window, text="PLAYER 1", font=("Helvetica", 11)).grid(row=2, column=0)
a= tkinter.StringVar()
a.set("START PLAYING")
label_5 = tkinter.Label(window, text="PLAYER 2", textvariable=a, font=("TimesRoman", 8))
label_5.grid(row=3, column=0)
label_4 = tkinter.Label(window, text="PLAYER 2", font=("Helvetica", 11)).grid(row=4, column=0)

b = tkinter.StringVar()
label_6 = tkinter.Label(window, text=b, textvariable=b, font=("Helvetica", 11))
label_6.grid(row=5, column=3, sticky='ew')
frame_1 = tkinter.Frame(window, relief= 'raised', background='beige')
frame_1.grid(row=3, column=3, sticky='ew')
turn=1
flag=0





def working(button):
    global turn,flag
    if button["text"] == " " and turn == 1:

        button["text"] = "X"
        a.set("PLAYER 2 TURN")
        turn = 2
        flag+=1

        check()
    elif button["text"] == " " and turn == 2:
        button["text"] = "O"
        turn = 1
        flag+=1
        a.set("PLAYER 1 TURN")

        check()


def check():
    b1 = button1["text"]
    b2 = button2["text"]
    b3 = button3["text"]
    b4 = button4["text"]
    b5 = button5["text"]
    b6 = button6["text"]
    b7 = button7["text"]
    b8 = button8["text"]
    b9 = button9["text"]

    if b1 == b2 and b2 == b3 and (b1 == "X" or b1 == "O"):
        if b1 == "X":
          b.set("Player {} wins".format(turn-1))
        elif b2 == "O":
            b.set("Player {} wins".format(turn+1))
        last()

    if b4 == b5 and b5 == b6 and (b4 == "X" or b4 == "O"):
        if b4 == "X":
            b.set("Player {} wins".format(turn-1))
        elif b4 == "O":
            b.set("Player {} wins".format(turn+1))
        last()
    if b7 == b8 and b8 == b9 and (b7 == "X" or b7 == "O"):
        if b7 == "X":
            b.set("Player {} wins".format(turn-1))
        elif b7 == "O":
            b.set("Player {} wins".format(turn+1))
        last()
    if b1 == b4 and b4 == b7 and (b1 == "X" or b1 == "O"):
        if b1 == "X":
            b.set("Player {} wins".format(turn-1))
        elif b1 == "O":
            b.set("Player {} wins".format(turn+1))
        last()
    if b2 == b5 and b5 == b8 and (b2 == "X" or b2 == "O"):
        if b2 == "X":
                b.set("Player {} wins".format(turn-1))
        elif b2 == "O":
                b.set("Player {} wins".format(turn+1))
        last()
    if b3 == b6 and b6 == b9 and (b3 == "X" or b3 == "O"):
        if b3 == "X":
                b.set("Player {} wins".format(turn-1))
        elif b3 == "O":
                b.set("Player {} wins".format(turn+1))
        last()
    if b1 == b5 and b5 == b9 and (b1 == "X" or b1 == "O"):
        if b1 == "X":
            b.set("Player {} wins".format(turn-1))
        elif b1 == "O":
            b.set("Player {} wins".format(turn+1))
        last()
    if b3 == b5 and b5 == b7 and (b3 == "X" or b3 == "O"):
        if b3 == "X":
            b.set("Player {} wins".format(turn-1))
        elif b3 == "O":
            b.set("Player {} wins".format(turn+1))
        last()
    if flag == 9:
        b.set("Match Tied")
        last()


def last():
    global flag,turn
    result = messagebox.askquestion("Game Over","Play again?")
    if result =="yes":
        button1["text"] = " "
        button2["text"] = " "
        button3["text"] = " "
        button4["text"] = " "
        button5["text"] = " "
        button6["text"] = " "
        button7["text"] = " "
        button8["text"] = " "
        button9["text"] = " "
        flag=0
        a.set("START PLAYING")
        b.set(" ")


    elif result == "no":
        result1 = messagebox.showwarning("WARNING","The game will close")
        window.quit()


button1 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button1))
button1.grid(row=3, column=1)
button2 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button2))
button2.grid(row=3, column=2)
button3 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button3))
button3.grid(row=3, column=3)
button4 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button4))
button4.grid(row=4, column=1)
button5 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button5))
button5.grid(row=4, column=2)
button6 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button6))
button6.grid(row=4, column=3)
button7 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button7))
button7.grid(row=5, column=1)
button8 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button8))
button8.grid(row=5, column=2)
button9 = tkinter.Button(frame_1, text=" ", background='beige', width='9', height='4', command=lambda: working(button9))
button9.grid(row=5, column=3)
window.mainloop()



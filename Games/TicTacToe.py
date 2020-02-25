from tkinter import *
import tkinter.messagebox
from pygame import mixer

tk = Tk()
tk.title("Tic Tac Toe")
tk.geometry('600x600')

mixer.init()

player1_name = StringVar()
playerb = StringVar()
p1 = StringVar()
p2 = StringVar()

upper_frame = Frame(tk, bg='#66B933', bd=2)
upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

player1_name = Entry(upper_frame, textvariable=p1, bd=5)
player1_name.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.5)
player2_name = Entry(upper_frame, textvariable=p2, bd=5)
player2_name.place(relx=0.4, rely=0.51, relwidth=0.6, relheight=0.5)

label = Label(upper_frame, text="Player 1:", font=('Autobus Bold', 30), bg='#66B933', fg='white', height=1, width=8)
label.place(relx=0, rely=0, relwidth=0.4, relheight=0.5)

label = Label(upper_frame, text="Player 2:", font=('Autobus Bold', 30), bg='#66B933', fg='white', height=1, width=8)
label.place(relx=0, rely=0.51, relwidth=0.4, relheight=0.5)

bclick = True
flag = 0


def disableButton():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btnClick(buttons):
    mixer.music.load("Click.wav")
    mixer.music.play()
    global bclick, flag, player2_name, player1_name, playerb, player1_name
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        playerb = p2.get() + " Wins!"
        player1_name = p1.get() + " Wins!"
        checkForWin()
        flag += 1


    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        checkForWin()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def checkForWin():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player1_name)

    elif (flag == 8):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")

    elif (button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
          button4['text'] == 'o' and button5['text'] == 'o' and button6['text'] == 'o' or
          button7['text'] == 'o' and button8['text'] == 'o' and button9['text'] == 'o' or
          button1['text'] == 'o' and button5['text'] == 'o' and button9['text'] == 'o' or
          button3['text'] == 'o' and button5['text'] == 'o' and button7['text'] == 'o' or
          button1['text'] == 'o' and button2['text'] == 'o' and button3['text'] == 'o' or
          button1['text'] == 'o' and button4['text'] == 'o' and button7['text'] == 'o' or
          button2['text'] == 'o' and button5['text'] == 'o' and button8['text'] == 'o' or
          button7['text'] == 'o' and button6['text'] == 'o' and button9['text'] == 'o'):
        disableButton()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", playerb)


buttons = StringVar()

lower_frame = Frame(tk, bg='#2c2c2c', bd=2)
lower_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

button1 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button1))
button1.place(relx=0, rely=0, relwidth=0.3, relheight=0.3)

button2 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button2))
button2.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.3)

button3 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button3))
button3.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.3)

button4 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button4))
button4.place(relx=0, rely=0.35, relwidth=0.3, relheight=0.3)

button5 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button5))
button5.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.3)

button6 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button6))
button6.place(relx=0.7, rely=0.35, relwidth=0.3, relheight=0.3)

button7 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button7))
button7.place(relx=0, rely=0.7, relwidth=0.3, relheight=0.3)

button8 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button8))
button8.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.3)

button9 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btnClick(button9))
button9.place(relx=0.7, rely=0.7, relwidth=0.3, relheight=0.3)

tk.mainloop()

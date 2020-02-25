from Global_functions import *
from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title("Tic Tac Toe")
tk.geometry('600x600')

player1_name = StringVar()
player2_name = StringVar()
p1 = StringVar()
p2 = StringVar()

upper_frame = Frame(tk, bg='#66B933', bd=2)
upper_frame.place(relx=0, rely=0, relwidth=1, relheight=0.2)

player1_name = Entry(upper_frame, textvariable=p1, bd=5)
player1_name.place(relx=0.4, rely=0, relwidth=0.6, relheight=0.5)
player2_name = Entry(upper_frame, textvariable=p2, bd=5)
player2_name.place(relx=0.4, rely=0.51, relwidth=0.6, relheight=0.5)

label = Label(upper_frame, text="Player 1 (X):", font=('Autobus Bold', 30), bg='#66B933', fg='white', height=1, width=8)
label.place(relx=0, rely=0, relwidth=0.4, relheight=0.5)

label = Label(upper_frame, text="Player 2 (O):", font=('Autobus Bold', 30), bg='#66B933', fg='white', height=1, width=8)
label.place(relx=0, rely=0.51, relwidth=0.4, relheight=0.5)

bclick = True
flag = 0


def disable_button():
    button1.configure(state=DISABLED)
    button2.configure(state=DISABLED)
    button3.configure(state=DISABLED)
    button4.configure(state=DISABLED)
    button5.configure(state=DISABLED)
    button6.configure(state=DISABLED)
    button7.configure(state=DISABLED)
    button8.configure(state=DISABLED)
    button9.configure(state=DISABLED)


def btn_click(buttons):
    click_sound()
    global bclick, flag, player2_name, player1_name, player2_name, player1_name
    if buttons["text"] == " " and bclick == True:
        buttons["text"] = "X"
        bclick = False
        player2_name = p2.get() + " Wins!"
        player1_name = p1.get() + " Wins!"
        check_for_win()
        flag += 1

    elif buttons["text"] == " " and bclick == False:
        buttons["text"] = "O"
        bclick = True
        check_for_win()
        flag += 1
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")


def check_for_win():
    if (button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button4['text'] == 'X' and button5['text'] == 'X' and button6['text'] == 'X' or
            button7['text'] == 'X' and button8['text'] == 'X' and button9['text'] == 'X' or
            button1['text'] == 'X' and button5['text'] == 'X' and button9['text'] == 'X' or
            button3['text'] == 'X' and button5['text'] == 'X' and button7['text'] == 'X' or
            button1['text'] == 'X' and button2['text'] == 'X' and button3['text'] == 'X' or
            button1['text'] == 'X' and button4['text'] == 'X' and button7['text'] == 'X' or
            button2['text'] == 'X' and button5['text'] == 'X' and button8['text'] == 'X' or
            button7['text'] == 'X' and button6['text'] == 'X' and button9['text'] == 'X'):
        disable_button()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player1_name)

    elif flag == 8:
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
        disable_button()
        tkinter.messagebox.showinfo("Tic-Tac-Toe", player2_name)


buttons = StringVar()

lower_frame = Frame(tk, bg='#2c2c2c', bd=2)
lower_frame.place(relx=0, rely=0.2, relwidth=1, relheight=0.8)

button1 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button1))
button1.place(relx=0, rely=0, relwidth=0.3, relheight=0.3)

button2 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button2))
button2.place(relx=0.35, rely=0, relwidth=0.3, relheight=0.3)

button3 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button3))
button3.place(relx=0.7, rely=0, relwidth=0.3, relheight=0.3)

button4 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button4))
button4.place(relx=0, rely=0.35, relwidth=0.3, relheight=0.3)

button5 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button5))
button5.place(relx=0.35, rely=0.35, relwidth=0.3, relheight=0.3)

button6 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button6))
button6.place(relx=0.7, rely=0.35, relwidth=0.3, relheight=0.3)

button7 = Button(lower_frame, text=" ", font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button7))
button7.place(relx=0, rely=0.7, relwidth=0.3, relheight=0.3)

button8 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button8))
button8.place(relx=0.35, rely=0.7, relwidth=0.3, relheight=0.3)

button9 = Button(lower_frame, text=' ', font=('Autobus Bold', 70), bg='gray', fg='white', height=4, width=8,
                 command=lambda: btn_click(button9))
button9.place(relx=0.7, rely=0.7, relwidth=0.3, relheight=0.3)

tk.mainloop()

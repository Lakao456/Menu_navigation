from tkinter import *
from tkinter import messagebox
import winsound
import sys
import os


def click_sound():
    winsound.PlaySound("Click.wav", winsound.SND_ASYNC)


def TicTacToe():
    click_sound()
    os.system("TicTacToe.py")


def GuessingGame():
    click_sound()
    os.system("GuessingGame.py")


game_menu = Tk()
game_menu.title('GAMES')
game_menu.geometry("600x600")
game_menu.configure(bg="black")

game_menu_frame = Frame(game_menu, bg='#66B933')
game_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

TicTacToe = Button(game_menu_frame, text=("Tic Tac Toe"), bg=("grey"), font=('Autobus Bold', 25), command=TicTacToe)
TicTacToe.place(relx=0.25, rely=0.1, relheight=0.2, relwidth=0.5)

GuessingGame = Button(game_menu_frame, text=("Guessing Game"), bg=("grey"), font=('Autobus Bold', 25),
                      command=GuessingGame)
GuessingGame.place(relx=0.25, rely=0.35, relheight=0.2, relwidth=0.5)

# PythonsAndLadders = Button(game_menu_frame , text=("Pythons And Ladders"), bg=("grey"), font=('Autobus Bold',25), command=gameButton)
# PythonsAndLadders.place(relx=0.1, rely=0.6, relheight=0.2, relwidth=0.8)

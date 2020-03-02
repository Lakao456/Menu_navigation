import Global_functions as Gfunc
from tkinter import *


def Game_menu():
    game_menu = Tk()
    game_menu.title('GAMES')
    game_menu.geometry("600x600")
    game_menu.configure(bg="black")

    game_menu_frame = Frame(game_menu, bg='#66B933')
    game_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

    buttons = [{"name": "Tic Tac Toe^", "func_name": "TicTacToe"},
               {"name": "Guess the number", "func_name": "GuessingGame"},
               {"name": "Dodge the blocks^", "func_name": "DodgeTheBlocks"},
               {"name": "Pythons and ladders*", "func_name": "PythonsAndLadders"}]

    Gfunc.create_buttons(game_menu, game_menu_frame, buttons, 1)

    Gfunc.create_back_button(game_menu)

    mainloop()

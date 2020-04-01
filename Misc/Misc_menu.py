import Global_functions as Gfunc
from tkinter import *


def Misc_menu():
    misc_menu = Tk()
    misc_menu.title('MISC')
    misc_menu.geometry("600x600")
    misc_menu.configure(bg="black")

    misc_menu_frame = Frame(misc_menu, bg='#66B933')
    misc_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

    buttons = [{"name": "Quiz Game", "func_name": "Quiz_game"}]

    Gfunc.create_buttons(misc_menu, misc_menu_frame, buttons, 1)

    Gfunc.create_back_button(misc_menu)

    mainloop()

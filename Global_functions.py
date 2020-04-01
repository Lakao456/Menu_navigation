from tkinter import *
import winsound
from functools import partial
import sys

sys.path.append('.//Games')
sys.path.append('.//Tools')
sys.path.append('.//WeatherApp')
sys.path.append('.//Misc')

from Game_menu import Game_menu
from TicTacToe import TicTacToe
from GuessingGame import GuessingGame
from DodgeTheBlocks import DodgeTheBlocks
from GuessingGame import GuessingGame

from Tools_menu import Tools_menu
from Area_calculator import Area_calculator
from BMI_calculator import BMI_calculator
from Temperature_converter import Temperature_converter

# from WeatherApp import Weather_App
#
# from Misc_menu import Misc_menu
# from Quiz_game import Quiz_game
# from Questions import Questions

print("**Global_functions IMPORTED**")


def create_buttons(root, parent_frame, buttons_list, column_num=1):
    global b_height

    def button_click(buttons_list2, n=0):
        click_sound()
        buttons[n].config(command=eval(buttons_list2[n]['func_name'] + '()'))

    if len(buttons_list) % 2 == 0:
        buttons_qty = len(buttons_list)
    else:
        buttons_qty = len(buttons_list) + 1

    buttons, left_i, right_i = [], 0, 0

    for i in range(len(buttons_list)):
        if column_num == 2:
            b_height = 1.88 / buttons_qty
            if i % 2 == 0:
                left_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="#8c8c8c", font=('Autobus Bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.01,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=b_height,
                                  relwidth=0.485)
            else:
                right_i += 1
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="#8c8c8c", font=('Autobus Bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.505,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=b_height,
                                  relwidth=0.485)
        elif column_num == 1:
            buttons.append(Button(parent_frame, text=(buttons_list[i]["name"]), bg="#8c8c8c", font=('Autobus Bold', 20),
                                  relief=GROOVE,
                                  command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.25,
                              rely=0.01 + (0.005 + b_height) * i,
                              relheight=b_height,
                              relwidth=0.5)


def click_sound():
    winsound.PlaySound(".\\Resources\\Sounds\\Click.wav", winsound.SND_ASYNC)


def create_back_button(parent_frame):
    back_button = Button(parent_frame, text='<--', font=('Autobus Bold', 20), command=parent_frame.destroy)
    back_button.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.1)

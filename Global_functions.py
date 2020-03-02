from tkinter import *
import winsound
from functools import partial
import sys

sys.path.append('.//Games')
sys.path.append('.//Tools')
sys.path.append('.//WeatherApp')

from Game_menu import Game_menu
from TicTacToe import TicTacToe
from GuessingGame import GuessingGame
from DodgeTheBlocks import DodgeTheBlocks
from GuessingGame import GuessingGame

from Tools_menu import Tools_menu
from Area_calculator import Area_calculator
from BMI_calculator import BMI_calculator
from Temperature_converter import Temperature_converter

from WeatherApp import Weather_App

print("**Global_functions IMPORTED**")


def create_buttons(root, parent_frame, buttons_list, column_num=1):
    def button_click(buttons_list2, n=0):
        click_sound()
        buttons[n].config(command=eval(buttons_list2[n]['func_name'] + '()'))

    buttons_qty = len(buttons_list)
    buttons = []
    for i in range(0, buttons_qty):
        if column_num == 2:
            if i % 2 == 0:
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.1, rely=(i * (1 / buttons_qty)) + (0.01 * i),
                                  relheight=1.3 * (1 / buttons_qty),
                                  relwidth=0.35)
            else:
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.5, rely=((i - 1) * (1 / buttons_qty)) + (0.01 * (i - 1)),
                                  relheight=1.3 * (1 / buttons_qty), relwidth=0.35)
        elif column_num == 1:
            buttons.append(Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                                  command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.1, rely=(i * (1 / buttons_qty)) + 0.01,
                              relheight=0.9 * (1 / buttons_qty), relwidth=0.7)


def click_sound():
    winsound.PlaySound(".\\Resources\\Sounds\\Click.wav", winsound.SND_ASYNC)


def create_back_button(parent_frame):
    back_button = Button(parent_frame, text='<--', font=('Autobus Bold', 20), command=parent_frame.destroy)
    back_button.place(relx=0.01, rely=0.01, relheight=0.05, relwidth=0.1)

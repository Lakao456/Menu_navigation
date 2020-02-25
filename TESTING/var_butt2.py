from tkinter import *
import winsound
from functools import partial
from tkinter import messagebox
import sys
import os

root = Tk()
root.title('Project')
root.geometry("600x600")
root.configure(bg="black")

main_frame = LabelFrame(root, bg='black', bd=5)
main_frame.place()

upper_frame = Frame(root, bg='#66B933', bd=5, )
upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.5, anchor="n")

apps_label = Label(upper_frame, text='APPS', font=('Autobus Bold', 50), bg="white")
apps_label.place(relheight=1, relwidth=1)

lower_frame = Frame(root, bg='#66B933', bd=5)
lower_frame.place(relx=0.5, rely=0.4, relheight=0.5, relwidth=0.8, anchor='n')


def create_buttons(parent_frame, buttons_list, column_num=1):
    def button_click(buttons_list2, n=0):
        print("debug")
        buttons[n].config(command=os.system(buttons_list2[n]["path"]))

    buttons_qty = len(buttons_list)
    buttons = []
    for i in range(0, buttons_qty):
        if column_num == 2:
            if i % 2 == 0:
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.1, rely=(i * (1 / buttons_qty)) - (0.02 * i),
                                  relheight=1.3 * (1 / buttons_qty),
                                  relwidth=0.35)
            else:
                buttons.append(
                    Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                           command=partial(button_click, buttons_list, i)))
                buttons[-1].place(relx=0.5, rely=((i - 1) * (1 / buttons_qty)) - (0.02 * (i - 1)),
                                  relheight=1.3 * (1 / buttons_qty), relwidth=0.35)
        elif column_num == 1:
            buttons.append(Button(parent_frame, text=(buttons_list[i]["name"]), bg="grey", font=('Autobus Bold', 20),
                                  command=partial(button_click, buttons_list, i)))
            buttons[-1].place(relx=0.3, rely=(i * (1 / buttons_qty)) - (0.002 * i),
                              relheight=0.9 * (1 / buttons_qty), relwidth=0.4)


b_list = [{"name": "Games", "path": "Game_menu.py"},
          {"name": "Tools", "path": "\Tools\Tools_menu.py"},
          {"name": "Music*", "path": "\Music\Music_player.py"},
          {"name": "Weather", "path": "\WeatherApp\WeatherApp.py"},
          {"name": "Store*", "path": "\Store\Store.py"},
          {"name": "Misc*", "path": "\Misc\Misc.py"}]

create_buttons(lower_frame, b_list, 2)

mainloop()

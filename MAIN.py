import Global_functions as Gf
from tkinter import *

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

buttons = [{"name": "Games", "path": ".\\Games\\Game_menu.py"},
           {"name": "Tools", "path": ".\\Tools\\Tools_menu.py"},
           {"name": "Music*", "path": ".\\Music\\Music_player.py"},
           {"name": "Weather^", "path": ".\\WeatherApp\\WeatherApp.py"},
           {"name": "Store*", "path": ".\\Store\\Store.py"},
           {"name": "Misc*", "path": ".\\Misc\\Misc.py"}]

Gf.create_buttons(root, lower_frame, buttons, 2)

root.mainloop()

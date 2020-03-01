import Global_Func_clone as GfuncC
from tkinter import *

test_menu = Tk()
test_menu.title('TESTS')
test_menu.geometry("600x600")
test_menu.configure(bg="black")

test_menu_frame = Frame(test_menu, bg='#66B933')
test_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

buttons = [{"name": "one", "func_name": "test_func1"},
           {"name": "2", "func_name": ".\\2.py"},
           {"name": "3", "func_name": ".\\3.py"},
           {"name": "4", "func_name": ".\\4.py"}]


GfuncC.create_buttons(test_menu, test_menu_frame, buttons, 1)

GfuncC.create_back_button(test_menu)

mainloop()

from Global_functions import *

tools_menu = Tk()
tools_menu.title('GAMES')
tools_menu.geometry("600x600")
tools_menu.configure(bg="black")

tools_menu_frame = Frame(tools_menu, bg='#66B933')
tools_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

buttons = [{"name": "Area Calculator", "path": ".\\Tools\\Area_calculator.py"},
           {"name": "BMI Calculator", "path": ".\\Tools\\BMI_calculator.py"},
           {"name": "Temperature Converter", "path": ".\\Tools\\Temperature_converter.py"}]

create_buttons(tools_menu, tools_menu_frame, buttons, 1)

create_back_button(tools_menu)

mainloop()

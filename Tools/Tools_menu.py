from Global_functions import *

def Tools_menu():
    tools_menu = Tk()
    tools_menu.title('GAMES')
    tools_menu.geometry("600x600")
    tools_menu.configure(bg="black")

    tools_menu_frame = Frame(tools_menu, bg='#66B933')
    tools_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

    buttons = [{"name": "Area Calculator", "func_name": "Area_calculator"},
               {"name": "BMI Calculator", "func_name": "BMI_calculator"},
               {"name": "Temperature Converter", "func_name": "Temperature_converter"}]

    create_buttons(tools_menu, tools_menu_frame, buttons, 1)

    create_back_button(tools_menu)

    mainloop()

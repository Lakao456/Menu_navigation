from tkinter import *
from tkinter import messagebox
import winsound
import sys
import os

root = Tk()
root.title('Project')
root.geometry("600x600")
root.configure(bg="black")


def click_sound():
	winsound.PlaySound("Click.wav", winsound.SND_ASYNC)


def gameButton():
	click_sound()
	os.system("Game_menu.py")


def toolsButton():
	click_sound()

	def BMI_calculator():
		click_sound()
		os.system("BMI_calculator.py")

	def Area_calculator():
		click_sound()
		os.system("Area_calculator.py")

	def Temprature_converter():
		click_sound()
		os.system("Temprature_converter.py")

	tools_menu = Toplevel()
	tools_menu.title('TOOLS')
	tools_menu.geometry("600x600")
	tools_menu.configure(bg="black")

	tools_menu_frame = Frame(tools_menu, bg='#66B933')
	tools_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

	BMI_calculator = Button(tools_menu_frame, text=("BMI calculator"), bg=("grey"), font=('Autobus Bold', 25),
							command=BMI_calculator)
	BMI_calculator.place(relx=0.25, rely=0.1, relheight=0.2, relwidth=0.5)

	Area_calculator = Button(tools_menu_frame, text=("Area calculator"), bg=("grey"), font=('Autobus Bold', 25),
							 command=Area_calculator)
	Area_calculator.place(relx=0.25, rely=0.35, relheight=0.2, relwidth=0.5)

	Temprature_converter = Button(tools_menu_frame, text=("Temprature converter"), bg=("grey"),
								  font=('Autobus Bold', 25), command=Temprature_converter)
	Temprature_converter.place(relx=0.1, rely=0.6, relheight=0.2, relwidth=0.8)


def musicButton():
	click_sound()


def shopButton():
	click_sound()


def weatherButton():
	click_sound()
	os.system("WeatherApp.py")


def miscButton():
	click_sound()


main_frame = LabelFrame(root, bg='black', bd=5)
main_frame.place()

upper_frame = Frame(root, bg='#66B933', bd=5, )
upper_frame.place(relx=0.5, rely=0.1, relheight=0.2, relwidth=0.5, anchor="n")

apps_label = Label(upper_frame, text=('APPS'), font=('Autobus Bold', 50), bg="white")
apps_label.place(relheight=1, relwidth=1)

lower_frame = Frame(root, bg='#66B933', bd=5)
lower_frame.place(relx=0.5, rely=0.4, relheight=0.5, relwidth=0.8, anchor='n')

games_button = Button(lower_frame, text=("GAMES"), bg=("grey"), font=('Autobus Bold', 20), command=gameButton)
games_button.place(relx=0.1, rely=0.1, relheight=0.25, relwidth=0.35)

tools_button = Button(lower_frame, text=("TOOLS"), bg=("grey"), font=('Autobus Bold', 20), command=toolsButton)
tools_button.place(relx=0.1, rely=0.4, relheight=0.25, relwidth=0.35)

music_button = Button(lower_frame, text=("MUSIC"), bg=("grey"), font=('Autobus Bold', 20), command=musicButton)
music_button.place(relx=0.1, rely=0.7, relheight=0.25, relwidth=0.35)

shop_button = Button(lower_frame, text=("SHOP"), bg=("grey"), font=('Autobus Bold', 20), command=shopButton)
shop_button.place(relx=0.5, rely=0.1, relheight=0.25, relwidth=0.35)

weather_button = Button(lower_frame, text=("WEATHER"), bg=("grey"), font=('Autobus Bold', 20), command=weatherButton)
weather_button.place(relx=0.5, rely=0.4, relheight=0.25, relwidth=0.35)

misc_button = Button(lower_frame, text=("MISC"), bg=("grey"), font=('Autobus Bold', 20), command=miscButton)
misc_button.place(relx=0.5, rely=0.7, relheight=0.25, relwidth=0.35)

root.mainloop()

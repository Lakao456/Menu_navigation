from Global_functions import *

print('Game_menu')

game_menu = Tk()
game_menu.title('GAMES')
game_menu.geometry("600x600")
game_menu.configure(bg="black")

game_menu_frame = Frame(game_menu, bg='#66B933')
game_menu_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

buttons = [{"name": "Tic Tac Toe^", "path": ".\\Games\\TicTacToe.py"},
           {"name": "Guess the number", "path": ".\\Games\\GuessingGame.py"},
           {"name": "Dodge the blocks^", "path": ".\\Games\\DodgeTheBlocks.py"},
           {"name": "Pythons and ladders*", "path": ".\\Games\\PythonsAndLadders.py"}]

create_buttons(game_menu, game_menu_frame, buttons, 1)

create_back_button(game_menu)

mainloop()

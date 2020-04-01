import Global_Func_clone as GfuncC
from tkinter import *
from tkinter import messagebox
import time
import winsound
from functools import partial
import sys
import os
from Questions import *

global questions
global subject


def create_buttons(root, parent_frame, buttons_list, column_num=1, job='select_sub'):
    global b_height
    global text

    def set_sub(n):
        global subject
        global clear1
        subject = buttons_list[n]
        root.quit()
        root.destroy()
        print(subject)

    def button_click(n=0):
        click_sound()
        if "sub" in job.lower():
            buttons[n].config(command=set_sub(n))
        elif "ques" in job.lower():
            buttons[n].config(command=display_ques(n))

    if len(buttons_list) % 2 == 0:
        buttons_qty = len(buttons_list)
    else:
        buttons_qty = len(buttons_list) + 1

    buttons, left_i, right_i = [], 0, 0

    for i in range(len(buttons_list)):

        if "ques" in job.lower():
            text = str(i+1)
        elif "sub" in job.lower():
            text = buttons_list[i]

        if column_num == 2:
            b_height = 1.88 / buttons_qty
            if i % 2 == 0:
                left_i += 1
                buttons.append(
                    Button(parent_frame, text=text, bg="#8c8c8c", font=('Autobus Bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, i)))
                buttons[-1].place(relx=0.01,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=b_height,
                                  relwidth=0.485)
            else:
                right_i += 1
                buttons.append(
                    Button(parent_frame, text=text, bg="#8c8c8c", font=('Autobus Bold', 20),
                           relief=GROOVE,
                           command=partial(button_click, i)))
                buttons[-1].place(relx=0.505,
                                  rely=0.01 + (0.005 + b_height) * (left_i - 1),
                                  relheight=b_height,
                                  relwidth=0.485)
        elif column_num == 1:
            b_height = 1.3 / buttons_qty
            buttons.append(Button(parent_frame, text=text, bg="#8c8c8c", font=('Autobus Bold', 20),
                           relief=GROOVE,
                                  command=partial(button_click, i)))
            buttons[-1].place(relx=0.1,
                              rely=0.01 + (0.005 + b_height) * i,
                              relheight=b_height,
                              relwidth=0.8)


def click_sound():
    winsound.PlaySound(".\\Resources\\Sounds\\Click.wav", winsound.SND_ASYNC)


# def stop_watch():
#     global start_time
#     time_str = (time.time() - start_time) // 1
#     time_label.config(text=time_str)
#     time_label.after(1000, stop_watch)


def display_ques(ques_num):
    global questions
    question_number_label.config(text="Q) " + str(ques_num+1))
    question_statement = questions[subject][ques_num]["question"]
    question_statement_label.config(text=question_statement, font=('Arial', 1200//len(question_statement)))
    print(len(question_statement)//3)


play = True
while play:
    clear1 = False
    select_sub_main = Tk()
    select_sub_main.title('TESTS')
    select_sub_main.geometry('400x400')
    select_sub_main.configure(bg="#85c6dd")

    select_subject_label = Label(select_sub_main, text='Which subject do you want to chose ?', bg='#ffffff', font=('Arial', 17))
    select_subject_label.place(relx=0, rely=0.03, relheight=0.24, relwidth=1, anchor='nw')

    select_subject_frame = Frame(select_sub_main, bg='#fcfcfc')
    select_subject_frame.place(relx=0.35, rely=0.3, relheight=0.55, relwidth=0.30, anchor='nw')

    create_buttons(select_sub_main, select_subject_frame, list(questions.keys()), 1, 'select_sub')


    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit()


    select_sub_main.protocol("WM_DELETE_WINDOW", on_closing)
    select_sub_main.mainloop()


    quiz_main = Tk()
    quiz_main.title('TESTS')
    quiz_main.geometry('1000x700')
    quiz_main.configure(bg="#85c6dd")

    quiz_main_frame = Frame(quiz_main, bg='#80c1ff')
    quiz_main_frame.place(relx=0.5, rely=0.15, relheight=0.8, relwidth=0.7, anchor='n')

    question_number_label = Label(quiz_main, bg='#80c1ff', text="Q) 1", font=('Arial', 30))
    question_number_label.place(relx=0.03, rely=0.03, relheight=0.24, relwidth=0.2, anchor='nw')

    question_statement_label = Label(quiz_main, bg='#ffcccc', text=questions[subject][0]["question"], anchor='nw',
                                     font=('Arial', 1200//len(questions[subject][0]["question"])))
    question_statement_label.place(relx=0.25, rely=0.03, relheight=0.24, relwidth=0.72, anchor='nw')

    question_buttons_frame = Frame(quiz_main, bg='#fcfcfc')
    question_buttons_frame.place(relx=0.03, rely=0.3, relheight=0.6, relwidth=0.2, anchor='nw')

    options_frame = Frame(quiz_main, bg='#3c3c3c')
    options_frame.place(relx=0.25, rely=0.3, relheight=0.47, relwidth=0.72, anchor='nw')

    bottom_frame = Frame(quiz_main, bg='#0c0cff')
    bottom_frame.place(relx=0.25, rely=0.8, relheight=0.1, relwidth=0.72, anchor='nw')

    time_label = Label(bottom_frame, font=('calibri', 20, 'bold'),
                       background='purple',
                       foreground='white')
    time_label.place(relx=0.05, rely=0.1, relheight=0.8, relwidth=0.3, anchor='nw')

    create_buttons(quiz_main, question_buttons_frame, questions[subject], 2, 'select_ques')

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            sys.exit()


    quiz_main.protocol("WM_DELETE_WINDOW", on_closing)
    quiz_main.mainloop()

import time
from Questions import *


def Quiz_game():
    subject_list = [maths_question, sci_question, gk_question]

    q_time = 5  # in Minuets
    score = 0

    def correct_ans(question_list, i):
        global score
        score += 4
        question_list[i]['Given_ans'] = 'Correct'
        print('Time elapsed: ', (time.time() - start_time) // 1)

    def wrong_ans(question_list, i):
        global score
        score -= 1
        question_list[i]['Given_ans'] = 'Wrong'
        print('Time elapsed: ', (time.time() - start_time) // 1, 'seconds')

    def skip_ques(question_list, i):
        question_list[i]['Given_ans'] = 'Skipped'
        print('Time elapsed: ', (time.time() - start_time) // 1, 'seconds')

    def sub_quiz(questions_list=None):
        if questions_list is None:
            questions_list = []
        global score
        score = 0
        for i in range(len(questions_list)):
            print("----------------------------------------------------------------------------------")
            print('Question ', i + 1, ') ', questions_list[i]['question'])

            if questions_list[i]['type'] == 'mcq':
                print(questions_list[i]['options'])
                while True:
                    input_ans = input('Enter your answer (a,b,c,d):: ')
                    if input_ans.lower() in ['a', 'b', 'c', 'd']:
                        if questions_list[i]['answer'] in input_ans.lower():
                            correct_ans(questions_list, i)
                            break
                        else:
                            wrong_ans(questions_list, i)
                            break
                    else:
                        print("wrong input")


            elif questions_list[i]['type'] == 'true/false':

                given_ans = False
                while not given_ans:
                    input_ans = input('Enter your answer (true/false):: ')
                    if questions_list[i]['answer'] == 'true':

                        if 't' in input_ans.lower() or 'y' in input_ans.lower():
                            correct_ans(questions_list, i)
                            given_ans = True
                        elif 'f' in input_ans.lower() or 'n' in input_ans.lower():
                            wrong_ans(questions_list, i)
                            given_ans = True
                        else:
                            print('wrong input')

                    if questions_list[i]['answer'] == 'false':
                        if 'f' in input_ans.lower() or 'n' in input_ans.lower():
                            correct_ans(questions_list, i)
                            given_ans = True
                        elif 't' in input_ans.lower() or 'y' in input_ans.lower():
                            wrong_ans(questions_list, i)
                            given_ans = True
                        else:
                            print('wrong input')


            elif questions_list[i]['type'] == 'one word':
                input_ans = input('Enter your answer (one word):: ')

                if questions_list[i]['answer'] == input_ans.lower():
                    correct_ans(questions_list, i)
                else:
                    wrong_ans(questions_list, i)

        end_time = (time.time() - start_time) // 1
        print("Quiz Over ! \n",
              "your score is ", score,
              "\n you completed the quiz in ", end_time, "seconds")

        print("Your correctness")
        for i in range(len(questions_list)):
            try:
                print('Ans', i + 1, ')', questions_list[i]["Given_ans"])
            except:
                print("end of ans")
                break

        if input("Do you want to play again (Y/N)?:: ").lower() != 'y':
            global play
            play = False

    play = True
    while play:
        start_time = time.time()
        print("1--Maths",
              "2--Science",
              "3--General knowledge",
              sep='\n', end="\n ----------------------------- \n")
        try:
            subject = subject_list[int(input("Select a subject:: ")) - 1]
        except IndexError:
            print("Wrong input")
            continue

        sub_quiz(subject)

    print("Thank you for playing !")


Quiz_game()

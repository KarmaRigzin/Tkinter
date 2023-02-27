import tkinter as tk

# define global variables
current_question = 0
score = 0

# create main menu window
def create_main_menu():
    main_menu = tk.Tk()
    main_menu.geometry("300x200")
    main_menu.title("Quiz Game")

    # create start quiz button
    start_quiz_button = tk.Button(main_menu, text="Start Quiz", command=start_quiz)
    start_quiz_button.pack()

    # create exit button
    exit_button = tk.Button(main_menu, text="Exit", command=main_menu.quit)
    exit_button.pack()

    main_menu.mainloop()

# create quiz window
def create_quiz_window():
    quiz_window = tk.Tk()
    quiz_window.geometry("300x200")
    quiz_window.title("Quiz Game")

    # create question label
    question_label = tk.Label(quiz_window, text="Question: " + str(current_question + 1))
    question_label.pack()

    # create answer buttons
    answer_buttons = []
    for i in range(4):
        answer_button = tk.Button(quiz_window, text="Answer " + str(i+1), command=lambda i=i: check_answer(i, quiz_window))
        answer_buttons.append(answer_button)
        answer_button.pack()

    # create next button
    next_button = tk.Button(quiz_window, text="Next", command=lambda: next_question(quiz_window))
    next_button.pack()

    quiz_window.mainloop()

# create score window
def create_score_window():
    score_window = tk.Tk()
    score_window.geometry("300x200")
    score_window.title("Quiz Game")

    # create score label
    score_label = tk.Label(score_window, text="Score: " + str(score) + "/3")
    score_label.pack()

    # create return to menu button
    menu_button = tk.Button(score_window, text="Return to Menu", command=create_main_menu)
    menu_button.pack()

    # create exit button
    exit_button = tk.Button(score_window, text="Exit", command=score_window.quit)
    exit_button.pack()

    score_window.mainloop()

# start quiz
def start_quiz():
    # destroy main menu
    main_menu.destroy()

    # create quiz window
    create_quiz_window()

# ask question
def ask_question():
    # get question and answers
    question = "What is the capital of France?"
    answers = ["Paris", "Berlin", "London", "Madrid"]

    # update question and answers on the GUI
    question_label.config(text="Question: " + str(current_question + 1) + "\n" + question)
    for i in range(4):
        answer_buttons[i].config(text=answers[i])

# check answer
def check_answer(answer, quiz_window):
    # check if answer is correct
    global score
    if answer == 0:
        score += 1

    # disable answer buttons
    for button in answer_buttons:
        button.config(state="disabled")

    # enable next button
    next_button.config(state="normal")

# go to next question
def next_question(quiz_window):
    # go to next question
    global current_question
    current_question += 1

    # check if all questions have been answered
    if current_question >= 3:
        # destroy quiz window
        quiz_window.destroy()

        # create score window
        create_score_window()
    else:
        # ask next question
        ask_question()

# create main menu
create_main_menu()

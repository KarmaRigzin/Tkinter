from tkinter import *
import random

score = 0
time_left = 10

def start_game():
    global time_left
    time_left = 10
    start_button.config(state="disabled")
    update_timer()

def update_timer():
    global time_left
    if time_left > 0:
        time_left =time_left - 1
        timer_label.config(text=f"Time left: {time_left}")
        timer_label.after(1000, update_timer)
    else:
        end_game()

def end_game():
    global score
    click_me_button.config(state="disabled")
    score_label.config(text=f"Final score: {score}",width =15,bg ="white",fg ="black")
    

def score_increment():
    global score
    score += 1
    score_label.config(text=f"Score: {score}")
    click_me_button.place(x=random.randint(0, 400), y=random.randint(0, 400))

root = Tk()
root.title("Game")
root.geometry("500x500")
root.configure(bg ="green")

timer_label = Label(root, text=f"Time left: {time_left}")
timer_label.pack()

click_me_button = Button(root, text="Click me!", command=score_increment)
click_me_button.place(x=random.randint(0, 400), y=random.randint(0, 400))

score_label = Label(root, text=f"Score: {score}")
score_label.pack()

start_button = Button(root, text="Start Game", command=start_game)
start_button.pack()

root.mainloop()

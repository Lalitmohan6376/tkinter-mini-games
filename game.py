import numpy as np
import tkinter as tk
from tkinter import messagebox
import random
root = tk.Tk()
root.geometry("400x400")
root.title("Gaming Field")
root.configure(bg="#f0f8ff")

# --------Main heading---------

label = tk.Label(text="Choose your game",
                 font=("Arial",14,"bold"), bg="#4682b4", fg="white", padx=10, pady=10)
label.pack(fill="x", pady=10)

# --------Game 1 label--------

label2 = tk.Label(text="1. Number Guessing Game",
                  font=("Arial",16,"bold"), bg="#f0f8ff", fg="#2f4f4f")
label2.pack(pady=10)
def number_guessing():
    duplicate_window = tk.Toplevel(root)
    duplicate_window.title("Number Guessing Game")
    duplicate_window.geometry("500x400")
    duplicate_window.configure(bg="#fafafa")

    #-------labels--------

    text = tk.Label(duplicate_window, text="Guess a number between 1 - 100",
                    font=("Arial",13), bg="#fafafa", fg="#333")
    text.pack(pady=15)
    entry = tk.Entry(duplicate_window, width=12, font=("Arial",12), justify="center", bd=3, relief="solid")
    entry.pack(pady=10, ipady=5)

    #------play game function-------

    random_guess = np.random.randint(1,101)
    def call():
        try:
            user_value = int(entry.get())
            differnce = abs(random_guess-user_value)
            if user_value == random_guess:
                output_label.config(text=" Congratulations! You win the game", fg="green")
            elif differnce >= 80:
                output_label.config(text=" Too Far", fg="red")
            elif differnce <= 50:
                output_label.config(text="Medium ", fg="orange")
            elif differnce <= 79:
                output_label.config(text="Far", fg="blue")
        except ValueError:
            output_label.config(text="Enter Number", fg="blue")

    # ---------Submit button----------

    submit_button = tk.Button(duplicate_window, text="Guess",
                              command=call, font=("Arial",12,"bold"),
                              bg="#4682b4", fg="white", padx=20, pady=5, relief="raised")
    submit_button.pack(pady=15)

    #-----Output label------

    output_label = tk.Label(duplicate_window, text="", font=("Arial",13,"bold"),
                            bg="#fafafa", fg="#333")
    output_label.pack(pady=10)

#------button-------

btn1 = tk.Button(root, text="Play Game 1", command=number_guessing,
                 font=("Arial",12,"bold"), bg="#34c834", fg="white",
                 padx=15, pady=5, relief="raised")
btn1.pack(pady=10)

# -----------Game 2 label-----------
label3 = tk.Label(text="2. Simple Rock,Paper,Scissor", font=("Arial",16,"bold"),
                  bg="#f0f8ff", fg="#2f4f4f")
label3.pack(pady=10)

#----------second window-----------

def second_window():
    global ans
    global second
    second = tk.Toplevel(root)
    second.title("Simple Quiz Game")
    second.geometry("500x400")
    text = tk.Label(second, text="Rock,Paper,Scissors",
                    font=("Arial",13), bg="#fafafa", fg="#333")
    text.pack(pady=15)

    #-------parent frame-------

    btn_frame = tk.Frame(second,width=900,height=800)
    btn_frame.pack()

    frame1 = tk.Frame(btn_frame)
    frame1.pack(side=tk.LEFT,padx=20)
    btn_rock = tk.Button(frame1,text="Rock",width=10,font=("Arial",12,"bold"), bg="#ffa500", fg="white",
                 padx=15, pady=5, relief="raised",command=lambda:on_click("Rock"))
    btn_rock.pack(pady=20)

    frame2 = tk.Frame(btn_frame)
    frame2.pack(side=tk.LEFT,padx=20)
    btn_paper = tk.Button(frame2,text="Paper",width=10,font=("Arial",12,"bold"), bg="#ffa500", fg="white",
                 padx=15, pady=5, relief="raised",command=lambda:on_click("Paper"))
    btn_paper.pack(pady=20)

    frame3 = tk.Frame(btn_frame)
    frame3.pack(side=tk.LEFT,padx=20)
    btn_scissor = tk.Button(frame3,text="Scissor",width=10,font=("Arial",12,"bold"), bg="#ffa500", fg="white",
                 padx=15, pady=5, relief="raised",command=lambda:on_click("Scissor"))
    btn_scissor.pack(pady=20)

    ans = tk.Label(second, text="", font=("Arial", 12,"bold"))
    ans.pack(pady=20)

#---------second window game function------------

def on_click(value):
    dsa = ["Rock","Paper","Scissor"]
    random_choice = random.choice(dsa)
    print(random_choice)
    
    if value == random_choice:
        result = "Draw You"
    elif value == "Rock" and random_choice == "Scissor":
        result = "You Wins"
    elif value == "Paper" and random_choice == "Rock":
        result = "You Wins"
    elif value == "Scissor" and random_choice == "Paper":
        result = "You Wins"
    else:
        result = "You Lose!Try Again"
        
    ans.config(text=result)


btn2 = tk.Button(root, text=" Play Game 2",
                 font=("Arial",12,"bold"), bg="#ffa500", fg="white",
                 padx=15, pady=5, relief="raised",command=second_window)
btn2.pack(pady=10)
root.mainloop()

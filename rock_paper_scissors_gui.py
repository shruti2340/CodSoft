import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]
player_score = 0
computer_score = 0
ties = 0

def play(user_choice):
    global player_score, computer_score, ties

    computer_choice = random.choice(choices)

    # Decide result
    if user_choice == computer_choice:
        result = "It's a Tie!"
        ties += 1
        color = "#3399FF"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        player_score += 1
        color = "#33cc33"
    else:
        result = "Computer Wins!"
        computer_score += 1
        color = "#ff3333"

    result_label.config(text=f"You: {user_choice}  |  Computer: {computer_choice}\n{result}", fg=color)
    animate_result()

   
    score_label.config(text=f"Score\nYou: {player_score}   Computer: {computer_score}   Ties: {ties}")

def animate_result():
    """Flashes the result label for a fun effect."""
    current_color = result_label.cget("fg")
    result_label.after(100, lambda: result_label.config(fg="white"))
    result_label.after(200, lambda: result_label.config(fg=current_color))

def reset_game():
    global player_score, computer_score, ties
    player_score = 0
    computer_score = 0
    ties = 0
    result_label.config(text="Make your move!", fg="white")
    score_label.config(text="Score\nYou: 0   Computer: 0   Ties: 0")

root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("500x500")
root.configure(bg="#1e1e2f") 

title = tk.Label(root, text="Rock-Paper-Scissors", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2f")
title.pack(pady=20)

result_label = tk.Label(root, text="Make your move!", font=("Arial", 16, "bold"), fg="white", bg="#1e1e2f")
result_label.pack(pady=30)

score_label = tk.Label(root, text="Score\nYou: 0   Computer: 0   Ties: 0", font=("Arial", 16, "bold"), fg="#FFD700", bg="#1e1e2f")
score_label.pack(pady=20)

button_frame = tk.Frame(root, bg="#1e1e2f")
button_frame.pack(pady=30)

def on_enter(e):
    e.widget["background"] = "#4444aa"

def on_leave(e):
    e.widget["background"] = "#2e2e4f"


for choice in choices:
    btn = tk.Button(button_frame, text=choice, width=12, height=2, font=("Arial", 14, "bold"),
                    bg="#2e2e4f", fg="white", activebackground="#6666ff", relief="flat", bd=0,
                    command=lambda c=choice: play(c))
    btn.pack(side="left", padx=15)
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)


reset_btn = tk.Button(root, text="Reset Game", width=14, font=("Arial", 12, "bold"),
                      bg="#ff4444", fg="white", activebackground="#ff7777", relief="flat", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()

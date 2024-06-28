import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image,ImageTk

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or (user_choice == "paper" and computer_choice == "rock") or (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    result = check_winner(user_choice, computer_choice)
    messagebox.showinfo("Result", f"Computer chose: {computer_choice}\n{result}")

def resize_image(image, width, height):
    image = image.resize((width, height))
    return image

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("600x600")

rock = Image.open("rock.png")
rock = resize_image(rock, 100, 100)
rock = ImageTk.PhotoImage(rock)

scissor = Image.open("scissor.png")
scissor = resize_image(scissor, 100, 100)
scissor = ImageTk.PhotoImage(scissor)

paper = Image.open("paper.png")
paper = resize_image(paper, 100, 100)
paper = ImageTk.PhotoImage(paper)

rock_btn = tk.Button(root, text="Rock", command=lambda: play_game("rock"), image=rock, compound="top", font=("Arial", 10), background="lightblue")
rock_btn.pack()

paper_btn = tk.Button(root, text="Paper", command=lambda: play_game("paper"), image=paper, compound="top", font=("Arial", 10), background="lightblue")
paper_btn.pack()

scissors_btn = tk.Button(root, text="Scissors", command=lambda: play_game("scissors"), image=scissor, compound="top", font=("Arial", 10), background="lightblue")
scissors_btn.pack()

root.mainloop()

# quiz_game.py
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What color is the sky on a clear day?": "Blue"
}

score = 0
for question, answer in questions.items():
    user_answer = input(question + " ")
    if user_answer.strip().lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {answer}")

print(f"Your score: {score}/{len(questions)}")
print(f"Your score: {score}/{len(questions)}")
print(f"Percentage: {(score / len(questions)) * 100:.2f}%")

import random

question_items = list(questions.items())
random.shuffle(question_items)

for question, answer in question_items:
    ...

import random

# Define correct answers
questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What color is the sky on a clear day?": "Blue"
}

# Define multiple choice options
options = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "What is 2 + 2?": ["3", "4", "5", "6"],
    "What color is the sky on a clear day?": ["Blue", "Green", "Red", "Yellow"]
}

# Initialize score
score = 0

# Shuffle question order
question_list = list(questions.keys())
random.shuffle(question_list)

# Quiz loop
for question in question_list:
    print("\n" + question)
    choices = options[question][:]
    random.shuffle(choices)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    
    try:
        user_choice = int(input("Enter the number of your answer: "))
        if 1 <= user_choice <= len(choices):
            selected = choices[user_choice - 1]
            if selected.lower() == questions[question].lower():
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer is {questions[question]}")
        else:
            print("⚠️ Invalid choice. Skipping question.")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number.")

# Final score
print(f"\nYour final score: {score}/{len(questions)}")


# gui_quiz_game.py
import tkinter as tk
from tkinter import messagebox
import random

# Quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "What color is the sky on a clear day?",
        "options": ["Blue", "Green", "Red", "Yellow"],
        "answer": "Blue"
    },
    {
        "question": "Which animal is known as man's best friend?",
        "options": ["Cat", "Dog", "Horse", "Rabbit"],
        "answer": "Dog"
    },
    {
        "question": "What planet do we live on?",
        "options": ["Mars", "Venus", "Earth", "Jupiter"],
        "answer": "Earth"
    }
]

# Shuffle questions
random.shuffle(quiz_data)

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")
        self.score = 0
        self.q_index = 0

        self.question_label = tk.Label(root, text="", wraplength=350, font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []
        for _ in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="", font=("Arial", 12), wraplength=350)
            btn.pack(anchor="w", padx=20)
            self.option_buttons.append(btn)

        self.submit_btn = tk.Button(root, text="Submit", command=self.check_answer)
        self.submit_btn.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.q_index < len(quiz_data):
            current = quiz_data[self.q_index]
            self.question_label.config(text=current["question"])
            self.var.set(None)
            options = current["options"]
            random.shuffle(options)
            for i in range(4):
                self.option_buttons[i].config(text=options[i], value=options[i])
        else:
            messagebox.showinfo("Quiz Completed", f"Your score: {self.score}/{len(quiz_data)}")
            self.root.quit()

    def check_answer(self):
        selected = self.var.get()
        correct = quiz_data[self.q_index]["answer"]
        if selected == correct:
            self.score += 1
        self.q_index += 1
        self.load_question()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

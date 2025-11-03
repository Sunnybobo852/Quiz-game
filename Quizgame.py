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

options = {
    "What is the capital of France?": ["Paris", "London", "Berlin", "Madrid"],
    "What is 2 + 2?": ["3", "4", "5", "6"],
    "What color is the sky on a clear day?": ["Blue", "Green", "Red", "Yellow"]
}

for question in questions:
    print(question)
    choices = options[question]
    random.shuffle(choices)
    for i, choice in enumerate(choices):
        print(f"{i + 1}. {choice}")
    user_choice = input("Enter the number of your answer: ")
    if choices[int(user_choice) - 1].lower() == questions[question].lower():
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer is {questions[question]}")

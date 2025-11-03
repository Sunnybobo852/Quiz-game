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

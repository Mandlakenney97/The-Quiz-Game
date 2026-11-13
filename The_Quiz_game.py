"""Multiple-choice quiz game.

Run: python quiz_game.py
Concepts: lists of dictionaries, loops, random.shuffle, scoring, f-strings.
Tip: add your own questions to the QUESTIONS list!
"""
import random

QUESTIONS = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "def", "function", "define"],
        "answer": 2,
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["2", "3", "4", "1"],
        "answer": 2,
    },
    {
        "question": "Which data type stores key-value pairs?",
        "options": ["list", "tuple", "dictionary", "set"],
        "answer": 3,
    },
    {
        "question": "What symbol starts a comment in Python?",
        "options": ["//", "#", "--", "/*"],
        "answer": 2,
    },
    {
        "question": "What is the output of print(type(3.14))?",
        "options": ["<class 'int'>", "<class 'str'>", "<class 'float'>", "<class 'num'>"],
        "answer": 3,
    },
    {
        "question": "Which loop repeats while a condition is True?",
        "options": ["for", "while", "repeat", "loop"],
        "answer": 2,
    },
]


def ask_question(number, total, item):
    print(f"\nQuestion {number}/{total}: {item['question']}")
    for index, option in enumerate(item["options"], start=1):
        print(f"  {index}) {option}")

    while True:
        try:
            choice = int(input("Your answer (1-4): "))
            if 1 <= choice <= 4:
                break
        except ValueError:
            pass
        print("Please enter a number from 1 to 4.")

    if choice == item["answer"]:
        print("Correct!")
        return True
    print(f"Wrong. The answer was: {item['options'][item['answer'] - 1]}")
    return False


def grade_message(percent):
    if percent == 100:
        return "Perfect score! Amazing!"
    if percent >= 70:
        return "Great job!"
    if percent >= 40:
        return "Not bad, keep practising."
    return "Keep studying, you'll get there!"


def main():
    print("=== PYTHON QUIZ ===")
    questions = QUESTIONS[:]
    random.shuffle(questions)
    score = 0

    for number, item in enumerate(questions, start=1):
        if ask_question(number, len(questions), item):
            score += 1

    percent = score / len(questions) * 100
    print(f"\nYou scored {score}/{len(questions)} ({percent:.0f}%)")
    print(grade_message(percent))


if __name__ == "__main__":
    main()

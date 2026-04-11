# Quiz game

questions = (
    "How many elements are in the periodic table?: ",
    "Which animal lays the most eggs?: ",
    "What is the most abundant gas in Earth's atmosphere?: ",
)

options = (
    ("A. 116", "B. 117", "C: 118"),
    ("A. Whale", "B. Crocodile", "C: Ostrich"),
    ("A. Nitrogen", "B. Oxygeb", "C: Carbon"),
)

answers = ("C", "C", "A")

guesses = []

score = 0

question_num = 0

for question in questions:
    print("-----------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, D): ")
    guesses.append(guess)
    print(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print(f"Incorrect")
    question_num += 1

print("-----------")
print(f"Your scored {score} points!")

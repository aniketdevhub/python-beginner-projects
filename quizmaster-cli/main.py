# --------------------------------------------------------
# Simple Python Quiz Game (9 Questions)
# --------------------------------------------------------

# 1. Welcome the player
print("Welcome to the General Knowledge Quiz!")
print("Let's see how many questions you can get right.")
print("Please type your answers carefully.\n")

# 2. Initialize the player's score
score = 0

# --- QUESTION 1 ---
print("Question 1: What is the capital of France?")
print("A) Berlin")
print("B) Paris")
print("C) Rome")
answer1 = input("Your answer (A, B, or C): ")

if answer1 == "B" or answer1 == "b" or answer1 == "Paris" or answer1 == "paris":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was B (Paris).\n")

# --- QUESTION 2 ---
print("Question 2: Which data type is used for text in Python?")
print("A) integer")
print("B) float")
print("C) string")
answer2 = input("Your answer (A, B, or C): ")

if answer2 == "C" or answer2 == "c" or answer2 == "string":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was C (string).\n")

# --- QUESTION 3 ---
print("Question 3: What is the result of 5 + 3 * 2 in Python?")
print("A) 16")
print("B) 11")
print("C) 10")
answer3 = input("Your answer (A, B, or C): ")

if answer3 == "B" or answer3 == "b" or answer3 == "11":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The answer is 11 because multiplication happens first.\n")

# --- QUESTION 4 ---
print("Question 4: What is the largest planet in our solar system?")
print("A) Earth")
print("B) Mars")
print("C) Jupiter")
answer4 = input("Your answer (A, B, or C): ")

if answer4 == "C" or answer4 == "c" or answer4 == "Jupiter" or answer4 == "jupiter":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was C (Jupiter).\n")

# --- QUESTION 5 ---
print("Question 5: Which symbol is used to write a comment in Python?")
print("A) #")
print("B) //")
print("C) /*")
answer5 = input("Your answer (A, B, or C): ")

if answer5 == "A" or answer5 == "a":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was A (#).\n")

# --- QUESTION 6 ---
print("Question 6: How many seconds are there in one minute?")
print("A) 50")
print("B) 60")
print("C) 100")
answer6 = input("Your answer (A, B, or C): ")

if answer6 == "B" or answer6 == "b" or answer6 == "60":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was B (60).\n")

# --- QUESTION 7 ---
print("Question 7: What does the 'print' function do in Python?")
print("A) It prints text onto a physical piece of paper.")
print("B) It displays text on the screen.")
print("C) It deletes a file.")
answer7 = input("Your answer (A, B, or C): ")

if answer7 == "B" or answer7 == "b":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was B (It displays text on the screen).\n")

# --- QUESTION 8 ---
print("Question 8: Which animal is known as the King of the Jungle?")
print("A) Elephant")
print("B) Tiger")
print("C) Lion")
answer8 = input("Your answer (A, B, or C): ")

if answer8 == "C" or answer8 == "c" or answer8 == "Lion" or answer8 == "lion":
    print("Correct!\n")
    score = score + 1
else:
    print("Incorrect. The correct answer was C (Lion).\n")

# --- QUESTION 9 ---
print("Question 9: What is the correct way to start an 'if' statement in Python?")
print("A) if x == 5:")
print("B) if x == 5 then")
print("C) if x = 5:")
answer9 = input("Your answer (A, B, or C): ")

if answer9 == "A" or answer9 == "a":
    print("Correct!\n")
    score = score + 1
else:
    print(
        "Incorrect. Remember, we use a colon and double equal signs for comparison. The answer was A.\n"
    )

# --- GAME OVER / TOTAL SCORE ---
print("--- Game Over ---")
print("Thank you for playing.")
print("Your final score is: " + str(score) + " out of 9.")

# Give feedback based on their score
if score == 9:
    print("Perfect score! Excellent job.")
elif score >= 5:
    print("Good job! You passed the quiz.")
else:
    print("Good try! Keep studying and try again.")

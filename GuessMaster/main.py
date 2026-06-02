import random


def play_game(max_number, max_attempts):
    secret_number = random.randint(1, max_number)
    attempts = 0

    print(f"\nGuess a number between 1 and {max_number}")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too Low!")

        elif guess > secret_number:
            print("Too High!")

        else:
            print(f"\n🎉 Congratulations!")
            print(f"You guessed the number in {attempts} attempts.")
            return

        print(f"Attempts Left: {max_attempts - attempts}\n")

    print(f"\n💀 Game Over!")
    print(f"The correct number was {secret_number}")


def start_game():
    print("=" * 35)
    print("   NUMBER GUESSING GAME")
    print("=" * 35)

    while True:
        print("\nChoose Difficulty:")
        print("1. Easy   (1-10, 5 Attempts)")
        print("2. Medium (1-50, 7 Attempts)")
        print("3. Hard   (1-100, 10 Attempts)")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            play_game(10, 5)

        elif choice == "2":
            play_game(50, 7)

        elif choice == "3":
            play_game(100, 10)

        elif choice == "4":
            print("\nThanks for playing!")
            break

        else:
            print("Invalid Choice!")

        play_again = input("\nPlay Again? (y/n): ").lower()

        if play_again != "y":
            print("\nThanks for playing!")
            break


start_game()
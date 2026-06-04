import random
import string


def generate_password(length, upper, lower, numbers, symbols):
    characters = ""

    if upper:
        characters += string.ascii_uppercase

    if lower:
        characters += string.ascii_lowercase

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


def main():
    print("=" * 40)
    print("      SecurePass Generator")
    print("=" * 40)

    while True:
        try:
            length = int(input("\nEnter password length: "))

            upper = input("Include uppercase letters? (y/n): ").lower() == "y"
            lower = input("Include lowercase letters? (y/n): ").lower() == "y"
            numbers = input("Include numbers? (y/n): ").lower() == "y"
            symbols = input("Include special characters? (y/n): ").lower() == "y"

            password = generate_password(length, upper, lower, numbers, symbols)

            if password is None:
                print("\nSelect at least one character type!")
                continue

            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (y/n): ").lower()

            if again != "y":
                print("\nThank you for using SecurePass Generator!")
                break

        except ValueError:
            print("Please enter a valid number.")


main()

import random
import time

easy_paragraphs = [
    "Python is a versatile programming language that helps developers build applications, automate tasks, and solve real world problems efficiently every day.",
    "Learning programming requires patience and practice because every small project teaches valuable concepts and improves logical thinking skills over time.",
    "Web development combines creativity and coding to create websites that provide useful information and enjoyable experiences for users around the world.",
]

medium_paragraphs = [
    "Artificial intelligence is transforming industries by automating repetitive tasks, improving decision making processes, and enabling innovative solutions across many different sectors today.",
    "Building projects is one of the most effective ways to learn programming because practical experience strengthens understanding and develops problem solving abilities.",
    "Developers frequently spend significant time debugging applications because identifying and resolving errors is essential for creating reliable and efficient software products.",
]

hard_paragraphs = [
    "Technology continues to evolve rapidly, requiring developers to continuously learn new frameworks, programming languages, and industry practices to remain competitive and adaptable.",
    "Creating an intuitive user interface requires thoughtful consideration of typography, spacing, navigation patterns, accessibility standards, and overall visual consistency throughout the application.",
    "Successful software engineering involves collaboration, communication, testing, documentation, and continuous improvement to deliver high quality solutions that meet user expectations.",
]


def calculate_accuracy(original, typed):
    correct = 0

    for i in range(min(len(original), len(typed))):
        if original[i] == typed[i]:
            correct += 1

    return (correct / len(original)) * 100


def typing_test():

    print("\n===== Typing Performance Analyzer =====\n")

    print("1. Easy")
    print("2. Medium")
    print("3. Hard")

    choice = input("\nChoose difficulty: ")

    if choice == "1":
        paragraph = random.choice(easy_paragraphs)

    elif choice == "2":
        paragraph = random.choice(medium_paragraphs)

    elif choice == "3":
        paragraph = random.choice(hard_paragraphs)

    else:
        print("Invalid choice!")
        return

    print("\nType the following paragraph:\n")
    print(paragraph)

    input("\nPress Enter to start...")

    start_time = time.time()

    typed_text = input("\nStart Typing:\n\n")

    end_time = time.time()

    time_taken = end_time - start_time

    word_count = len(typed_text.split())

    wpm = (word_count / time_taken) * 60

    accuracy = calculate_accuracy(paragraph, typed_text)

    print("\n===== Results =====")
    print(f"Time Taken : {time_taken:.2f} seconds")
    print(f"Words Typed: {word_count}")
    print(f"WPM        : {wpm:.2f}")
    print(f"Accuracy   : {accuracy:.2f}%")
    print("===================\n")


while True:
    typing_test()

    again = input("Try Again? (y/n): ").lower()

    if again != "y":
        print("\nThank you for using Typing Performance Analyzer!")
        break

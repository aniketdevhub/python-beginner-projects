import time

def countdown(seconds):
    while seconds > 0:
        minutes, remaining_seconds = divmod(seconds, 60)
        print(f"{minutes:02d}:{remaining_seconds:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

    print("\n⏰ Time's Up!")

try:
    total_seconds = int(input("Enter time in seconds: "))
    countdown(total_seconds)
except ValueError:
    print("Please enter a valid number.")
# Multi-Unit Converter
# Beginner Friendly Python Project

def length_converter():
    km = float(input("Enter kilometers: "))
    print(f"Meters: {km * 1000}")


def weight_converter():
    kg = float(input("Enter kilograms: "))
    print(f"Grams: {kg * 1000}")


def temperature_converter():
    c = float(input("Enter temperature in Celsius: "))
    f = (c * 9/5) + 32
    print(f"Fahrenheit: {f}")


def area_converter():
    sq_m = float(input("Enter area in square meters: "))
    print(f"Square Feet: {sq_m * 10.764}")


def volume_converter():
    liters = float(input("Enter liters: "))
    print(f"Milliliters: {liters * 1000}")


def speed_converter():
    kmh = float(input("Enter speed in km/h: "))
    print(f"m/s: {kmh * 0.2778}")


def time_converter():
    hours = float(input("Enter hours: "))
    print(f"Minutes: {hours * 60}")


def currency_converter():
    amount = float(input("Enter amount in USD: "))
    rate = 83  # Example exchange rate
    print(f"INR: {amount * rate}")


while True:
    print("\n===== MULTI UNIT CONVERTER =====")
    print("1. Length (KM → M)")
    print("2. Weight (KG → G)")
    print("3. Temperature (C → F)")
    print("4. Area (m² → ft²)")
    print("5. Volume (L → mL)")
    print("6. Speed (km/h → m/s)")
    print("7. Time (Hours → Minutes)")
    print("8. Currency (USD → INR)")
    print("9. Exit")

    choice = input("Choose an option (1-9): ")

    if choice == "1":
        length_converter()
    elif choice == "2":
        weight_converter()
    elif choice == "3":
        temperature_converter()
    elif choice == "4":
        area_converter()
    elif choice == "5":
        volume_converter()
    elif choice == "6":
        speed_converter()
    elif choice == "7":
        time_converter()
    elif choice == "8":
        currency_converter()
    elif choice == "9":
        print("Thank you for using Multi Unit Converter!")
        break
    else:
        print("Invalid choice. Try again.")
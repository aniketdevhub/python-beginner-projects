class HealthTracker:

    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight

    def calculate_bmi(self):
        bmi = self.weight / ((self.height / 100) ** 2)
        return round(bmi, 2)

    def bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal Weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"

    def water_intake(self):
        water = self.weight * 35
        return water

    def calculate_bmr(self):
        if self.gender.lower() == "male":
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5
        else:
            bmr = 10 * self.weight + 6.25 * self.height - 5 * self.age - 161

        return round(bmr, 2)

    def show_report(self):
        print("\n" + "=" * 40)
        print("      HEALTH REPORT")
        print("=" * 40)

        print(f"Name       : {self.name}")
        print(f"Age        : {self.age}")
        print(f"Gender     : {self.gender}")
        print(f"Height     : {self.height} cm")
        print(f"Weight     : {self.weight} kg")

        print("\nHealth Statistics")
        print("-" * 40)
        print(f"BMI                : {self.calculate_bmi()}")
        print(f"BMI Category       : {self.bmi_category()}")
        print(f"Daily Water Intake : {self.water_intake()} ml")
        print(f"BMR                : {self.calculate_bmr()} calories/day")

        print("=" * 40)


while True:

    print("\n===== HEALTH TRACKER =====")
    print("1. Generate Health Report")
    print("2. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender (Male/Female): ")
        height = float(input("Enter Height (cm): "))
        weight = float(input("Enter Weight (kg): "))

        user = HealthTracker(name, age, gender, height, weight)

        user.show_report()

    elif choice == "2":
        print("Thank you for using Health Tracker!")
        break

    else:
        print("Invalid Choice!")

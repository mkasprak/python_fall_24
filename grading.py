# BMI_calculator assignment
# Start functions to convert variables
def calculate_kilograms(WEIGHT):
    global KILOGRAMS
    KILOGRAMS = WEIGHT*0.45359
    return KILOGRAMS


def calculate_meters(HEIGHT):
    global METERS
    METERS = HEIGHT*0.0254
    return HEIGHT

# Calculate BMI


def calculate_BMI():
    global BMI
    BMI = KILOGRAMS/(METERS*METERS)
# Start the main part of the program


def main():
    print("Hello user I am a BMI caluclator.")
    HEIGHT = float(input("Please enter your height in inches: "))
    WEIGHT = float(input("Please enter your weight in pounds: "))
    calculate_kilograms(WEIGHT)
    calculate_meters(HEIGHT)
    calculate_BMI()
    print(f"Your BMI is {BMI:.2f}.")
    if BMI < 18.5:
        print("You are in the underweight category")
    elif BMI < 24.9:
        print("You are in the normal weight category.")
    elif BMI < 29.9:
        print("You are in the overweight category.")
    elif BMI >= 30:
        print("You are in the obese category.")


main()

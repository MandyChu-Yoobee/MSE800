"""BMI (Body Mass Index) Calculator.

A simple command-line application that asks the user for their weight and
height, then calculates and classifies their Body Mass Index.
"""


def get_positive_number(prompt):
    """Prompt the user until they enter a positive number, then return it.

    Args:
        prompt (str): The message shown to the user before reading input.

    Returns:
        float: The positive number entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_bmi(weight_kg, height_m):
    """Calculate BMI from weight and height.

    Args:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in metres.

    Returns:
        float: The Body Mass Index (kg/m^2).
    """
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Return the WHO weight category for a given BMI value.

    Args:
        bmi (float): The Body Mass Index.

    Returns:
        str: The weight category label.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25.0:
        return "Normal weight"
    elif bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def main():
    """Entry point: collect input, compute BMI, and display the result."""
    print("=== BMI Calculator ===")

    # Collect and validate the user's measurements.
    weight = get_positive_number("Enter your weight in kilograms: ")
    height = get_positive_number("Enter your height in metres: ")

    # Compute and classify the BMI.
    bmi = calculate_bmi(weight, height)
    category = classify_bmi(bmi)

    print(f"\nYour BMI is {bmi:.2f} ({category}).")


if __name__ == "__main__":
    main()

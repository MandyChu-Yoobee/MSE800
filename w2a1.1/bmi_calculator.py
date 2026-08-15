"""BMI (Body Mass Index) Calculator — OOP version.

An object-oriented rewrite of the W1-A4 BMI calculator. The logic is
organised into a single class that exposes its behaviour through methods.

Note: as required by the activity, no ``__init__`` constructor is used —
the class holds no per-instance state, so its methods are ``@staticmethod``
(and one ``@classmethod`` entry point) rather than instance methods.
"""


class BMICalculator:
    """A collection of methods for calculating and classifying BMI."""

    @staticmethod
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

    @staticmethod
    def calculate_bmi(weight_kg, height_m):
        """Calculate BMI from weight and height.

        Args:
            weight_kg (float): Weight in kilograms.
            height_m (float): Height in metres.

        Returns:
            float: The Body Mass Index (kg/m^2).
        """
        return weight_kg / (height_m ** 2)

    @staticmethod
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

    @classmethod
    def run(cls):
        """Entry point: collect input, compute BMI, and display the result."""
        print("=== BMI Calculator ===")

        # Collect and validate the user's measurements.
        weight = cls.get_positive_number("Enter your weight in kilograms: ")
        height = cls.get_positive_number("Enter your height in metres: ")

        # Compute and classify the BMI.
        bmi = cls.calculate_bmi(weight, height)
        category = cls.classify_bmi(bmi)

        print(f"\nYour BMI is {bmi:.2f} ({category}).")


def main():
    """Launch the BMI calculator."""
    BMICalculator.run()


if __name__ == "__main__":
    main()

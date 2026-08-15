"""BMI (Body Mass Index) Calculator — optimized version.

Optimized from the reference ``Activity_1-4`` code. The original used ``this``
as the name of a method's first parameter, which is JavaScript terminology.
In Python that reference is written as ``self`` (a convention, not a keyword).

Key changes:
- Renamed ``this`` -> ``self`` (the idiomatic Python name).
- Added an ``__init__`` constructor so the object's attributes are declared
  up front instead of appearing only after ``get_data`` runs.
- Tightened the helper functions (``is_float`` / ``input_float``) into clean,
  self-contained functions that don't touch the object at all.
"""


def is_float(value):
    """Return ``value`` as a float, or ``None`` if it can't be converted.

    Args:
        value: The value to convert.

    Returns:
        float or None: The converted number, or ``None`` on failure.
    """
    try:
        return float(value)
    except (ValueError, TypeError):
        return None


def input_float(prompt):
    """Prompt the user until they enter a decimal number, then return it.

    Args:
        prompt (str): The message shown before reading input.

    Returns:
        float: The number entered by the user.
    """
    while True:
        value = is_float(input(prompt))
        if value is not None:
            return value
        print("Please enter a number")


class BMICalculator:
    """Calculate and report a person's Body Mass Index."""

    def __init__(self):
        """Create a calculator with no measurements recorded yet."""
        self.weight_kg = None
        self.height_m = None

    def get_data(self):
        """Ask the user for weight (kg) and height (cm), storing height in m."""
        self.weight_kg = input_float("Please enter your weight in kilograms: ")
        self.height_m = input_float("Please enter your height in centimetres: ") / 100

    def calculate(self):
        """Calculate and return the BMI, rounded to two decimal places."""
        return round(self.weight_kg / (self.height_m * self.height_m), 2)


def main():
    """Entry point: collect the user's measurements and report their BMI."""
    print("\n", "=" * 42, "\n")
    print("Hello, let's calculate your BMI.")

    calc = BMICalculator()
    print()
    calc.get_data()
    bmi = calc.calculate()
    print(f"Your BMI is {bmi}")
    print("\n", "=" * 42, "\n")


if __name__ == "__main__":
    main()

def fibonacci_series(n):
    """Return a list of all Fibonacci numbers up to n (inclusive)."""
    series = []
    a, b = 0, 1
    while a <= n:
        series.append(a)
        a, b = b, a + b
    return series


def factorial(n):
    """Return the factorial of n (n!)."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def main():
    n = int(input("Enter a number (N): "))

    print(f"Fibonacci series up to {n}:")
    print(" ".join(str(x) for x in fibonacci_series(n)))

    print(f"Factorial of {n}: {factorial(n)}")


if __name__ == "__main__":
    main()

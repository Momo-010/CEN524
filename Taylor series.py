def taylor_series_sum(F, a, x):
    result = 0
    term = 1
    factorial = 1

    for i in range(len(F)):
        if i > 0:
            term *= (x - a)
            factorial *= i
        result += F[i] * term / factorial

    return result


if __name__ == "__main__":
    # Get number of terms
    n = int(input("Enter the number of terms (n): "))

    # Get derivatives f(a), f'(a), ..., f^n(a)
    print(f"Enter the {n} derivative values at a (f(a), f'(a), ..., f^{n-1}(a)):")
    F = []
    for i in range(n):
        val = float(input(f"f^{i}(a): "))
        F.append(val)

    # Get the value of 'a'
    a = float(input("Enter the value of a: "))

    # Get the value of 'x'
    x = float(input("Enter the value of x: "))

    # Calculate and display the result
    result = taylor_series_sum(F, a, x)
    print(f"\nApproximated value of f({x}) using Taylor series: {result}")

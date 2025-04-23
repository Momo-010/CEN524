def factorial(n):
    result = 1  # Initialize the result to 1

    # If n is 0 or 1, return 1 as 0! = 1 and 1! = 1
    if n == 0 or n == 1:
        return result

    # Calculate factorial using a loop
    for i in range(2, n + 1):
        result *= i

    return result


if __name__ == "__main__":
    # Get user input for the integer n
    n = int(input("Enter a non-negative integer to calculate its factorial: "))

    # Check if the input is valid (non-negative)
    if n < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        # Call the factorial function and display the result
        print(f"The factorial of {n} is {factorial(n)}")

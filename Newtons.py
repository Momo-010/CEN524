def newton_reciprocal(N, x0=0.1, tolerance=1e-6, max_iterations=10):
    x = x0
    for i in range(max_iterations):
        # Apply Newton's formula
        x_next = x * (2 - x * N)
        
        # Check for convergence
        if abs(x_next - x) < tolerance:
            break
        
        x = x_next  # Update for next iteration
    
    return x

# Input from user
N = float(input("Enter the number N to calculate its reciprocal: "))
x0 = float(input("Enter the initial guess (x0), recommended value is 0.1: "))
tolerance = float(input("Enter the tolerance for convergence (e.g., 1e-6): "))
max_iterations = int(input("Enter the maximum number of iterations (e.g., 10): "))

# Call the function with user inputs
result = newton_reciprocal(N, x0, tolerance, max_iterations)

# Display results
print(f"Approximation of 1/{N} is: {result}")
print(f"True reciprocal of {N} is: {1/N}")

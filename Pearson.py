import math

def pearson_correlation(x, y):
    # Check if the length of x and y are the same
    if len(x) != len(y):
        return "Error: The lists x and y must have the same length."
    
    n = len(x)  # Number of data points
    
    # Calculate the required sums
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(i**2 for i in x)
    sum_y_squared = sum(i**2 for i in y)
    sum_xy = sum(x[i] * y[i] for i in range(n))
    
    # Calculate the numerator
    numerator = n * sum_xy - sum_x * sum_y
    
    # Calculate the denominator
    denominator = math.sqrt((n * sum_x_squared - sum_x**2) * (n * sum_y_squared - sum_y**2))
    
    # Check if the denominator is zero (which could happen if all values in x or y are constant)
    if denominator == 0:
        return "Error: Denominator is zero, correlation cannot be calculated."
    
    # Calculate Pearson's correlation coefficient
    r = numerator / denominator
    return r

# Example usage
if __name__ == "__main__":
    # Get user input for the two variables
    x = list(map(float, input("Enter values for x (separated by space): ").split()))
    y = list(map(float, input("Enter values for y (separated by space): ").split()))
    
    # Call the function and display the result
    correlation = pearson_correlation(x, y)
    print(f"Pearson's Correlation Coefficient: {correlation}")

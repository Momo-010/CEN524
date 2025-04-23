def sum_of_gp(a, r, n=None):

    # Calculate the sum of a Geometric Progression (GP).

    if n is not None:
        # Finite GP
        if r == 1:
            return a * n
        else:
            return a * (1 - r ** n) / (1 - r)
    else:
        # Infinite GP
        if abs(r) < 1:
            return a / (1 - r)
        else:
            raise ValueError("Infinite GP sum is only defined for |r| < 1 when n is not specified.")

def main():
    print("=== Geometric Progression Sum Calculator ===")
    try:
        a = float(input("Enter the first term (a): "))
        r = float(input("Enter the common ratio (r): "))
        n_input = input("Enter the number of terms (n), or press Enter for infinite GP: ")

        if n_input.strip() == "":
            result = sum_of_gp(a, r)
            print(f"The sum of the infinite GP is: {result}")
        else:
            n = int(n_input)
            result = sum_of_gp(a, r, n)
            print(f"The sum of the first {n} terms of the GP is: {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

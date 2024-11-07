"""
Genererer fibonacci tall nummer n.
"""
import argparse

def fibonacci(n):
    """Genererer Fibonacci-sekvensen opp til det n-te tallet og returnerer det."""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def main():
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Parse command line arguments example.")

    # Add arguments
    parser.add_argument('n', type=int, help="An integer for Fibonacci calculation")
    parser.add_argument('m', type=int, nargs='?', default=1, help="Number of Fibonacci numbers to print (optional)")

    # Parse the arguments
    args = parser.parse_args()

    # Use the parsed arguments
    #print(f'n = {args.n}, m = {args.m}')

    if args.m == 1:
        numbers = [31, 45, 53, 80, 34, 53, 80, 63, 39, 58, 64, 66, 35, 50, 16, 18, 42, 65, 64, 27, 54, 72, 43, 26, 26, 23, 42, 61, 94, 81, 83, 49, 93, 58, 56, 61, 57, 85, 74, 58, 32, 56, 19, 72, 31, 75, 37, 19, 16, 62, 76, 50, 90, 53, 89, 50, 63, 67, 55, 38, 86, 87, 57, 33, 43, 73, 38, 68, 86, 94, 29, 76, 33, 24, 64, 44, 81, 69, 75, 16, 76, 88, 60, 58, 23, 67, 25, 81, 52, 43, 15, 90, 76, 41, 41, 27, 44, 50, 82, 59, 57, 86, 88, 92, 90, 57, 84, 85, 20, 17, 56, 71, 87, 17, 58, 93, 39, 73, 64, 34, 87, 70, 19, 92, 74, 63, 70, 86, 17, 27, 29, 77, 25, 66, 35, 93, 75, 58, 18, 27, 62, 69, 76, 88, 40, 21, 88, 92, 37, 87, 16, 22, 59, 92, 28, 67, 47, 94, 80, 68, 64, 15, 67, 48, 92, 23, 31, 72, 19, 27, 60, 64, 68, 91, 33, 83, 41, 18, 46, 52, 85, 17, 94, 92, 58, 35, 30, 46, 82, 93, 48, 91, 42, 57, 18, 69, 59, 83, 73, 82]
        print("calculates 200 fib numbers")
        for num in numbers:
            fibonacci(num)
        print("Done!")
    else:
        print(fibonacci(args.n))

if __name__ == "__main__":
    main()
#354 224 848 179 261 915 075

"""
Returnerer det n-te tallet i fibonacci serien.
"""

import sys

def fibonacci(n):
    """Genererer Fibonacci-sekvensen opp til det n-te tallet og returnerer det."""
    a, b = 0, 1
    for i in range(n+2):
        a, b = b, a + b
    return a

if __name__ == "__main__":

    # Get the arguments from sys.argv
    try:
        n = int(sys.argv[1])  # First argument is the Fibonacci number to calculate
        print(fibonacci(n))
    except IndexError:
        print("n is not defined. Syntax: python fibonacci.py n")
    
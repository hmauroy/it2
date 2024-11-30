"""
En samling av funksjoner.
"""

def legg_sammen(a,b):
    if b == 0:
        return "b er null!"
    else:
        return a + b

def main():
    print(legg_sammen(5, 1))

# print("Hilsen fra innsiden av biblioteket.") # Fyfy å ha statements i selve skriptet.


if __name__ == "__main__":
    main()


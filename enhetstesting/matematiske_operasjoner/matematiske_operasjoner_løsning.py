"""

"""


def add_and_subtract(a, b):
    """Legger sammen to tall og subtraherer det andre fra det første."""
    return a + b, a - b


def multiply_and_divide(a, b):
    """Multipliserer to tall og dividerer det første med det andre."""
    if b == 0:
        return "Kan ikke dele på null!"
    return a * b, a / b


def power_and_square_root(a, b):
    """Hever det første tallet til det andre og finner kvadratroten av det første tallet."""
    return a ** b, a ** 0.5


def floor_and_ceil(a, b):
    """Gulv og tak av det første tallet og det andre tallet."""
    import math
    return math.floor(a), math.ceil(b)


def mod_and_integer_division(a, b):
    """Modulus og heltallsdivisjon av to tall."""
    if b == 0:
        return "Kan ikke dele på null!"
    return a % b, a // b


def average_and_sum(a, b):
    """Beregn gjennomsnitt og summen av to tall."""
    return (a + b) / 2, a + b


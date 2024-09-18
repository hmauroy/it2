"""
Egen for-løkke
"""

def For(a,b):
    ferdig = False
    teller = a
    while not ferdig:
        print(teller)
        teller += 1
        if teller >= b:
            ferdig = True

For(0,10)
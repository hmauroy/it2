"""
Funksjon som tar en eller to parametre.
"""

def fun(liste,*args):
    if args and len(args) == 1:
        n = args[0]
        return liste[-n:]   # args er nå en enkelt verdi som gjøres om til heltall.
    else:
        return liste[-1]

print(fun([1,2,4,3,6]))
print(fun([1,2,4,3,6],3))
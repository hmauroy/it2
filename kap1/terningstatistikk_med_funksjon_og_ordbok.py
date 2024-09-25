"""
Terningstatistikk
"""
from random import randint

def terning(n):
    """n er antall øyne"""
    return randint(1,n)

def statistikk(antall_kast):
    verdi = 0
    ordbok = {}
    for i in range(antall_kast):
        verdi = terning(6)
        if verdi in ordbok:
            ordbok[verdi] += 1
        else:
            ordbok[verdi] = 1
    return ordbok



# Tester terningfunksjon
#for i in range(10):
#    print(terning(6))

terningstatistikk = statistikk(100)
for key,value in terningstatistikk.items():
    print(f"Terning {key}: {value} forekomster")

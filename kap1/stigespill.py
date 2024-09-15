"""
Vi starter nede i venstre hjørne og går mot høyre. Ved enden snur vi og går tilbake til venstre, og slik fortsetter vi ved hver ende.

Treffer vi en stige beveger vi oss til stigens ende, og tilsvarende om vi treffer en slange. Nedenfor kan du se en tabell som oppsummerer plasseringen av stiger og slanger.

Vinneren er den som først kommer i mål. Synes du man må vinne ved å lande direkte på målfeltet? Eller holder det å passere det for å vinne?

Tabell over stiger og slanger

"""

from random import randint

rader = 10
kolonner = 10
brett = []
shadow = []
players = []
radstart = 111
endring = -1
teller = 0
# Lager stiger
stiger = [
    [1,4,9,21,28,36,51,71,80],
    [38,14,31,42,84,44,67,91,100]
]
slanger = [
    [16,48,49,56,62,64,87,93,95,98],
    [6,26,11,53,19,60,24,73,75,78]
]
for i in range(rader):
    if i % 2 == 0:
        radstart -= 11
        endring = -1
    else:
        radstart -= 9
        endring = 1
    brett.append([])
    shadow.append([])
    for j in range(kolonner):
        # Leter etter slanger og stiger
        if radstart in slanger[0]:
            brett[i].append("🐍")
        elif radstart in stiger[0]:
            brett[i].append("🪜")
        else:
            brett[i].append(radstart)
        shadow.append(radstart)
        radstart += endring



        
#print(ord("🐍"))



# Starter spillet
viSpiller = True
posisjon = 0
posisjon_old = 0
while viSpiller:
    input("Trykk enter for å kaste terning...")
    terning = randint(1,6)
    posisjon += terning
    if posisjon in stiger[0]: # Leter etter om posisjonen finnes i listen med start for stigene.
        # finner indeksen til stigen så vi kan anvende indeksen på listen med enden på stigene.
        kol_indeks = stiger[0].index(posisjon)
        posisjon = stiger[0][kol_indeks]
        print("STIGE!")
    print(f"Spiller gikk fra posisjon {posisjon_old} til posisjon {posisjon}")
    posisjon_old = posisjon
    
    # Leter etter indeksen til spiller
    m = 9
    n = 0
    for i in range(rader):
        for j in range(kolonner):
            if brett[i][j] == posisjon:
                m = i
                n = j
    print(f"rad: {m}, kol: {n}")

    # Skriver ut brettet
    for i in range(rader):
        for j in range(kolonner-1):
            if i == m and j == n:
                print(" 🅿️ ", end=" ")
            else:
                if isinstance(brett[i][j],str):
                    if ord(brett[i][j]) == 129692:  # Stige-emoji har unicode-verdi 129692
                        print(f" {brett[i][j]}", end="  ")
                    elif ord(brett[i][j]) == 128013: # Slange-emoji har unicode-verdi. Bruker en plass mer.
                        print(f" {brett[i][j]}", end=" ")
                else:
                    print(f"{brett[i][j]:3}", end=" ")
        if i == m and j == n:
            print(" 🅿️ ")
        elif isinstance(brett[i][j],str):
                if ord(brett[i][j]) > 1000:
                    print(f" {brett[i][j]}")
        else:
            print(f"{brett[i][-1]:3}")


        

"""
Du kan også la maskinen «spille» spillet mange ganger og få litt statistikk knyttet til spillet. 
Hvor mange kast er det vanligste antallet kast som kreves for å vinne?

Hvor mange kast skal til før det er ganske sannsynlig at noen vinner? 
Er alle stiger og slanger like «populære»? (Altså: Lander spillerne like ofte på hver av stigene?)


Vi starter nede i venstre hjørne og går mot høyre. Ved enden snur vi og går 
tilbake til venstre, og slik fortsetter vi ved hver ende.

Treffer vi en stige beveger vi oss til stigens ende, og tilsvarende om 
vi treffer en slange. Nedenfor kan du se en tabell som oppsummerer 
plasseringen av stiger og slanger.

Vinneren er den som først kommer i mål. Synes du man må vinne ved å 
lande direkte på målfeltet? Eller holder det å passere det for å vinne?

Tabell over stiger og slanger
# [[fra posisjoner],[destinasjoner]]
stiger = [
    [1,  4,9, 21,28,36,51,71, 80],
    [38,14,31,42,84,44,67,91,100]
]
slanger = [
    [16,48,49,56,62,64,87,93,95,98],
    [6, 26,11,53,19,60,24,73,75,78]
]

"""

from random import randint
import matplotlib.pyplot as plt

rader = 10
kolonner = 10
brett = []
shadow = []
players = []
radstart = 111
endring = -1
# Lager stiger, [[fra posisjoner],[destinasjoner]]
stiger = [
    [1,  4,9, 21,28,36,51,71, 80],
    [38,14,31,42,84,44,67,91,100]
]
slanger = [
    [16,48,49,56,62,64,87,93,95,98],
    [6, 26,11,53,19,60,24,73,75,78]
]
for i in range(rader):
    if i % 2 == 0:
        radstart -= 11
        endring = -1
    else:
        radstart -= 9
        endring = 1
    brett.append([])
    shadow.append([])   # lager rad i skyggebrettet
    for j in range(kolonner):
        # Leter etter slanger og stiger
        if radstart in slanger[0]:
            brett[i].append("🐍")
        elif radstart in stiger[0]:
            brett[i].append("🪜")
        else:
            brett[i].append(radstart)
        shadow[i].append(radstart) # Fyller skyggebrettet
        radstart += endring




# Lager en ordbok som kan lagre antall ganger hvert felt blir besøkt.
statistikk = {
    "antKast": {},
    "felter": [0 for x in range(106)],

}
ant_repetisjoner = 10000
for i in range(ant_repetisjoner):
    # Printer ut prosent fremdrift, bruker CPU-ressurser men kan være fint å se på.
    if i % (10*ant_repetisjoner/100) == 0:
        print(f"{100* i / ant_repetisjoner:.0f} %")

    viSpiller = True
    teller = 0
    # Starter spillet
    posisjon = 0
    posisjon_stige = 0
    posisjon_slange = 0
    posisjon_old = 0
    m = 9
    n = 0
    antKast = 0
    while viSpiller:
        antKast += 1
        terning = randint(1,6)
        #print(f"Terning: {terning}")
        posisjon += terning
        # Oppdaterer ordboken med antall ganger feltet er besøkt.
        statistikk["felter"][posisjon-1] += 1
        if posisjon in stiger[0]: # Leter etter om posisjonen finnes i listen med start for stigene.
            # finner indeksen til stigen så vi kan anvende indeksen på listen med enden på stigene.
            posisjon_stige = posisjon
            kol_indeks = stiger[0].index(posisjon)
            posisjon = stiger[1][kol_indeks]
            #print("STIGE!")
            #print(f"Spiller gikk fra posisjon {posisjon_old} via {posisjon_stige} til posisjon {posisjon}")
        elif posisjon in slanger[0]: # Leter etter om posisjonen finnes i listen med start for slangene.
            # finner indeksen til slangen så vi kan anvende indeksen på listen med enden på slangene.
            posisjon_slange = posisjon
            kol_indeks = slanger[0].index(posisjon)
            posisjon = slanger[1][kol_indeks]
           # print("SLANGE UÆÆÆ!")
            #print(f"Spiller gikk fra posisjon {posisjon_old} via {posisjon_slange} til posisjon {posisjon}")
        else:
            #print(f"Spiller gikk fra posisjon {posisjon_old} til posisjon {posisjon}")
            posisjon_old = posisjon
        if posisjon >= rader * kolonner:
            #print(f"Du vant!")
            #print(f"Antall kast: {antKast}")
            if antKast in statistikk["antKast"]:
                statistikk["antKast"][antKast] += 1
            else:
                statistikk["antKast"][antKast] = 1
            viSpiller = False
            continue
        
        # Leter etter indeksen til spiller i shadow-brettet som inneholder selve tallene og ingen emojis.
        for i in range(rader):
            for j in range(kolonner):
                if shadow[i][j] == posisjon:
                    m = i
                    n = j

    
# Sorterer ordboken etter synkende frekvens.
# ChatGPT 18. okt 2023 hjalp til med dette kompliserte lambdauttrykket vi ikke trenger å 
# forstå, bare bruke.
sortert_verdier = dict(sorted(statistikk["antKast"].items(), key=lambda item: item[1], reverse=True))
sortert_nøkler = dict(sorted(statistikk["antKast"].items(), key=lambda item: item[0], reverse=False))

# Legg den sorterte ordboken inn i en liste der hvert par legges inn som en tuple.
# ChatGPT hjalp til nok en gang!
sortert_list_nøkler = [(key, value) for key, value in sortert_nøkler.items()]
sortert_list_verdier = [(key, value) for key, value in sortert_verdier.items()]
# Printer ut sortert
for pair in sortert_list_nøkler:
    print(pair)

# Lager et plot over frekvensen til antall kast
xverdier = [key for key,val in sortert_list_nøkler]
yverdier = [val for key,val in sortert_list_nøkler]

# Create a figure object with specified dimensions

plt.bar(xverdier, yverdier,color="darkslateblue")
plt.title(f"Stigespill antall kast for å vinne etter {ant_repetisjoner} spill.")
plt.xlabel("Antall kast")
plt.ylabel("Frekvens")

plt.show()

# Lager et plot over frekvensen til hvert felt
felt_indekser = [x for x in range(0,106)]

plt.bar(felt_indekser, statistikk["felter"],color="darkslateblue")
plt.title(f"Stigespill antall besøk for hvert felt 0-103 etter {ant_repetisjoner} spill.")
plt.xlabel("Felt indeks (0,1,2,...)")
plt.ylabel("Frekvens")

plt.show()


# Skriver statistikk til fil (kapitttel 3B)
import json
utdata = json.dumps(statistikk,indent=4)
print(utdata)

# Skriver til fil
with open(f"statistikk_stigespill_{ant_repetisjoner}reps.json", "w") as fil:
    fil.write(utdata)



            

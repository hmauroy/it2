liste = [
    {
        "navn": "Jonas Bredesen",
        "alder": 9
    },
    {
        "navn": "Jonas Larsen",
        "alder": 94
    }
]
def finn_person_alder(navn):
    """Finner alder ved å søke på navn. \n
    Eksempel på bruk \n
    alder = finn_person_alder(navn)
    """
    indeks = 0
    while True:
        person = liste[indeks]
        if person["navn"] == navn:
            return person["alder"]
        indeks += 1
        if indeks >= len(liste):
            return False

def finn_person_alder_forlokke(navn):
    for person in liste:
        if person["navn"] == navn:
            return person["alder"]
    return False

print(help(finn_person_alder))

print(finn_person_alder("Jonas Larsen"))
print(finn_person_alder("Jonas Bredesen"))
print(finn_person_alder_forlokke("Jonas Bredesen"))


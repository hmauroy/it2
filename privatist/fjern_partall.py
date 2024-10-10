liste = [1,2,3,4,5,6,7,8,9]
# Bruker løkke og sjekker for partall
# Indeksene til de som skal fjernes lagres for å brukes
# senere.

for i in range(len(liste)-1,-1,-1):
    if liste[i] % 2 == 0:
        liste.pop(i)
   


#Alternativ 2 og 3
liste = [1,2,3,4,5,6,7,8,9]


sletteliste = []
kopiliste = []  # Kopi av listen
for i in range(len(liste)):
    if liste[i] % 2 == 0:
        sletteliste.append(i)
    else:
        kopiliste.append(liste[i])
print(f"Sletter indeksene: {sletteliste}")
# Sletter indeksene
sletteliste.sort(reverse=True)
for indeks in sletteliste:
    liste.pop(indeks)

print(sletteliste)

print(liste)
liste = [5,7,13,4]

print(f"Første verdi: {liste[0]}")
print(f"Siste verdi: {liste[-1]}")
print(f"Siste verdi: {liste[len(liste)-1]}")
print(f"Nest siste verdi: {liste[-2]}")

liste[1] = 9
print(liste)
print(f"lengde: {len(liste)}")
# Bytte om to verdier
buffer = liste[0]
liste[0] = liste[-1]
liste[-1] = buffer
print(liste)

mange_tall = []
for i in range(10000000):
    mange_tall.append(i)
print(len(mange_tall))
print(mange_tall[len(mange_tall)-100:])
# Sletter noe fra slutten og fra starten
print(mange_tall.pop())
print(mange_tall.pop(0))
print(f"lengde nå: {len(mange_tall)}")
try:
    print(mange_tall.remove(31400000))
except ValueError as e:
    print("Noe gikk galt. Full feilmelding:")
    print(e)
print("Programmet fortsetter å kjøre.")
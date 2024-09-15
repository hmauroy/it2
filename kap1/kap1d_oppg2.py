"""
Lag en liste med heltallene fra og med 1 til og med 50. 
Skriv ut lista for å sjekke at du har fått med de riktige tallene.
"""

partall = []
for tall in range(1,51):
    if tall % 2 == 0:
        partall.append(tall)

print(partall)
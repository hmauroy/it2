"""
Lag et program som ber brukeren oppgi karaktersnittet sitt. 
Husk at et karaktersnitt ofte er et desimaltall. Legg til en 
test som sørger for at snittet som oppgis, er mulig å ha. 
Bruk en løkke slik at programmet fortsetter helt til et godkjent tall er oppgitt.
"""

godkjent = False

while not godkjent:
    snitt = input("skriv inn karaktersnitt som desimaltall: ")
    try:
        snitt = float(snitt)
        godkjent = True
        print(f"Bra, du har et snitt på {snitt:.1f}")
    except ValueError:
        print(f"Feil input! Du må skrive desimaltall med . som skilletegn.")
    
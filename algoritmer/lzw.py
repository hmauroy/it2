"""
LZW-algoritmen for å komprimere tekst.
Henriks egen versjon laget på sparket i timen 28/10-2024.
Koder med litt juks som en tekst med tegnene b, 0 og 1.
"""
t = "abcabcabc"
t = "Problemet er at du ikke vet om toget kommer, eller er i rute. Det er for uforutsigbart for hundretusenvis av folk."
#print(ord("b"))

lzw = {}
kode = 0
sekvens = ""

# Går gjennom teksten
for c in t:
    #print(f"ascii-kode {ord(c)}")
    if len(sekvens) >= 8:
        sekvens = ""
    else:
        sekvens += c
    if c not in lzw:
        lzw[c] = kode
        kode += 1
    if sekvens not in lzw:
        lzw[sekvens] = kode
        kode += 1
    

for key,val in lzw.items():
    print(key,bin(val))

# "Problemet er at du ikke vet om toget kommer, eller er i rute. Det er for uforutsigbart for hundretusenvis av folk."
ut = ""
sekvens_gammel = ""
for c in t:
    if len(sekvens) >= 8:
        sekvens = ""
    else:
        sekvens += c
    if sekvens in lzw:
        sekvens_gammel = sekvens
        ut += str(bin(lzw[sekvens]))

print(ut)
lengde_tekst = len(t) * 8
forhold = len(ut) / lengde_tekst
print(f"Forholdet [ut_tekst]:[input_tekst] = {100*forhold:.1f}%")

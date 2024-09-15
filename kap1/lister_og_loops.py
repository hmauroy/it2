liste = [x**3 for x in range(100)] # "List comprehension"
# 1) Indeksert for-løkke
for i in range(len(liste)):
    #print(liste[i])
    if liste[i] == 262144:
        print(f"262144 ligger på indeks {i}")
# 2) Verdi-looping
teller = 0
for verdi in liste: # Loop går gjennom hvert element og plukker det opp.
    #print(verdi)
    if verdi == 262144:
        print(f"262144 ligger på indeks {teller}")
    teller += 1
print(f"262144 ligger på indeks {liste.index(262144)}")

# Hvilken indeks har tallet 262144?
# Svaret er 64

# Baklengs looping
for i in range(len(liste)-1,-1,-1):
    print(i)


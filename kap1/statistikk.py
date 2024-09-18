from random import randint
tall = []
for i in range(100000000):
    tall.append(randint(1,6))
# Lager statistikk
statistikk = {}
for verdi in tall:
    if verdi in statistikk:
        statistikk[verdi] += 1
    else:
        statistikk[verdi] = 1

print(statistikk)

exit()
vanligste = max(statistikk.values())
for key,val in statistikk.items():
    if val == vanligste:
        print(f"vanligste tall er {key} med {val} forekomster")

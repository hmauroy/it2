setning = "Lag en tekstvariabel som inneholder en setning. Lag en ordbok som inneholder alle bokstavene i setningen/teksten, og som angir hvor mange ganger hver bokstav forekommer i teksten."

# Ordbok som inneholder statistikk over bokstaver
statistikk = {}

for bokstav in setning:
    if bokstav in statistikk:
        statistikk[bokstav] += 1
    else:
        statistikk[bokstav] = 1

for nokkel, verdi in statistikk.items():
    print(f"{nokkel}: {verdi}")
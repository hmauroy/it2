# Lager ordboken
ordbok = {}

# Legger til nøkkel og verdi-par
ordbok["10"] = "ti"
ordbok["2"] = "to"


print(ordbok)

for nokkel,verdi in ordbok.items():
    print(nokkel,verdi)

for x in ordbok:
    print(x)

for y in ordbok.keys():
    print(y)

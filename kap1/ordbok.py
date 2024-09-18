"""
Ordbok med python
"""

noedetater = {
    "113": "Ambulanse",
    "112": "Politi",
    "110": "Brann"
}
# Loope med nøkkelen
for nøkkel in noedetater:
    print(nøkkel)

# Loope med verdi
for verdi in noedetater.values():
    print(verdi)

# Loope med keys
for nøkkel in noedetater.keys():
    print(nøkkel, noedetater[nøkkel])   # Henter ut verdi ved hjelp av nøkkel.


# Loope med både nøkkel og verdi
for key, val in noedetater.items():
    print(key,val)

print(f"110 hører til {noedetater['110']}") # Må bruke to ulike anførselstegn.
print(f'{noedetater["112"]}')

# Legge til ny verdi
noedetater["nyNøkkel"] = "Legevakten"
print(noedetater)
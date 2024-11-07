"""
Leser fra en json-fil.
"""

 

"""

ordbok = {
  "en": 1,
  "to": 2,
  "tre": 3
}

utskrift = json.dumps(ordbok)

# Skriver til fil
with open("ordbok.json", "w") as fil:
    fil.write(utskrift)

  """
import json

filnavn = "ordbok.json"
#filnavn = "liste.json"

# Åpner tekstfilen og gjør om fra json-format til en ordbok
with open(filnavn, encoding="utf-8") as f:
  data = json.load(f)

print(type(data))
# Skriver ut ordboken vi fikk fra tekstfilen.
for key, value in data.items():
    print(key,value)

"""
En enkel simulering av bestanden til rådyr og rever i en skog.
"""
from random import randrange
# Rådyrenes egenskaper
n_deer = 20
deer_male_prob = 0.3    # Sannsynlighet for at avkom blir hann.
t_deer_reproduction_ready = 2   # Antall år før rådyr kan få avkom
male_reproduction = 5   # Antall suksefull parringer per sesong


n_fox = 10

class Deer:
    def __init__(self) -> None:
        self.setSex()
    

    def setSex(self):
        prob = randrange(1,100)
        if prob <= 70:
            self.sex = "hann"
        else:
            self.sex = "hunn"

dyr = []
for i in range(1000000):
    dyr.append(Deer())

male = 0
female = 0
for d in dyr:
    if d.sex == "hann":
        male += 1
    else:
        female += 1

print(f"antall hanner: {male}")
print(f"antall hunner: {female}")
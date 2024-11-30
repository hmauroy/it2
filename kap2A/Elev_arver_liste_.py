"""
To klasser som beskriver elever og skoleklasser.
"""

class Elev(list):
    def __init__(self) -> None:
        super().__init__()
        self.navn = "Superlisten"
    
    def __str__(self):
        tekst = ""
        for verdi in self:
            tekst += f"{self.navn}: {verdi}, "
        return tekst


elev = Elev()
elev.append(1)
elev.append(2)
elev.append(3)

print(elev)

    
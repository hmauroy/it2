"""
Mitt første ekte python-program.
En quiz med spørsmål og svar.
"""

class Quiz:
    def __init__(self):
        self.navn = "Henrik Mauroy"
        self.questions = [
            ["Er hovedstaden i Norge Oslo?", "ja"],
            ["Nytt spm", "492"]
            ]

    def nyttSpm(self):
        if len(self.questions) > 0:
            return self.questions.pop()
        else:
            return "Error! Ikke flere spørsmål!"
    
    def sjekkSvar(self,spm,brukersvar):
        if brukersvar == spm[1]:
            print("Hurra! Det var riktig!")
        else:
            print("Sorry, feil svar :(")


q = Quiz()
print(q.navn)
spm = q.nyttSpm() # Legger et nytt spørsmål inn i variabel spm
print(spm[0])
svar = input("Svar på spørsmålet: ")
print(f"Du svarte: {svar}")
q.sjekkSvar(spm,svar)

# Henter spørsmål
spm2 = q.nyttSpm()
print(spm2[0])
# Svarer på det
svar2 = input("svar nøyaktig med riktig caps: ")
# Sjekker svar
q.sjekkSvar(spm2, svar2)


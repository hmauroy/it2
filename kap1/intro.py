class Quiz:
    def __init__(self) -> None:
        self.navn = "klasseQuiz"
        self.questions = ["Hva er Norges hovedstad?"]
    
    def newQuestion(self):
        if len(self.questions) > 0:
            spm = self.questions.pop(0)
            return spm
        else:
            return "ERROR! Ingen flere spørsmål igjen."
    
    def addQuestion(self):
        spm = input("Skriv inn et spørsmål, avslutt med ENTER: ")
        self.questions.append(spm)
    
    def lengdeSpm(self):
        q = self.newQuestion()
        lengde = len(q)
        print(f"Lengden på {q} er {lengde} tegn")

q = Quiz()
q.newQuestion()
q.addQuestion()
q.lengdeSpm()



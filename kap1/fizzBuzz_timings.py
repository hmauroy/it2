"""
Skriv ut tallene fra 0 til 100. 
Hvis tallet er delelig på 3 skrives det ikke ut tallet, 
men ordet 'Fizz'. Hvis det er delelig på 5, skrives det ut 'Buzz'. 
Hvis det er delelig på både 3 og 5 skrives det ut 'FizzBuzz'.

Utfordring: Bruk så få linjer med kode som mulig :)
"""
# Åpenbar måte hvis man følger spørsmålet

mySetup = ''''''
mySlowCode='''
def fizzBuzz():
    for i in range(0,101):
        utskrift = ""
        if i % 3 == 0 and i % 5 == 0:
            utskrift += "FizzBuzz"
        elif i % 3 == 0:
            utskrift += "Fizz" 
        elif i % 5 == 0:
            utskrift += "Buzz" 
        else:
            utskrift += str(i)
        #print(utskrift)
'''

myFasterCode = '''
def fizzBuzzRask():
    for i in range(0,101):
        utskrift = ""
        if i % 3 == 0:
            utskrift += "Fizz" 
        if i % 5 == 0:
            utskrift += "Buzz" 
        if len(utskrift) == 0:
            utskrift += str(i)
        #print(utskrift)
'''

myEvenFasterCode = '''
def fizzBuzzEndaRaskere():
    for i in range(0,101):
        utskrift = ""
        if i % 3 == 0:
            utskrift += "Fizz" 
        if i % 5 == 0:
            utskrift += "Buzz" 
        if len(utskrift) < 1:
            utskrift += str(i)
        #print(utskrift)
'''

# Måling av ytelse med timeit
import timeit
tid_raskere_kode = timeit.repeat(setup=mySetup,
                    stmt=myEvenFasterCode,
                    repeat=1,
                    number=10000000)
tid_rask_kode = timeit.repeat(setup=mySetup,
                    stmt=myFasterCode,
                    repeat=1,
                    number=10000000)
tid_treg_kode = timeit.repeat(setup=mySetup,
                    stmt=mySlowCode,
                    repeat=1,
                    number=10000000)

print(f"Treg kode tok: {min(tid_treg_kode)} s")
print(f"Rask kode tok: {min(tid_rask_kode)} s")
print(f"Raskere kode tok: {min(tid_raskere_kode)} s")


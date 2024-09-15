totalutskrift = ""
for i in range(0,101):
    utskrift = ""
    if i % 3 == 0:
        utskrift += "Fizz" 
    if i % 5 == 0:
        utskrift += "Buzz" 
    if len(utskrift) == 0:
        utskrift += str(i)
    totalutskrift += utskrift
    totalutskrift += "\n"
print(totalutskrift)
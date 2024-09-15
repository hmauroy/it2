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
    print(utskrift)

for i in range(0,101):
        utskrift = ""
        if i % 3 == 0:
            utskrift += "Fizz" 
        if i % 5 == 0:
            utskrift += "Buzz" 
        if len(utskrift) == 0:
            utskrift += str(i)
        #print(utskrift)
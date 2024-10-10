ferdig = False

while not ferdig:
    t = input("skriv inn tall")
    try:
        tall = int(t)
        ferdig = True
    except ValueError as e:
        print(f"feil input: {e}")
    
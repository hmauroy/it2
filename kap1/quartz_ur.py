"""
41.	Analogt Quartz-ur. Først litt informasjon om virkemåten til quartz-ur: Det elektroniske analoge quartz-uret virker ved at en quartz-oscillator vibrerer med elektrisk stimulerte egensvingninger ved en frekvens på 
32 768 Hz.
Svingningene blir fanget opp av en elektrisk krets som aktiverer en kjede av 15 elektroniske flip-flops. 
En flip flop bytter status én gang når den aktiveres, fra 'flip' til 'flop', eller motsatt. I virkeligheten settes utgangen til enheten til å være 0V (flip) etter første aktivering. Når den så aktiveres en gang til blir utgangen satt til å være en positiv spenning (flop) som så aktiverer den neste flip-flop-enhetene i kjeden.
Fordi hver flip-flop-enhet må aktiveres 2 ganger før den gir et positivt aktiveringssignal til neste flip-flop tar det 215 ganger før den 15. (og siste) flip-flop-enheten får positiv spenning på utgangen sin. Denne siste flip-flop-en styrer sekundviseren på klokken. Smart ikke sant!
215 tilsvarer nøyaktig 32 768 ganger!
Dermed vil tiden det tar å gjøre alle disse flip-flop-ene ta ett sekund fordi quartz-krystallen svinger med 32 768 ganger per sekund.
	Det går dessverre ikke an å lage en oscillator som svinger så raskt med javascript i nettleseren, men vi kan bruke setInterval-funksjonen som kan gå ned til 1 millisekund som gir en svingetid på 1000Hz. Vi må derfor lage færre flip-flops som går opp i omtrent 1000 klokkesignaler:
1000 = 2x
x = 9,96
Hvis vi bruker 10 flip-flops trenger vi et klokkesignal som svinger 210 = 1024 klokkepulser i sekundet, som er ikke så langt unna det vi ønsker.
Intervall-funksjonen skulle helst aktivert den første flip-flopen hvert 
1/1024 = 0,98 ms
så klokken vår vil gå bittelitt for sakte siden vi kun kan gi klokkesignal hvert 1,0 ms, men sånn er det med urmakeri; Ingen klokker er 100% nøyaktige. Ikke engang atomur!
Oppgaven går nå ut på å lage 10 flip-flops (enkeltfunksjoner) som tar et inputsignal på 1000 Hz for å kjøre en sekundviser. Det kan gjerne være en digital sekundviser som blinker. 
"""
import time

isRunning = True
flipflops = {
    "ff1": False,
    "ff2": False,
    "ff3": False,
}

def flipFlop1():
    if flipflops["ff1"] == False:
        flipflops["ff1"] = True
    if flipflops["ff1"] == True:
        flipFlop2()

def flipFlop2():
    if flipflops["ff2"] == False:
        flipflops["ff2"] = True
    if flipflops["ff2"] == True:
        flipFlop3()

def flipFlop3():
    if flipflops["ff3"] == False:
        flipflops["ff3"] = True
    if flipflops["ff3"] == True:
        print("Sekund!")


def oscillator():
    time.sleep(0.3)
    flipFlop1()



oscillator()

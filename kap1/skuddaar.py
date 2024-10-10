"""
Hvis du vil teste om et år er et skuddår eller ikke, så kan du teste det ved å følge instruksene under.

 1.	Dersom årstallet dividert med 4 gir et heltall, 
 men det samme årstallet dividert med 100 ikke gir et heltall; 
 da er det et skuddår. Som for eksempel årene 1992, 1996 og 2004.

 2.	Dersom årstallet dividert med 4 gir et heltall, 
 og det samme årstallet dividert med 100 gir et heltall, 
 og årstallet kan ikke divideres med 400; da er det ikke et skuddår. 
 Som for eksempel årene 1900, 2100 og 2200.

 3.	Dersom årstallet dividert med 400400 gir et heltall, 
 da er det et skuddår. Som for eksempel 1600, 2000 1600, 2000 og 2400.

"""

def erSkuddaar(year):
    """Returnerer True hvis skuddår og False ellers. """
    #TODO

print(f"2024 var et skuddår? {erSkuddaar(2024)}")


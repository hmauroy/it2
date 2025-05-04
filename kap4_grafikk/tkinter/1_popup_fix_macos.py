# MacOS har et nylig problem med fokus for popup-vinduer i tkinter.
# Koden under fikser dette. Legg det inn rett etter at window er opprettet.

# Sentrer vinduet på skjermen
window_width = 600
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
window.geometry(f'{window_width}x{window_height}+{x}+{y}')

# Fjern vindu midlertidig
window.withdraw()  
window.update()
#vis vinduet igjen
window.deiconify()
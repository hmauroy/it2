import tkinter as tk
import random
import time

#Lage et vindu 
window = tk.Tk()
window.title("Dinospill")
window_width = 600
window_height = 400
window.minsize(window_width,window_height)

# MacOS har et nylig problem med fokus for popup-vinduer
# Sentrer vinduet på skjermen
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

#Lager et tegnebrett til animering
canvas = tk.Canvas(window, width=window_width, height=window_height, bg="white")
canvas.pack()

#Tegner bakken
bakke_høyde = window_height-50
canvas.create_line(0, bakke_høyde,window_width,bakke_høyde,width=5)

#Status på om spillet kjører
game_running = True

#Lager Dino class for animasjon av dinosauren(en klosse)
class Dino:
    def __init__(self,canvas):
        self.canvas = canvas
        self.x = 40
        self.y = bakke_høyde
        self.høyde = 30
        self.bredde = 20
        #Lager dinoen
        self.dino_id = canvas.create_rectangle(self.x-self.bredde,self.y -self.høyde, self.x + self.bredde,self.y, fill="blue")
        self.hopper = False
        self.dukker = False

    #Funksjon som definerer og animerer hopp
    def hopp(self):
        #Hindre at figuren hopper og dukker samtidig
        if self.hopper or self.dukker:
            return 
        self.hopper = True
        self.hopp_max = bakke_høyde - 150
        self.start_y = self.y
        self.hoppefart = -13 #Negativ fordi y-aksen er positiv nedover
        
        def animer_hopp():

            if self.hopper:
                #Flytt Dino oppover (-) så lenge den er under maks høyde og har negativ fart
                if self.hoppefart < 0 and self.y >self.hopp_max:
                    self.y += self.hoppefart
                elif self.hoppefart > 0 and self.y <self.start_y:
                    self.y += self.hoppefart
                else:
                    self.hoppefart = - self.hoppefart #Endrer retning på farten 
                
                if self.y >= self.start_y:
                    self.y = self.start_y
                    self.hopper = False
                
                canvas.coords(self.dino_id, self.x -self.bredde, self.y - self.høyde, self.x+self.bredde, self.y )

                if self.hopper:
                    window.after(20,animer_hopp)

        animer_hopp()
    
    #Lage en funksjon for dukking
    def dukk(self, start=True):
        #Hindrer dukking under hopp
        if self.hopper:
            return
        if start:
            self.dukker = True
            self.høyde = 20
            canvas.coords(self.dino_id, 
                          self.x - self.bredde -10, 
                          self.y, 
                          self.x + self.bredde +10,
                          self.y - self.høyde)
        else:
            self.dukker = False
            self.høyde = 30
            canvas.coords(self.dino_id, 
                          self.x - self.bredde, 
                          self.y - self.høyde, 
                          self.x + self.bredde, 
                          self.y )

#Klasse for å lage hindringer 
class Hindring:
    def __init__(self, canvas, y_offset = 0):
        self.canvas = canvas
        self.x = window_width
        self.y_offset = y_offset
        self.y = bakke_høyde - 20 - self.y_offset 

        #Tegner hindringen på canvaset som et rektangel
        self.hindring_id = canvas.create_rectangle(self.x, 
                                                   self.y, 
                                                   self.x+20,
                                                   self.y+20,
                                                   fill="red")
        
    def move(self):
        #Bevege hindringene mot venstre når spillet kjører
        if game_running:
            # self.x -=20
            #canvas.move() er det som flytter hindringen
            canvas.move(self.hindring_id,-20,0)

dino = Dino(canvas)

#Lage en funksjon som oppretter hindringer
hindringer = []
def spawn_hindring():
    #Generere hindringer med varierende høyde
    if game_running:
        y_offset = random.choice([5, 8, 9, 12, 15, 30, 40, 50, 300])
        hindring = Hindring(canvas, y_offset)
        hindringer.append(hindring)
        window.after(random.choice([500, 700, 1000, 1200, 1500]),spawn_hindring)


#Funksjon for å sjekke kollisjon mellom dino og hinder
def kollisjonssjekk(dino,hindring):
    dino_coords = canvas.coords(dino.dino_id)
    hindring_coords = canvas.coords(hindring.hindring_id)

    #Sjekke om dinoen dukker
    if dino.dukker:
        adjusted_dino_top = dino_coords[1] + 10
    else:
        adjusted_dino_top = dino_coords[1]

    overlapp_i_x = dino_coords[2] >= hindring_coords[0] and dino_coords[0] <=hindring_coords[2]
    overlapp_i_y = adjusted_dino_top <= hindring_coords[3] and dino_coords[3] >= hindring_coords[1]

    if overlapp_i_x and overlapp_i_y:
        return True
    return False


def game_loop():
    #Flytter hindringene så lenge spillet kjører
    if game_running:
        for hindring in hindringer:
            hindring.move()
            if kollisjonssjekk(dino, hindring):
                game_over()
                return

        window.after(50, game_loop)


#Lage en Game Over funksjon ved kollisjon
def game_over():
    global game_running
    game_running = False
    elapesed_time = round(time.time() -start_time,3)
    #Viser text med "Game Over"
    canvas.create_text(window_width/2, window_height/2-20, 
                       text="GAME OVER",
                       font=("Arial",30),
                       fill="red")
    #Tekst som viser tiden du fikk
    canvas.create_text(window_width/2,
                       window_height/2 +20,
                       text=f"Score: {elapesed_time} seconds",
                       font=("Arial", 20),
                       fill="green")








#Definerer hendelser for trykk på knapper
def on_up_key(event):
    if game_running:
        dino.hopp()
def on_down_key(event):
    if game_running:
        dino.dukk(start=True)
def on_down_key_relese(event):
    if game_running:
        dino.dukk(start=False)
def avslutt(event):
    window.destroy()


#Binder taster til funksjonene sine
window.bind("<Up>", on_up_key)
window.bind("<Down>", on_down_key)
window.bind("<KeyRelease-Down>", on_down_key_relese)
window.bind("<Escape>", avslutt)


#Starter soillet
start_time = time.time()
spawn_hindring()
game_loop()


window.mainloop()

import numpy as np
import pygame
import sys
import math

# Definera färger
BLUE = (0,0,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

# Definerar dimensionerna på "brädan"
Y_RADER = 6
X_RADER = 7

def skapa_bräda():           # Skapar en 2D numpy array bräda
    bräda = np.zeros((Y_RADER,X_RADER))
    return bräda

def droppa_pollet(bräda, rad, drag, pollet):    # En funktion för att spela en pollet i brädan
    bräda[rad][drag] = pollet
    
def tillåtet_drag(bräda, drag): # Funktion för att kolla om draget är tillåtet/möjligt
    return bräda[Y_RADER-1][drag] ==0

def öppna_nästa_rad(bräda, drag): 
    for i in range( Y_RADER):
        if bräda[i][drag] == 0:
            return i

def skriv_ut_brädan(bräda):
    print(np.flip(bräda, 0))

def vinnande_drag(bräda, pollet):
    #horisontellt
    for x in range(X_RADER-3):
        for y in range(Y_RADER):
            if bräda[y][x] == pollet and bräda[y][x+1] == pollet and bräda[y][x+2] == pollet and bräda[y][x+3] == pollet:
                return True

    for x in range(X_RADER):    #verticalt
        for y in range(Y_RADER-3):
            if bräda[y][x] == pollet and bräda[y+1][x] == pollet and bräda[y+2][x] == pollet and bräda[y+3][x] == pollet:
                 return True
    
    for x in range(X_RADER-3):  #diagonalt upp
        for y in range(Y_RADER-3):
            if bräda[y][x] == pollet and bräda[y+1][x+1] == pollet and bräda[y+2][x+2] == pollet and bräda[y+3][x+3] == pollet:
                return True

    for x in range(X_RADER-3):   #diagonalr ner
        for y in range(3,Y_RADER):
            if bräda[y][x] == pollet and bräda[y-1][x+1] == pollet and bräda[y-1][x+2] == pollet and bräda[y-1][x+3] == pollet:
                return True
            
def rita_bräda(bräda):
    for x in range(X_RADER):
        for y in range(Y_RADER):
            pygame.draw.rect(screen, BLUE, (x*storlek_ruta, y*storlek_ruta + storlek_ruta, storlek_ruta, storlek_ruta))
            pygame.draw.circle(screen, BLACK, (int(x*storlek_ruta+storlek_ruta/2), int(y*storlek_ruta+storlek_ruta+storlek_ruta/2)), radie)

    for x in range(X_RADER):
        for y in range(Y_RADER):		
            if bräda[y][x] == 1:
                pygame.draw.circle(screen, RED, (int(x*storlek_ruta+storlek_ruta/2), höjd-int(y*storlek_ruta+storlek_ruta/2)), radie)
            elif bräda[y][x] == 2: 
                pygame.draw.circle(screen, YELLOW, (int(x*storlek_ruta+storlek_ruta/2), höjd-int(y*storlek_ruta+storlek_ruta/2)), radie)  
    pygame.display.update()            


bräda = skapa_bräda()
skriv_ut_brädan(bräda)
spelet_slut = False
tur = 0

pygame.init()

storlek_ruta = 100
brädd = X_RADER * storlek_ruta
höjd = (Y_RADER +1 ) * storlek_ruta

storlek = (brädd, höjd)

radie = int(storlek_ruta/2 - 5)

screen = pygame.display.set_mode(storlek)
rita_bräda(bräda)
pygame.display.update()

myFont= pygame.font.SysFont('monospace', 60)

while not spelet_slut:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION: # Kollar musens rörelse
            pygame.draw.rect(screen, BLACK, (0,0, brädd, storlek_ruta))
            posx = event.pos[0]
            if tur == 0:
                pygame.draw.circle(screen, RED, (posx, int(storlek_ruta/2)), radie)
            else:
                pygame.draw.circle(screen, YELLOW, (posx, int(storlek_ruta/2)), radie)

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN: # Kollar musklick
            
            if tur == 0:
                posx = event.pos[0]
                drag = int(math.floor(posx/storlek_ruta))
                
                if tillåtet_drag(bräda, drag):
                    rad = öppna_nästa_rad(bräda, drag)
                    droppa_pollet(bräda,rad,drag, 1)
                    if vinnande_drag(bräda,1):
                        label = myFont.render('Seplare 1 vann!:', 1, RED)
                        screen.blit(label,(40,10))
                        spelet_slut = True
                        
            else:
                posx = event.pos[0]
                drag = int(math.floor(posx/storlek_ruta))
                if tillåtet_drag(bräda, drag):
                    rad = öppna_nästa_rad(bräda, drag)
                    droppa_pollet(bräda,rad,drag, 2)
                    if vinnande_drag(bräda,2):
                        label = myFont.render('Seplare 2 vann!:', 1, YELLOW)
                        screen.blit(label,(40,10))
                        spelet_slut = True
                        
            skriv_ut_brädan(bräda)
            rita_bräda(bräda)
            tur +=1
            tur = tur % 2

            if spelet_slut:
                pygame.time.wait(5000)

    
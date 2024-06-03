
from tre_i_rad_backend import player2, randomAiSpelare, oslagbarAI
import time
import math

class treIRad:
    def __init__(self):
        self.bräda = self.skapa_bräda()
        self.C_vinnare=None
    @staticmethod
    def skapa_bräda():
         return [' ' for _ in range(9)]

    def Skriv_ut_brädan(self):
        for rad in [self.bräda[i*3:(i+1)*3] for i in range(3)]:
            print(' | ' + ' | '.join(rad) + ' | ')

    @staticmethod
    def print_board_nums():
       nummer_bräda = [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]
       for rad in nummer_bräda:
           print(' | ' + ' | '.join(rad) + ' | ') 
    
    def möjliga_drag(self):
        return [i for i, x in enumerate(self.bräda) if x == ' ']

    def tomma_rutor(self):
        return ' ' in self.bräda

    def antal_tomma_rutor(self):
        return self.bräda.count(' ')

    def gör_drag(self, ruta, spelare):
        if self.bräda[ruta] == ' ':
           self.bräda[ruta] = spelare 
           if self.vinnare(ruta ,spelare):
               self.C_vinnare = spelare
           return True
        return False

    def vinnare(self, ruta, spelare):
        rad_ind = math.floor(ruta / 3)
        rad = self.bräda[rad_ind*3:(rad_ind + 1) *3]
        if all([spot == spelare for spot in rad]):
            return True

        col_ind = ruta % 3 
        column = [self.bräda[col_ind+i*3] for i in range(3)]
        if all([spot == spelare for spot in column]):
            return True
        
        if ruta % 2 == 0:
            diagonal1 = [self.bräda[i] for i in [0, 4, 8]]
            if all([spot == spelare for spot in diagonal1]):
                return True
            diagonal2 = [self.bräda[i] for i in [2, 4, 6]]
            if all([spot == spelare for spot in diagonal2]):
                return True
                
def spela(game, x_spelare, o_spelare, skriv_ut_spelet = True):
    
    if skriv_ut_spelet:
        game.antal_tomma_rutor()
    
    spelare = "X"
    while game.tomma_rutor():
        if spelare == 'O':
            ruta = o_spelare.get_move(game)
        else:
            ruta = x_spelare.get_move(game)

        if game.gör_drag(ruta, spelare):
            
            if skriv_ut_spelet:
                print(spelare + ' gjorde ett drag till ruta {}'.format(ruta))
                
                game.Skriv_ut_brädan()
                print(' ')
           
            if game.C_vinnare:
                if skriv_ut_spelet:
                    print(spelare +' har vunnit')
                return spelare
            spelare = 'O' if spelare == 'X' else 'X'
        time.sleep(.5)
    if skriv_ut_spelet:
            print('Det blev lika')

if __name__ == '__main__':
     x_spelare = player2('X')
     o_spelare = oslagbarAI('O')
     t = treIRad()
     treIRad.print_board_nums()
     spela(t, x_spelare, o_spelare, skriv_ut_spelet=True)



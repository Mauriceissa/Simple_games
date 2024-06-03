import math
import random


class Spelare:
    def __init__(self, spelare):
        self.spelare = spelare

    def get_move(self, game):
        pass    

class randomAiSpelare(Spelare):
    def __init__(self, spelare):
        super().__init__(spelare)

    def get_move(self, game):
        ruta = random.choice(game.möjliga_drag())
        return ruta

class player2(Spelare):
    def __init__(self, spelare):
        super().__init__(spelare)


    def get_move(self, game):
        möjlig_ruta = False
        val = None
        while not möjlig_ruta:
            ruta = input(self.spelare + ' skriv in ditt drag (0-8): ') 
            try:
                val=int(ruta) 
                if val not in game.möjliga_drag():
                    raise ValueError
                möjlig_ruta = True
            except ValueError:
                print( "du kan inte använda den rutan, försök igen. ") 
        return val       

class oslagbarAI(Spelare):
    def __init__(self, spelare):
        super().__init__(spelare)
   
    def get_move(self, game):
        if len(game.möjliga_drag()) == 9:
            ruta = random.choice(game.möjliga_drag())
        else:
            ruta = self.minimax(game, self.spelare)['position'] 
        return ruta

    def minimax(self, state, spelare):
        max_spelare = self.spelare
        annan_spelare = 'O' if spelare == 'X' else 'X'

        if state.C_vinnare == annan_spelare:
            return {'position': None, 'poäng': 1 * (state.antal_tomma_rutor() +1)
             if annan_spelare == max_spelare else -1* (state.antal_tomma_rutor() +1)}
        elif not state.tomma_rutor():
            return {'position' : None, 'poäng': 0}
        
        if spelare == max_spelare:
            bästa_drag = {'position' : None, 'poäng' : -math.inf}
        else:
            bästa_drag = {'position': None, 'poäng': math.inf}

        for möjliga_drag in state.möjliga_drag():
            state.gör_drag(möjliga_drag, spelare)
            sim_poäng = self.minimax(state, annan_spelare)

            state.bräda[möjliga_drag] = ' '
            state.C_vinnare = None
            sim_poäng['position']= möjliga_drag

            if spelare == max_spelare:
                if sim_poäng['poäng']> bästa_drag['poäng']:
                    bästa_drag = sim_poäng
            else:
                if sim_poäng['poäng'] < bästa_drag['poäng']:
                    bästa_drag = sim_poäng
        return bästa_drag
   


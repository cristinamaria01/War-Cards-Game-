from carte import Carte
import random

simboluri = ['♥','♦','♣','♠']
simbol = ['inima', 'romb', 'trefla', 'frunza']
valori    = list(range(2, 15))

class Pachet:
    def __init__(self):
        self.pachet   = []
        self.pachet_1 = []
        self.pachet_2 = []

    def ConstruiestePachet(self):
        for v in valori:
            for s in simboluri:
                self.pachet.append(Carte(v,s))

    def build(self):
        for v in range(2,8):
            for s in simbol:
                self.pachet_1.append(Carte(v, s))
        self.pachet_1.append(Carte(8, 'inima'))
        self.pachet_1.append(Carte(8, 'trefla'))

        for v in range(9,15):
            for s in simbol:
                self.pachet_2.append(Carte(v, s))
        self.pachet_2.append(Carte(8, 'romb'))
        self.pachet_2.append(Carte(8, 'frunza'))

        return self

    def AfiseazaPachet(self):
        print('Pachet: ', len(self.pachet))
        for carte in self.pachet:
            carte.AfiseazaCarte()

        print('Pachet 1: ', len(self.pachet_1))
        for carte in self.pachet_1:
            carte.AfiseazaCarte()

        print('Pachet 2: ', len(self.pachet_2))
        for carte in self.pachet_2:
            carte.AfiseazaCarte()

    def ImpartePachet(self):
        for carte in self.pachet[:27]:
            c = carte.GetCarte()
            self.pachet_1.append(c)

        for carte in self.pachet[27:]:
            c = carte.GetCarte()
            self.pachet_2.append(c)

        return self

    def AmestecaPachet(self):
        random.shuffle(self.pachet)

    def TrageCarte(self):
        carte = self.pachet.pop()

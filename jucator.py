from pachet import *

class Jucator:
    def __init__(self, nume, pachet):
        self.nume        = nume
        self.pachet      = []
        self.runde_castigate = 0
        for carte in pachet:
            c = carte.GetCarte()
            self.pachet.append(c)

    def TrageCarte(self):
        #top_carte = self.pachet[0]
        #self.pachet.pop(0)
        return self.pachet.pop(0)

    def AfiseazaJucator(self):
        print(Jucator)
        print('Nume: ', self.nume)
        print('Pachet jucator: ', len(self.pachet))
        for carte in self.pachet:
            carte.AfiseazaCarte()

    def NumeJucator(self):
        return self.nume

    def IaCartile(self, carti):
        self.pachet.extend(carti)


class Carte:
    def __init__(self, valoare, simbol):
        self.simbol  = simbol
        self.valoare = valoare
    def AfiseazaCarte(self):
        if self.valoare == 11:
            print('{} {}'.format('A', self.simbol))
        elif self.valoare == 12:
            print('{} {}'.format('J', self.simbol))
        elif self.valoare == 13:
            print('{} {}'.format('Q', self.simbol))
        elif self.valoare == 14:
            print('{} {}'.format('K', self.simbol))
        else:
            print('{} {}'.format(self.valoare, self.simbol))
    def GetCarte(self):
        return self
    def ValoareCarte(self):
        return self.valoare
    def SimbolCarte(self):
        return self.simbol
    def Get(self):
        return self.valoare, self.simbol

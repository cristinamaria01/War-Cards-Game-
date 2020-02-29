from jucator import Carte, Pachet, Jucator
import sys

class Razboi:
    def __init__(self, nume1 , nume2 ):
        self.pachet_1 = []
        self.pachet_2 = []
        self.cartiPeMasa = []                      # cartile care se dueleaza intr-o runda
        self.numar_runde = 0

        """ Creez pachetul de carti """
        self.pachet   = Pachet()
        self.pachet.ConstruiestePachet()
        #self.pachet.AfiseazaPachet()
        #self.pachet.AmestecaPachet()

        """ Impart pachetul de carti la cei doi jucatori """
        pack = self.pachet.build()      #SAU: pot sa folosesc ->  pack = self.pachet.ImpartePachetul()
        for carte in pack.pachet_1:
            c = carte.GetCarte()
            self.pachet_1.append(c)
        for carte in pack.pachet_2:
            c = carte.GetCarte()
            self.pachet_2.append(c)

        """ Jucatorii """
        self.jucator_1 = Jucator(nume1, self.pachet_1)
        self.jucator_2 = Jucator(nume2, self.pachet_2)
        #self.jucator_1.AfiseazaJucator()
        #self.jucator_2.AfiseazaJucator()

    def GameOver(self):
        if len(self.jucator_2.pachet) == 0:
            print('{} a castigat jocul cu {} runde castigate!'.format(self.jucator_1.NumeJucator(),
                                                                      self.jucator_1.runde_castigate))
        elif len(self.jucator_1.pachet) == 0:
            print('{} a castigat jocul cu {} runde castigate!'.format(self.jucator_2.NumeJucator(),
                                                                      self.jucator_2.runde_castigate))



    def Razboi(self):
        print('-----RAZBOI!-----')
        if len(self.jucator_1.pachet) == 0 or len(self.jucator_2.pachet) == 0:
            self.GameOver()
        self.JoacaRunda()

    def CartiPeMasa(self, carti):
        self.cartiPeMasa.extend(carti)

    def resetCartiPeMasa(self):
        self.cartiPeMasa = []

    def JoacaRunda(self):
        if len(self.jucator_1.pachet) == 0 or len(self.jucator_2.pachet) == 0:
            return

        """ Incepe runda --> fiecare jucator trage cate o carte din propriul pachet """
        carte_jucator_1 = self.jucator_1.TrageCarte()
        carte_jucator_2 = self.jucator_2.TrageCarte()



        """ Se pun cartile pe masa """
        self.CartiPeMasa(carti = [carte_jucator_1, carte_jucator_2])

        """ Se compara cartile """
        if carte_jucator_1.valoare > carte_jucator_2.valoare:
            self.numar_runde += 1
            self.jucator_1.IaCartile(carti = self.cartiPeMasa)
            self.jucator_1.runde_castigate += 1
            print('{} --> {} {} - {} {} <-- {}\t\t Castigator runda {} este {}\t\t {}:{} carti <---> {}:{} carti'
                  .format(self.jucator_1.NumeJucator(),
                          carte_jucator_1.ValoareCarte(),
                          carte_jucator_1.SimbolCarte(),
                          carte_jucator_2.ValoareCarte(),
                          carte_jucator_2.SimbolCarte(),
                          self.jucator_2.NumeJucator(),
                          self.numar_runde,
                          self.jucator_1.NumeJucator(),
                          self.jucator_1.NumeJucator(),
                          len(self.jucator_1.pachet),
                          self.jucator_2.NumeJucator(),
                          len(self.jucator_2.pachet)))
            self.resetCartiPeMasa()
        elif carte_jucator_1.valoare < carte_jucator_2.valoare:
            self.numar_runde += 1
            self.jucator_2.IaCartile(carti= self.cartiPeMasa)
            self.jucator_2.runde_castigate += 1
            print('{} --> {} {} - {} {} <-- {}\t\t Castigator runda {} este {}\t\t {}:{} carti <---> {}:{} carti'
                  .format(self.jucator_1.NumeJucator(),
                          carte_jucator_1.ValoareCarte(),
                          carte_jucator_1.SimbolCarte(),
                          carte_jucator_2.ValoareCarte(),
                          carte_jucator_2.SimbolCarte(),
                          self.jucator_2.NumeJucator(),
                          self.numar_runde,
                          self.jucator_2.NumeJucator(),
                          self.jucator_1.NumeJucator(),
                          len(self.jucator_1.pachet),
                          self.jucator_2.NumeJucator(),
                          len(self.jucator_2.pachet)))
            self.resetCartiPeMasa()
        else:
            print('{} --> {} {} - {} {} <-- {}\t\t Se va da RAZBOI \t\t {}:{} carti <---> {}:{} carti'
              .format(self.jucator_1.NumeJucator(),
                      carte_jucator_1.ValoareCarte(),
                      carte_jucator_1.SimbolCarte(),
                      carte_jucator_2.ValoareCarte(),
                      carte_jucator_2.SimbolCarte(),
                      self.jucator_2.NumeJucator(),
                      self.jucator_1.NumeJucator(),
                      len(self.jucator_1.pachet),
                      self.jucator_2.NumeJucator(),
                      len(self.jucator_2.pachet)))
            self.Razboi()

    def IncepeJocul(self):
        print('Incepe jocul! ')
        """ Cat timp ambii jucatori au carti cu care sa joace in pachet --> Jocul continua """
        while self.jucator_1.pachet and self.jucator_2.pachet:
            self.JoacaRunda()

        if len(self.jucator_1.pachet) == 52:
            print('{} a castigat jocul cu {} runde castigate!'.format(self.jucator_1.NumeJucator(),
                                                                      self.jucator_1.runde_castigate))
        elif len(self.jucator_2.pachet) == 52:
            print('{} a castigat jocul cu {} runde castigate!'.format(self.jucator_2.NumeJucator(),
                                                                      self.jucator_2.runde_castigate))

if __name__ == '__main__':
    print(80*'-'+'WAR CARD GAME'+80*'-')
    print('Introduceti numele jucatorilor!')
    nume1 = input('Jucator 1:')
    nume2 = input('Jucator2:')

    with open('output_joc.txt', 'wt') as f:
        sys.stdout = f
        razboi = Razboi(nume1, nume2)
        razboi.IncepeJocul()
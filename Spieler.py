from Spielstein import *
from Spielbrett import *



class Spieler(object):
    def __init__(self, spielbrett, farbe):
        '''
        erzeugt ein Spieler-Objekt, dem ein Spielbrett und die Farbe uebergeben wird. Erstellt fuer den Spieler eine Liste an Spielsteinen mit der Länge aus der Multiplikation der Hoehe und der Breite des Spielbretts
        '''
        self.name = ""
        self.spielbrett = spielbrett
        self.spielsteine = []
        for i in range((self.spielbrett.getAnzahlZeilen() * self.spielbrett.getAnzahlSpalten()) // 2):
            s = Spielstein(self)
            self.spielsteine.append(s)
        self.farbe = farbe

    def setzen(self, spalte):
        '''
        ruft die setzen-Methode des Spielbretts mit der uebergebenen Spalte und dem 0. Element der Spielsteine-Liste auf.
        Anschließend wird dieses Spielstein-Objekt aus der Liste entfernt
        '''
        self.spielbrett.setzen(spalte, self.spielsteine[0])
        self.spielsteine = self.spielsteine[1:]

    def setName(self, name):
        '''
        aendert den Namen des Spielers zu dem uebergebenem Namen
        '''
        self.name = name
    
    def getName(self):
        '''
        gibt den Namen des Spielers zurueck
        '''
        return self.name
    
    def getFarbe(self):
        '''
        gibt die Farbe des Spielers zurueck
        '''
        return self.farbe
    
    def reset(self):
        '''
        macht die Spielsteine-Liste zu einer leeren Liste und bringt sie dann zu dem ursprünglichen Zustand der init-Methode zurueck
        '''
        self.spielsteine = []
        for i in range((self.spielbrett.getAnzahlZeilen() * self.spielbrett.getAnzahlSpalten()) // 2):
            s = Spielstein(self)
            self.spielsteine.append(s)


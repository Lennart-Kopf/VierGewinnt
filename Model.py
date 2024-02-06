from Spieler import *
from Spielbrett import *

class Model(object):
    def __init__(self):
        '''
        erzeugt ein Model-Objekt.
        Legt die groesse des Spielbretts fest, erschafft ein Spielbrett-Objekt, erschafft zwei Spieler-Objekte mit den Farben red und yellow und setzt den aktuellen Spieler zunaechst auf Spieler1
        '''
        self.groesse = [7, 6]
        self.spielbrett = Spielbrett(self.groesse)
        self.spieler1 = Spieler(self.spielbrett, "red")
        self.spieler2 = Spieler(self.spielbrett, "yellow")
        self.aktuellerSpieler = self.spieler1
    
    def aktuellerSpielerSetzen(self, spalte):
        '''
        laesst den aktuellen Spieler mit der uebergebenen Spalte setzen und aendert dann den aktuellen Spieler auf den anderen Spieler
        '''
        self.aktuellerSpieler.setzen(spalte)
        if self.aktuellerSpieler == self.spieler1:
            self.aktuellerSpieler = self.spieler2
        else:
            self.aktuellerSpieler = self.spieler1
    
    def setzenLegal(self, spalte):
        '''
        gibt den Rueckgabewert der Methode setzenLegal des Spielbrett-Objekts mit der uebergebenen Spalte zurueck
        '''
        return self.spielbrett.setzenLegal(spalte)
    
    def spielerBenennen(self, spieler, name):
        '''
        setzt den Namen des Spielers auf den uebergebenen Text
        '''
        spieler.setName(name)
    
    def voll(self):
        '''
        gibt den Rueckgabewert der Methode voll des Spielbrett-Objekts zurueck
        '''
        return self.spielbrett.voll()
    
    def getSpielerListe(self):
        '''
        gibt Spieler 1 und 2 als Liste zurueck
        '''
        return [self.spieler1, self.spieler2]
    
    def getSpielerName(self, spieler):
        '''
        gibt den Namen des uebergebenen Spielers zurueck
        '''
        return spieler.getName()
    
    def getGroesse(self):
        '''
        gibt die Liste der groesse des Spielbretts zurueck
        '''
        return self.groesse
    
    def getAktuellerSpieler(self):
        '''
        gibt den aktuellen Spieler zurueck
        '''
        return self.aktuellerSpieler
    
    def getFelder(self):
        '''
        gibt die Felder-Liste des Spielbrett-Objekts zurueck
        '''
        return self.spielbrett.getFelder()
    
    def gewonnen(self):
        '''
        gibt den Rueckgabewert des Methode gewonnen des Spielbrett-Objekts zurueck
        '''
        return self.spielbrett.gewonnen()

    def reset(self):
        '''
        fuehrt die reset Methode des Spielbretts und der Spieler aus und setzt den aktuellen Spieler wieder auf Spieler 1
        '''
        self.spielbrett.reset()
        self.spieler1.reset()
        self.spieler2.reset()
        self.aktuellerSpieler = self.spieler1
    
    def getVorherigenSpieler(self):
        '''
        gibt den Spieler zurueck, der nicht gerade der aktuelle Spieler ist
        '''
        if self.aktuellerSpieler==self.spieler1:
            return self.spieler2
        else:
            return self.spieler1
    
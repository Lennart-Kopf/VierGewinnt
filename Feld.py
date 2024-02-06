from Spielstein import *
from Spieler import *

class Feld(object):
    def __init__(self):
        '''
        erzeugt ein Feld-Objekt, dem zunaechst kein Spielstein-Objekt zugeordnet ist
        '''
        self.spielstein = None

    def setSpielstein(self, spielstein):
        '''
        ordet dem Spielstein-Attribut das uebergebene Spielstein-Objekt zu
        '''
        self.spielstein = spielstein

    def getSpielstein(self):
        '''
        gibt das Spielstein-Objekt zurueck
        '''
        return self.spielstein
    
    def getSpieler(self):
        '''
        gibt den Spieler des Spielsteins, der sich auf dem Feld befindet zurueck
        '''
        if self.spielstein != None:
            return self.spielstein.getSpieler()
        else:
            return None
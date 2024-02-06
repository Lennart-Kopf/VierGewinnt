from Spieler import *

class Spielstein(object):
    def __init__(self, spieler):
        '''
        erzeugt ein Spielstein-Ojekt
        '''
        self.spieler = spieler
    
    def getSpieler(self):
        '''
        gibt den Spieler des Spielsteins zurueck
        '''
        return self.spieler
from Feld import *

class Spielbrett(object):
    def __init__(self, groesse):
        '''
        erzeugt ein Spielbrett-Objekt, das zunaechst eine Liste an Feldern abhaengig von der Anzahl der Spalten und der Zeilen besitzt.
        Diese Feld-Objekte sind dann noch in Spalten und Diagonalen geordnet.
        Den Attributen anzahlSpalten und anzahlZeilen werden die uebergebenen Werte zugewiessen
        '''
        self.felder = []
        self.anzahlSpalten = groesse[0]
        self.anzahlZeilen = groesse[1]
        self.spalten = []
        self.diagonalen = []

        #erzeugt das Spielbrett in Reihen
        for i in range(self.anzahlZeilen):
            zeile = []
            for j in range(self.anzahlSpalten):
                f = Feld()
                zeile.append(f)
            self.felder.append(zeile)
        
        #erzeugt eine Liste der Felder in Spalten
        for i in range(self.anzahlSpalten):
            spalte = []
            for j in self.felder:
                spalte.append(j[i])
            self.spalten.append(spalte)

        #erzeugt eine Liste der Felder in Diagonalen, deren Laenge mindestens 4 Felder sind
        #erste Zeile rechts diagonal
        for i in range(len(self.felder[0])):
            l = []
            l.append(self.felder[0][i])
            for j in range(1, len(self.felder)):
                if i + j <= self.anzahlSpalten - 1:
                    l.append(self.felder[j][i + j])
            if len(l) >= 4:
                self.diagonalen.append(l)
        
        #erste Zeile links diagonal
        for i in range(len(self.felder[0])):
            l = []
            l.append(self.felder[0][i])
            for j in range(1, len(self.felder)):
                if i - j >= 0:
                    l.append(self.felder[j][i - j])
            if len(l) >= 4:
                self.diagonalen.append(l)
        
        #erste Spalte rechts diagonal
        for i in range(1, len(self.spalten[0])):
            l = []
            l.append(self.spalten[0][i])
            for j in range(1, len(self.spalten)):
                if i + j <= self.anzahlZeilen - 1:
                    l.append(self.spalten[j][i+j])
            if len(l) >= 4:
                self.diagonalen.append(l)
        
        #letzte Spalte links diagonal
        for i in range(1, len(self.spalten[len(self.spalten) - 1])):
            l = []
            l.append(self.spalten[len(self.spalten) - 1][i])
            for j in range(1, len(self.spalten)):
                if i + j <= self.anzahlZeilen - 1:
                    l.append(self.spalten[len(self.spalten) - 1- j][i+j])
            if len(l) >= 4:
                self.diagonalen.append(l)

    def gewonnen(self):
        '''
        prueft, ob es in den Zeilen, Spalten oder Diagonalen 4 nebeneinander liegende Spielsteine eines Spielers gibt.
        Falls ja wird True zurueckgegeben, falls nein False
        '''
        #prueft die Zeilen
        for i in self.felder:
            for j in range(self.anzahlSpalten - 3):
                if i[j].getSpieler() == i[j+1].getSpieler() and i[j].getSpieler() == i[j+2].getSpieler() and i[j].getSpieler() == i[j+3].getSpieler() and i[j].getSpieler() != None:
                    return True

        #prueft die Spalten
        for i in self.spalten:
            for j in range(self.anzahlZeilen - 3):
                if i[j].getSpieler() == i[j+1].getSpieler() and i[j].getSpieler() == i[j+2].getSpieler() and i[j].getSpieler() == i[j+3].getSpieler() and i[j].getSpieler() != None:
                    return True

        #prueft die Diagonalen
        for i in self.diagonalen:
            for j in range(len(i) - 3):
                if i[j].getSpieler() == i[j+1].getSpieler() and i[j].getSpieler() == i[j+2].getSpieler() and i[j].getSpieler() == i[j+3].getSpieler() and i[j].getSpieler() != None:
                    return True
        return False

    def getAnzahlSpalten(self):
        '''
        gibt anzahlSpalten zurueck
        '''
        return self.anzahlSpalten
    
    def getAnzahlZeilen(self):
        '''
        gibt anzahlZeilen zurueck
        '''
        return self.anzahlZeilen

    def setzen(self, spalte, spielstein):
        '''
        weist dem ersten Feld von unten der uebergebenen Spalte das uebergebene Spielstein-Objekt dem Spielstein-Attribut des Feld-Objekts zu
        '''
        zaehler = len(self.spalten[spalte]) - 1
        while zaehler >= 0:
            if self.spalten[spalte][zaehler].getSpielstein() == None:
                self.spalten[spalte][zaehler].setSpielstein(spielstein)
                break
            zaehler -= 1

    def setzenLegal(self, spalte):
        '''
        prueft, ob es in der uebergebenen Spalte mindestens ein Feld gibt, dass noch kein Spielstein kennt.
        Falls ja, wird True zurueckgegeben, falls nein, False.
        '''
        for i in self.spalten[spalte]:
            if i.getSpielstein() == None:
                return True
        return False
    
    def voll(self):
        '''
        prueft, ob es in der gesamten Zahl an Feldern, noch ein Feld ohne Spielstein-Objekt gibt.
        Falls ja, wird True und falls nein, wird False zurueckgegeben.
        '''
        for i in self.felder:
            for j in i:
                if j.getSpielstein() == None:
                    return False
        return True
    
    def getFelder(self):
        '''
        gibt die Liste der Felder zruueck
        '''
        return self.felder
    
    def reset(self):
        '''
        setzt bei jedem Feld-Objekt das Spielstein-Attribut auf None
        '''
        for i in self.felder:
            for j in i:
                j.setSpielstein(None)


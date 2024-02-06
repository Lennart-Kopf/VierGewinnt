from Model import *
from GUI import *

class Controller(object):
    def __init__(self):
        '''
        erzeugt ein Model-Objekt und ein GUI-Objekt, dem die Groesse des Spielbretts uebergeben wird und mehrere Methoden, die ausgefuehrt werden, wenn die entsprechen Button gedrueckt werden
        '''
        self.model = Model()
        self.gui = GUI(self.model.getGroesse(), self.cmdStart, self.cmdSetzen, self.cmdNochmal)
        self.gui.guiStarten()

    def cmdStart(self):
        '''
        prueft, ob die Spielernamen gueltig sind und uebergibt diese an das Model.
        Anschliessend wird der Spielbildschirm angezeigt und die Spieleranzeige zu dem aktuellen Spieler geaendert
        '''
        if self.gui.getSpieler2() == "" or self.gui.getSpieler1() == "":
            self.gui.falscheEingabe()
        else:
            self.model.spielerBenennen(self.model.getSpielerListe()[0], self.gui.getSpieler1())
            self.model.spielerBenennen(self.model.getSpielerListe()[1], self.gui.getSpieler2())
            self.gui.configSpielerAnzeige(self.model.getAktuellerSpieler().getName())
            self.gui.disableStart()
            self.gui.placeSpielbildschirm()
        
    def cmdSetzen(self, spalte):
        '''
        laesst den aktuellen Spieler setzen, aktualisiert die Spieleranzeige, prueft ob das Setzen in den Spalten legal ist, wenn nicht wird der zugehoerige Button deaktiviert,
        zeichnet das Spielfeld, prueft ob jemand gewonnen hat und gibt dann das Endefenster mit Sieger aus und wenn nicht prueft, ob das Spielbrett voll ist und das Spiel
        dementsprechend unentschieden endet
        '''
        self.model.aktuellerSpielerSetzen(spalte)
        self.gui.configSpielerAnzeige(self.model.getAktuellerSpieler().getName())
        for i in range(self.model.getGroesse()[0]):
            if self.model.setzenLegal(i) == False:
                self.gui.disableButton(i)
        self.spielfeldZeichnen()
        if self.model.gewonnen():
            for i in range(self.model.getGroesse()[0]):
                self.gui.disableButton(i)
            self.gui.configErgebnisTitle("Gewonnen")
            self.gui.configErgebnisLabel("{} hat gewonnen".format(self.model.getVorherigenSpieler().getName()))
            self.gui.ausgabeEnde()
        
        elif self.model.voll():
            for i in range(self.model.getGroesse()[0]):
                self.gui.disableButton(i)
            self.gui.configErgebnisTitle("Unentschieden")
            self.gui.configErgebnisLabel("Unentschieden")
            self.gui.ausgabeEnde()
            
    def spielfeldZeichnen(self):
        '''
        zeichnet das Spielfeld, indem alle Felder des Spielbretts durchlaufen werden und dann die Felder der GUI nach der Farbe des Spielers geaendert werden
        '''
        brett = self.model.getFelder()
        for i in range(self.model.getGroesse()[1]):
            for j in range(self.model.getGroesse()[0]):
                if brett[i][j].getSpielstein() != None:
                    self.gui.farbeAendern([i, j], brett[i][j].getSpieler().getFarbe())
                else:
                    self.gui.farbeAendern([i, j], "white")
    
    def cmdNochmal(self):
        '''
        fuehrt reset fuer das Model und die GUI durch, zeichnet das Spielfeld und schliesst das Ende-Fenster und aktualisiert die Spieler-Anzeige
        '''
        self.model.reset()
        self.gui.reset()
        self.spielfeldZeichnen()
        self.gui.entferneEnde()
        self.gui.configSpielerAnzeige(self.model.getAktuellerSpieler().getName())

c = Controller()

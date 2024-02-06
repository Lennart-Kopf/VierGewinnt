from tkinter import *
from tkinter import messagebox
from functools import partial


class GUI(object):
    def __init__(self, groesse, cmdStart, cmdSetzen, cmdNochmal):
        '''
        erzeugt ein Vier Gewinnt GUI-Objekt, weist den anzahlSpalten und anzahlReihen die uebergebenen Groessen zu
        '''
        self.root = Tk()
        self.cmdSetzen = cmdSetzen
        self.root.geometry("1000x1000")
        self.root.resizable(False, False)
        self.root.title("Vier gewinnt")
        self.anzahlSpalten = groesse[0]
        self.anzahlReihen = groesse[1]

        #Startbildschirm
        self.frameStart = Frame(master=self.root, bg="red")
        self.frameStart.place(x=0, y=0, width=1000, height=1000)

        self.labelTitel = Label(master=self.frameStart, bg="white", text="Vier Gewinnt", font=("Arial", 25))
        self.labelTitel.place(x=40, y=40, width=920, height=100)

        self.labelSpieler1 = Label(master=self.frameStart, bg="white", text="Spieler 1:", font=("Arial", 12))
        self.labelSpieler1.place(x=300, y=400, width=200, height=50)

        self.labelSpieler2 = Label(master=self.frameStart, bg="white", text="Spieler 2:", font=("Arial", 12))
        self.labelSpieler2.place(x=300, y=450, width=200, height=50)

        self.entrySpieler1 = Entry(master=self.frameStart, bg="white", font=("Arial", 12))
        self.entrySpieler1.place(x=500, y=400, width=200, height=50)

        self.entrySpieler2 = Entry(master=self.frameStart, bg="white", font=("Arial", 12))
        self.entrySpieler2.place(x=500, y=450, width=200, height=50)

        #erstellt den Startbutton, an den den die Methoden cmdStart gebunden ist
        self.buttonStart = Button(master=self.frameStart, bg="white", text="Start", font=("Arial", 12), command=cmdStart)
        self.buttonStart.place(x=400, y=600, width=200, height=100)

        #Spielbildschirm
        self.frameSpiel = Frame(master=self.root, bg="black")

        self.labelAktuellerSpieler = Label(master=self.frameSpiel, text="", font=("Arial", 12), bg="white")
        self.labelAktuellerSpieler.place(x=5, y=10, width=990, height=50)

        #Spielfeld
        self.canvasBrett = Canvas(master=self.frameSpiel, bg = "blue")
        self.canvasBrett.place(x=150, y=200, width=700, height=600)

        #erstellt die Ovale des Spielfeld-Canvas
        self.felder = []

        for i in range(self.anzahlReihen):
            reihe = []
            for j in range(self.anzahlSpalten):
                f = self.canvasBrett.create_oval((700 / self.anzahlSpalten) * 0.1 + (700 / self.anzahlSpalten) * j, (600 / self.anzahlReihen) * 0.1 + (600 / self.anzahlReihen) * i, (700 / self.anzahlSpalten) * 0.9 + (700 / self.anzahlSpalten) * j, (600 / self.anzahlReihen) * 0.9 + (600 / self.anzahlReihen) * i, fill="white")
                reihe.append(f)
            self.felder.append(reihe)
        
        #erstellt die Button der einzelnen Spalten, werden die Buttons gedrueckt, wird cmdSetzen mit der Zahl der Spalte als Paramater ausgefuehrt
        self.buttonSetzen = []
        for i in range(self.anzahlSpalten):
            b = Button(master=self.frameSpiel, text="Spalte {}".format(i + 1), command=partial(cmdSetzen, i))
            b.place(x=150 + 700/self.anzahlSpalten * i, y=160, width=700/self.anzahlSpalten, height=40)
            self.buttonSetzen.append(b)
        
        #Ende-Bildschirm
        self.fensterEnde = Toplevel()
        self.fensterEnde.title("")
        self.fensterEnde.geometry("400x400")
        self.labelErgebnis = Label(master=self.fensterEnde, text="", bg="blue", font=("Arial", 10), foreground="white")
        self.labelErgebnis.place(x=50, y=20, width=300, height=50)
        #erstellt den buttonNochmal, an den die Methode cmdNochmal gebunden ist
        self.buttonNochmal = Button(master=self.fensterEnde, text="Nochmal spielen", font=("Arial", 10), command = cmdNochmal)
        self.buttonNochmal.place(x = 25, y=300, width=150, height=50)
        #erstellt den buttonBeenden, bei dem die Methode cmdBeenden ausgefuehrt wird, wenn er gedrueckt wird
        self.buttonBeenden = Button(master=self.fensterEnde, text="Beenden", font=("Arial", 10), command = self.cmdBeenden)
        self.buttonBeenden.place(x = 225, y=300, width=150, height=50)
        self.fensterEnde.withdraw()
    
    
    def placeSpielbildschirm(self):
        '''
        platziert den Frame des Spielbildschirms
        '''
        self.frameSpiel.place(x=0, y=0, width=1000, height=1000)
    
    def getSpieler1(self):
        '''
        gibt den eingebenen Namen von Spieler 1 zurueck
        '''
        return self.entrySpieler1.get()

    def getSpieler2(self):
        '''
        gibt den eingebenen Namen von Spieler 2 zurueck
        '''
        return self.entrySpieler2.get()
    
    def disableStart(self):
        '''
        laesst den Start-Frame verschwinden
        '''
        self.frameStart.forget()
    
    def guiStarten(self):
        '''
        startet die mainloop der GUI
        '''
        self.root.mainloop()
    
    def configSpielerAnzeige(self, name):
        '''
        aendert das Label fuer den aktuellen Spieler mit dem uebergebenem Namen
        '''
        self.labelAktuellerSpieler.config(text="{} ist am Zug".format(name))
    
    def falscheEingabe(self):
        '''
        zeigt eine Fehlanzeige an, dass die Eingabe nicht sinnvoll war
        '''
        messagebox.showerror("Fehler", "Keine sinnvolle Eingabe fuer einen Namen")
    
    def disableButton(self, zahl):
        '''
        deaktiviert den Button aus der Button-Liste mit dem uebergebenen Index
        '''
        self.buttonSetzen[zahl].config(state=DISABLED)
    
    def aktiviereButton(self, zahl):
        '''
        aktiviert den Button aus der Button-Liste mit dem uebergebenen Index
        '''
        self.buttonSetzen[zahl].config(state=ACTIVE)
    
    def getFelder(self):
        '''
        gibt die Ovale des Spielbrett-Objekts zurueck
        '''
        return self.felder
    
    def farbeAendern(self, index, farbe):
        '''
        aendert die Farbe des Ovals, dessen Index uebergeben wird, mit der uebergebenen Farbe
        '''
        self.canvasBrett.itemconfig(self.felder[index[0]][index[1]], fill=farbe)
    
    def ausgabeEnde(self):
        '''
        laesst das Ende-Fenster erscheinen
        '''
        self.fensterEnde.deiconify()
    
    def configErgebnisLabel(self, text):
        '''
        aendert den Text des Ergebnis-Labels zu dem uebergebenen Text
        '''
        self.labelErgebnis.config(text="{}".format(text))
    
    def configErgebnisTitle(self,text):
        '''
        aendert den Titel des Ende-Fensters zu dem uebergebenen Text
        '''
        self.fensterEnde.title("{}".format(text))
    
    def reset(self):
        '''
        aktiviert alle Buttons
        '''
        for i in range(len(self.buttonSetzen)):
            self.aktiviereButton(i)
    
    def entferneEnde(self):
        '''
        laesst das Ende Fenster verschwinden
        '''
        self.fensterEnde.withdraw()
    
    def cmdBeenden(self):
        '''
        beendet das Tkinter-Programm
        '''
        self.root.destroy()
    

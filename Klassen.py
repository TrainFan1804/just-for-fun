class Toaster:  # (Objekt)Klassen groß schreiben

    def __init__(self, schaechte, farbe,
                 zeit):  # Kunstruktor = Einrichtungsfunktion um Eigenschaften neuen Objekten zu geben
        self.schaechte = schaechte
        self.farbe = farbe
        self.toast_zeit = zeit
        self.anzahl_toast = 0
        self.brot_zustand = 0

    def __str__(self):  # __str__ wird ausgeführt wenn, Objekt als Text ausgegeben werden soll
        antwort = "Das Objekt ist ein Toaster. "
        antwort += "Die Farbe ist " + self.farbe + ". "
        antwort += "Er hat " + str(self.schaechte) + " Schächte. "
        antwort += "Im Moment sind " + str(self.anzahl_toast) + " Toast drinnen. "
        antwort += "Der Zustand des Toast ist " + str(self.brot_zustand) + ". "
        antwort += "Der Timer ist auf " + str(self.toast_zeit) + " Sekunden eingestellt."
        return antwort

    def toastReintun(self, anzahl):  # Methoden (Klassenfunktionen) in camelCase schreiben
        if (self.anzahl_toast + anzahl) > self.schaechte:
            return "Nicht genug Platz!"
        else:
            self.anzahl_toast = self.anzahl_toast + anzahl
            return str(anzahl) + " Toast reingetan."

    def toasten(self):
        if self.anzahl_toast > 0:
            zeit = self.toast_zeit
            if zeit <= 20:
                self.brot_zustand += 1
            if zeit > 20:
                self.brot_zustand += 2
            if zeit >= 40:
                self.brot_zustand += 3
            if self.brot_zustand > 3:
                self.brot_zustand = 3
            zustand = ["ungetoastet", "leicht getoastet", "stark getoastet", "verbrannt"]
            return str(zeit) + " Sekunden vergangen, Toast ist Fertig. Das Brot ist " + zustand[self.brot_zustand] + "."
        else:
            return "Toaster ist leer."

    def toastAuswerfen(self):
        zustand = ["ungetoastet", "leicht getoastet", "stark getoastet", "verbrannt"]
        info = str(self.anzahl_toast) + " Mal Toast ausgeworfen. Zustand: " + zustand[self.brot_zustand]
        self.anzahl_toast = 0
        self.brot_zustand = 0
        return info


class SuperToaster(Toaster):
    temperatur = 300

    def temptoasten(self):
        if self.temperatur > 500:
            return "Zu heiß!"
        elif self.temperatur < 100:
            return "Zu kalt!"
        else:
            return self.toasten()


mein_toaster = Toaster(5, "rot", 30)  # Objekt der Klasse Toaster, Objekte in snake_case schreiben
print(mein_toaster.toastReintun(3))
print(mein_toaster.anzahl_toast)
print(mein_toaster.toastReintun(4))
print(mein_toaster)
print(mein_toaster.toasten())
print(mein_toaster.toastAuswerfen())
print(mein_toaster)
print()
super_toaster = SuperToaster(2, "blau", "15")
super_toaster.toastReintun(2)
super_toaster.temperatur = 250

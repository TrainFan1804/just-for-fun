menge = 1
summe = 0
feld = 1
for i in range(64):
    summe = summe + menge
    menge = menge * 2
    print("Auf Feld", feld, "sind", menge, "Reiskörner")
    feld = feld + 1
print()
print("Reiskörner insgesamt:", summe)
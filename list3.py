import random


vokabeln = [["Tisch", "table"], ["Auto", "car"], ["Katze", "cat"]]
random.shuffle(vokabeln)
richtig = 0
falsch = 0
for vok in vokabeln:
    eingabe = input("Was heißt " + vok[0] + "?")
    if eingabe == vok[1]:
        print("Richtig")
        richtig += 1
    else:
        print("Falsch")
        falsch += 1

print("Du hast", richtig, "richtig, und", falsch, "Falsch")

def zahlwort(zahl):
    einer = ["null", "ein", "zwei", "drei", "vier", "fünf", "sechs", "sieben", "acht", "neun", "zehn", "elf", "zwölf",
             "dreizehn", "vierzehn", "fünfzehn", "sechzehn", "siebzehn", "achtzehn", "neunzehn"]
    zehner = ["null", "zehn", "zwanzig", "dreizig", "vierzig", "fünfzig", "sechzig", "siebzig", "achtzig", "neunzig"]
    hunderter = ["hundert", "tausend"]
    wort = None
    if zahl < 20:
        wort = einer[zahl]
        if zahl == 1:
            wort = "eins"
    elif 20 <= zahl < 100:
        z = zahl // 10
        e = zahl % 10
        wort = einer[e] + "und" + zehner[z]
        if e == 0:
            wort = zehner[z]
    elif zahl >= 100:
        h = zahl // 100
        z = (zahl % 100) // 10
        e = ((zahl % 100) % 10)
        wort = einer[h] + hunderter[0] + einer[e] + "und" + zehner[z]
        if z == 0:
            wort = einer[h] + hunderter[0] + einer[e]
            if e == 1:
                wort = einer[h] + hunderter[0] + einer[e] + "s"
        if e == 0:
            wort = einer[h] + hunderter[0] + zehner[z]
        if e == 0 and z == 0:
            wort = einer[h] + hunderter[0]
    return wort


while True:
    number = input()
    if int(number) <= 1000:
        print(str(number) + " ist in Worten: " + zahlwort(int(number)))
    else:
        print(str(number) + " ist zu hoch!")

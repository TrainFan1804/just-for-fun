import random


def correct_result():
    print("---------------\n"
          "Richtig!\n"
          "---------------")


def wrong_result(result):
    print("---------------\n"
          "Leider falsch. Die richtige Lösung wäre: " + str(result) + "\n"
          "---------------")


rArt = random.randint(3, 3)

if rArt == 0:
    print("---------------\n"
          "Addieren\n"
          "---------------\n")
    number_range = input("Zahlenraum eingeben (Mit Komma getrennt): ")
    print()
    numbers_string = number_range.split(",")    # Komma wird entfernt
    numbers_int = list(map(int, numbers_string))    # Zahlen werden in liste übertragen
    a = random.randint(numbers_int[0], numbers_int[1])  # züfällige zahlen werden generiert
    b = random.randint(numbers_int[0], numbers_int[1])
    c = a + b
    userResult = int(input("Was ist " + str(a) + " + " + str(b) + ": "))
    print()
    if userResult == c:
        correct_result()
    else:
        wrong_result(c)

elif rArt == 1:
    print("---------------\n"
          "Subtrahieren\n"
          "---------------")
    number_range = input("Zahlenraum eingeben (Mit Komma getrennt): ")
    print()
    numbers_string = number_range.split(",")
    numbers_int = list(map(int, numbers_string))
    a = random.randint(numbers_int[0], numbers_int[1])
    b = random.randint(numbers_int[0], numbers_int[1])
    c = a - b
    userResult = int(input("Was ist " + str(a) + " - " + str(b) + ": "))
    print()
    if userResult == c:
        correct_result()
    else:
        wrong_result(c)

elif rArt == 2:
    print("---------------\n"
          "Multiplizieren\n"
          "---------------")
    number_range = input("Zahlenraum eingeben (Mit Komma getrennt): ")
    print()
    numbers_string = number_range.split(",")
    numbers_int = list(map(int, numbers_string))
    a = random.randint(numbers_int[0], numbers_int[1])
    b = random.randint(numbers_int[0], numbers_int[1])
    c = a * b
    userResult = int(input("Was ist " + str(a) + " * " + str(b) + ": "))
    print()
    if userResult == c:
        correct_result()
    else:
        wrong_result(c)

else:
    print("---------------\n"
          "Dividieren\n"
          "---------------")
    number_range = input("Zahlenraum eingeben (Mit Komma getrennt): ")
    print()
    numbers_string = number_range.split(",")
    numbers_int = list(map(int, numbers_string))
    a = random.randint(numbers_int[0], numbers_int[1])
    b = random.randint(numbers_int[0], numbers_int[1])
    c = a / b
    cRound = round(c, 2)
    userResult = float(input("Was ist " + str(a) + " : " + str(b) + ": "))
    print()
    if userResult == cRound:
        correct_result()
    else:
        wrong_result(cRound)

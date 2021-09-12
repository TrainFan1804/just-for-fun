def to_number(buchstabe):
    number = ord(buchstabe) - ord("a")
    return number


def to_buchstabe(number):
    buchstabe = chr(number + ord("a"))
    return buchstabe


def verschieben(buchstabe, schlüssel):
    number_buchstabe = to_number(buchstabe)
    number_neuer_buchstabe = number_buchstabe + schlüssel
    number_neuer_buchstabe = (number_neuer_buchstabe % 26)
    neuer_buchstabe = to_buchstabe(number_neuer_buchstabe)
    return neuer_buchstabe

print(verschieben("a", 2))
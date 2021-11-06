alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def verschlüsseln(text, key):
    digit_text  = ""
    for character in text:
        if character.isalpha():
            character = character.lower()
            char_index = alphabet.index(character)
            new_index = (char_index + key) % 26
            cipher_char = alphabet[new_index].upper()
        else:
            cipher_char = character

        digit_text += cipher_char

    print("Your ciphertext is: " + digit_text)

def entschlüsseln(ciphertext, schlüssel):
    klartext = ""
    for character in ciphertext:
        if character.isalpha():
            character = character.lower()
            char_index = alphabet.index(character)
            new_index = (char_index - schlüssel) % 26
            plain_char = alphabet[new_index]
        else:
            plain_char = character

        klartext += plain_char

    print("your plaintext is: " + klartext)


verschlüsseln("password here", 804)

entschlüsseln("RFC08MUJ-&4FMSQC", 804)

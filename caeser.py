# Convert letter to a number // look at the ascii schedule
def to_number(letter):
    number = ord(letter) - ord("a")
    return number


# Convert a number to a letter // look at the ascii
def to_letter(number):
    letter = chr(number + ord("a"))
    return letter


# Switch a letter to a new number // the new letter is moved by the key value
def switch(letter, key):
    number_from_letter = to_number(letter)
    number_new_from_letter = number_from_letter + key
    number_new_from_letter = (number_new_from_letter % 26)
    new_letter = to_letter(number_new_from_letter)
    return new_letter


def caeser_cipher(word, key):
    secret_text = ""
    for letter in word:
        if letter == " ":
            secret_text = secret_text + " "
        else:
            secret_text = secret_text + switch(letter, key)
    return secret_text


def caeser_decipher(secret_text, key):
    decode_text = caeser_cipher(secret_text, -key)
    return decode_text


def brute_force_attack(secret_text):
    key = 0
    while key < 27:
        decode_text = caeser_decipher(secret_text, key)
        key += 1
        print("Schlüssel: %s" % (key))
        print("Klartext: %s" % (decode_text))

print(to_number("h"))
print(to_letter(7))
print(switch("h", 1))
print()
print(caeser_cipher("hi", 3))
print(caeser_decipher("ibmmp ev", 1))
print(brute_force_attack("pl hxkk jxk gbabk qbuq bkqpzeirbppbik rka axp kro jfq cg sboprzebk axp dbeq wr bfkcxze labo"))
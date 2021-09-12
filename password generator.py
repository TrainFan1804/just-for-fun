import random


list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
        "v", "w", "x", "y", "z", ""]

password = []
lenght = 6
for i in range(lenght):
    letter = list[random.randint(0, 25)]
    password.append(letter)

print(password)
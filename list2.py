import random


list = [0, 0, 0, 0, 0, 0]
for i in range(10000):
    number = random.randint(1, 6)
    list[number - 1] = list[number - 1] + 1
for z in range(6):
    print(z + 1, ":", list[z])

import random


list = []
for i in range(50):
    list.append(i + 1)

random.shuffle(list)
print(list[:6])


import random


trys = 1
userNumber = []
while trys <= 6:
    nInput = int(input("Enter a number: "))
    if nInput in userNumber:
        print("Already taken")
    elif nInput >= 49 or nInput <= 1:
        print("Invalid input")
    else:
        userNumber.append(nInput)
        trys += 1

userNumber.sort()

lotto = random.sample(range(1, 50), 6)
lotto.sort()

print(userNumber)
print(lotto)

correctNumbers = 0
for i in userNumber:
    if i in lotto:
        correctNumbers =+ correctNumbers
print("Correct tips: ", correctNumbers)

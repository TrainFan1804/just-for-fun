def rekursiv(x):
    print(x)
    if x < 100:
        rekursiv(x + 1)

def fakultät(x):
    if x == 1:
        return 1
    else:
        return (x * fakultät(x - 1))

print(fakultät(6))
import time


start = int(input("Zum starten 1 Drücken: "))
timer = 10
if start == 1:
    for i in range(10):
        print(timer)
        timer += 1
        time.sleep(1)


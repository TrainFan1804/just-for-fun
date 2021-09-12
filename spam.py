import time
import keyboard


for i in range(4):
    print("Start in:",3 - i)
    time.sleep(1)
    if i == 3:
        print("Start: Jetzt")
print()

x = 0
while x <= 1000:
    keyboard.write(str(x))
    keyboard.press("enter")
    time.sleep(0.1)
    print(x)
    x += 1
    if keyboard.is_pressed("esc"):
        break

from tkinter import *


root = Tk()
root.geometry("200x150")
root.title("First")

frame = Frame(root, bg="red", bd="3")
frame.pack()

left_frame = Frame(root, bg="blue", bd="3")
left_frame.pack(side=LEFT)

right_frame = Frame(root, bg="green", bd="3")
right_frame.pack(side=RIGHT)

label = Label(frame, text="Hello World")
label.pack()

button1 = Button(left_frame, text="Button1")
button1.pack(padx=3, pady=3)
button2 = Button(right_frame, text="Button2")
button2.pack(padx=3, pady=3)
button3 = Button(left_frame, text="Button3")
button3.pack(padx=3, pady=3)
root.mainloop()

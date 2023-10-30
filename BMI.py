from tkinter import *

root = Tk()
root.title("BMI CALCULATOR")
root.configure(width=153, height=108)
root.configure(bg="black")

height = DoubleVar()
h_label = Label(root, text="height", fg="red", bg="black", font=("Calibri 14 bold"), pady=6, padx=9)
heigh = Entry(root, textvariable=height)
h_label.grid(row=2, column=1, columnspan=2, padx=6)

weight = DoubleVar()
w_label = Label(root, text="height", fg="red", bg="black", font=("Calibri 14 bold"), pady=9, padx=3)
weigh = Entry(root, textvariable=weight)
w_label.grid(row=4)
weigh.grid(row=4, column=1)

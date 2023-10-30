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

bmi_Val = DoubleVar()
stat = StringVar()
bmi = Label(root, text="BMI",fg="blue", bg="black", font=("Calibri 14 bold"), padx=3, pady=9, justify=LEFT)
status = Label(root, text="Status", fg="blue", bg="black", font=("Calibri 14 bold"), padx=3, pady=9)
status_msg = Label(root, textvariable=stat, fg="white", bg="black", font=("Calibri 14 bold"), padx=3, pady=9 )
BMI_Total = Label(root, textvariable=bmi_Val, fg="white", bg="black", font=("Calibri 14 bold"), padx=3, pady=9)

bmi.grid(row=6)
status.grid(row=7)
BMI_Total.grid(row=6, column=1)
status_msg.grid(row=7, column=1)

calculate = Button(root, text="Calculate",fg="black", bg="white", font=("Calibri 12 bold"))
clear = Button(root, text="Reset", fg="black", bg="white", font=("Calibri 14 bold"))

calculate.grid(row=8)
clear.grid(row=8, column=3)
root.mainloop()








import tkinter
#creatin the window
root = tkinter.Tk()
root.title("Calculator")

expression = ""
#CREATE FUNCTIONS 
def add(value):
    global expression
    expression = expression+value
    label_result.config(text=expression)


def clear():
    global expression
    expression = ""
    label_result.config(text=expression)


def calculate():
    global expression
    result = ""
    if expression!= "":
        try:
            result = eval(expression)           
        except:
            result = "error"
            expression = ""
    label_result.config(text=result)
    expression = str(result)

#CREATE GUI 
#creating the layout
label_result = tkinter.Label(root, text="")
label_result.grid(row=0, column=0, columnspan=4)
#buttons of row 1
button_1 = tkinter.Button(root, background="#9E9FA5", text="1",width=4, command=lambda: add("1"))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, background="#9E9FA5", text="2",width=4, command=lambda: add("2"))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, background="#9E9FA5", text="3",width=4, command=lambda: add("3"))
button_3.grid(row=1, column=2)

button_divide = tkinter.Button(root, background="#9E9FA5", text="/", width=4, command=lambda: add("/"))
button_divide.grid(row=1, column=3)

#buttons of row 2
button_4 = tkinter.Button(root, background="#9E9FA5", text="4", width=4, command=lambda: add("4"))
button_4.grid(row=2, column=0)

button_5 = tkinter.Button(root, background="#9E9FA5", text="5", width=4, command=lambda: add("5"))
button_5.grid(row=2, column=1)

button_6 = tkinter.Button(root, background="#9E9FA5", text="6", width=4, command=lambda: add("6"))
button_6.grid(row=2, column=2)

button_multiply = tkinter.Button(root, background="#9E9FA5", text="*", width=4, command=lambda: add("*"))
button_multiply.grid(row=2, column=3)

#buttons of row 3
button_7 = tkinter.Button(root, background="#9E9FA5", text="7", width=4, command=lambda: add("7"))
button_7.grid(row=3, column=0)

button_8 = tkinter.Button(root, background="#9E9FA5", text="8", width=4, command=lambda: add("8"))
button_8.grid(row=3, column=1)

button_9 = tkinter.Button(root, background="#9E9FA5", text="9", width=4, command=lambda: add("9"))
button_9.grid(row=3, column=2)

button_substract = tkinter.Button(root, background="#9E9FA5", text="-", width=4, command=lambda: add("-"))
button_substract.grid(row=3, column=3)

#buttons of row 4
button_clear = tkinter.Button(root, background="#9E9FA5", text="C", width=4, command=lambda: clear())
button_clear.grid(row=4, column=0)

button_0 = tkinter.Button(root, background="#9E9FA5", text="0",width=4, command=lambda: add("0"))
button_0.grid(row=4, column=1)

button_dot = tkinter.Button(root, background="#9E9FA5", text=". ", width=4, command=lambda: add("."))
button_dot.grid(row=4, column=2)

button_add = tkinter.Button(root, background="#9E9FA5", text="+", width=4, command=lambda: add("+"))
button_add.grid(row=4, column=3)

#buttons of row 5
button_equals = tkinter.Button(root, background="#9E9FA5", width=20, text="=", command=lambda: calculate())
button_equals.grid(row=5, column=0, columnspan=4)

root.mainloop()

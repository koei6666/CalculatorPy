from tkinter import *
from tkinter import ttk
from module import calculate,length_restrict

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("CalculatorPy")

        self.mainframe = ttk.Frame(root, padding = "3 12 3 3")
        self.mainframe.grid(column=0,row=0, sticky=(N,W,E,S))

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        self.value = []
        self.operator = None
        self.status = "i"




        #show an input filed and take input as a variable to show as label in next code block
        self.result_field = StringVar(value="0")


        #button cluster 0-9
        ttk.Button(self.mainframe, text="1", command=lambda:self.button("1")).grid(column=0, row=1)
        ttk.Button(self.mainframe, text="2", command=lambda:self.button("2")).grid(column=1, row=1)
        ttk.Button(self.mainframe, text="3", command=lambda:self.button("3")).grid(column=2, row=1)
        ttk.Button(self.mainframe, text="4", command=lambda:self.button("4")).grid(column=0, row=2)
        ttk.Button(self.mainframe, text="5", command=lambda:self.button("5")).grid(column=1, row=2)
        ttk.Button(self.mainframe, text="6", command=lambda:self.button("6")).grid(column=2, row=2)
        ttk.Button(self.mainframe, text="7", command=lambda:self.button("7")).grid(column=0, row=3)
        ttk.Button(self.mainframe, text="8", command=lambda:self.button("8")).grid(column=1, row=3)
        ttk.Button(self.mainframe, text="9", command=lambda:self.button("9")).grid(column=2, row=3)
        ttk.Button(self.mainframe, text="0", command=lambda:self.button("0")).grid(column=0, row=4)
        ttk.Button(self.mainframe, text=".", command=lambda:self.button(".")).grid(column=1, row=4)


        ttk.Button(self.mainframe, text="CA", command=self.clear_all).grid(column=5, row=0, sticky=(E))

        ttk.Button(self.mainframe, text="+", command=lambda:self.opera("+")).grid(column=4, row=0, sticky=(E))
        ttk.Button(self.mainframe, text="-", command=lambda:self.opera("-")).grid(column=4, row=1, sticky=(E))
        ttk.Button(self.mainframe, text="*", command=lambda:self.opera("*")).grid(column=4, row=2, sticky=(E))
        ttk.Button(self.mainframe, text="/", command=lambda:self.opera("/")).grid(column=4, row=3, sticky=(E))
        ttk.Button(self.mainframe, text="=", command=lambda:self.opera("=")).grid(column=4, row=4, sticky=(E))



        self.result_window = ttk.Label(self.mainframe, textvariable=self.result_field, width=20)
        self.result_window.grid(column=1, row=0, sticky=(N,W,E,S))


    def button(self,val):
        if self.status == "w":
            self.result_field.set("")
            self.status = "i"
        current = str(self.result_field.get())
        if len(current) < 12:
            if current == "0":
                value = val
            else:
                value = current + val
            self.result_field.set(value)


    def opera(self, operator):
        if self.status == "i":
            self.value.append(float(self.result_field.get()))
            self.status = "w"
        if len(self.value) == 2 and self.operator:
            self.value[0] = calculate(self.value[0], self.value.pop(), self.operator)
            self.result_field.set(length_restrict(self.value[0]))
            self.operator = None
        if operator != "=":
            self.operator = operator


    def clear_all(self):
        self.value = []
        self.operator = None
        self.result_field.set("0")





def create_root():
    root = Tk()
    return root

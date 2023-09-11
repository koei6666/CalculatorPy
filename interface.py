from tkinter import *
from tkinter import ttk
from module import calculate,length_restrict

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("CalculatorPy")


        #operator display dictionary
        self.operators = {
        "+":"+",
        "-":"-",
        "*":"×",
        "/":"÷",
        "%":"%",
        "**":"^",
        "//":"//"
        }


        #mainframe
        self.mainframe = ttk.Frame(root, padding = "3 12 3 3")
        self.mainframe.grid(column=0,row=0, sticky=(N,W,E,S))


        #column and row configuration
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)

        #attributes
        self.value = []
        self.operator = None
        self.status = "i"
        self.mode = "i"

        #style
        st = ttk.Style()
        st.theme_use('alt')
        st.configure("operator.TButton", font=("Helvetica",10))
        st.configure("operator_.TButton", font=("Helvetica",14))
        st.configure("specialbt.TButton", font=("Helvetica",9), background="darkorange", width=8, foreground="black", borderwidth=5, focusthickness=1, focuscolor='red')
        st.map("specialbt.TButton", background=[("pressed","red")])
        st.configure("specialbt1.TButton", font=("Helvetica",9), background="firebrick1", width=8, foreground="black", borderwidth=5, focusthickness=1, focuscolor='white')
        st.map("specialbt1.TButton", background=[("pressed","darkorange")])
        st.configure("hexbt.TButton", font=("Courier",10), background="grey", foreground="black", width=4)
        #style-button ipad
        ipadY = 5
        ipadY_op = 1

        #string var to display in the result window
        self.result_field = StringVar(value="0")
        self.operator_display = StringVar(value=" ")
        self.display_window = StringVar()
        self.window_update()
        self.result_field.trace_add("write", self.window_update)
        self.operator_display.trace_add("write", self.window_update)


        #button cluster 0-9
        self.one = ttk.Button(self.mainframe, text="1", command=lambda:self.button("1"), style="operator.TButton")
        self.two = ttk.Button(self.mainframe, text="2", command=lambda:self.button("2"), style="operator.TButton")
        self.three = ttk.Button(self.mainframe, text="3", command=lambda:self.button("3"), style="operator.TButton")
        self.four = ttk.Button(self.mainframe, text="4", command=lambda:self.button("4"), style="operator.TButton")
        self.five = ttk.Button(self.mainframe, text="5", command=lambda:self.button("5"), style="operator.TButton")
        self.six = ttk.Button(self.mainframe, text="6", command=lambda:self.button("6"), style="operator.TButton")
        self.seven = ttk.Button(self.mainframe, text="7", command=lambda:self.button("7"), style="operator.TButton")
        self.eight = ttk.Button(self.mainframe, text="8", command=lambda:self.button("8"), style="operator.TButton")
        self.nine = ttk.Button(self.mainframe, text="9", command=lambda:self.button("9"), style="operator.TButton")
        self.zero = ttk.Button(self.mainframe, text="0", command=lambda:self.button("0"), style="operator.TButton")
        self.dot = ttk.Button(self.mainframe, text=".", command=lambda:self.button("."), style="operator.TButton")

        self.numbers = {1:self.one, 2:self.two, 3:self.three, 4:self.four, 5:self.five, 6:self.six, 7:self.seven, 8:self.eight, 9:self.nine, 0:self.zero, ".":self.dot}

        #grid
        self.numbers[1].grid(column=0, row=1, ipady=ipadY)
        self.numbers[2].grid(column=1, row=1, ipady=ipadY)
        self.numbers[3].grid(column=2, row=1, ipady=ipadY)
        self.numbers[4].grid(column=0, row=2, ipady=ipadY)
        self.numbers[5].grid(column=1, row=2, ipady=ipadY)
        self.numbers[6].grid(column=2, row=2, ipady=ipadY)
        self.numbers[7].grid(column=0, row=3, ipady=ipadY)
        self.numbers[8].grid(column=1, row=3, ipady=ipadY)
        self.numbers[9].grid(column=2, row=3, ipady=ipadY)
        self.numbers[0].grid(column=0, row=4, ipady=ipadY)
        self.numbers["."].grid(column=1, row=4, ipady=ipadY)


        ttk.Button(self.mainframe, text="CA", command=lambda:self.clear_all("0"), style="operator.TButton").grid(column=2, row=4, ipady=ipadY)

        ttk.Button(self.mainframe, text="+", command=lambda:self.opera("+"), style="operator_.TButton").grid(column=4, row=0, sticky=(E), ipady=ipadY_op)
        ttk.Button(self.mainframe, text="-", command=lambda:self.opera("-"), style="operator_.TButton").grid(column=4, row=1, sticky=(E), ipady=ipadY_op)
        ttk.Button(self.mainframe, text="×", command=lambda:self.opera("*"), style="operator_.TButton").grid(column=4, row=2, sticky=(E), ipady=ipadY_op)
        ttk.Button(self.mainframe, text="÷", command=lambda:self.opera("/"), style="operator_.TButton").grid(column=4, row=3, sticky=(E), ipady=ipadY_op)
        ttk.Button(self.mainframe, text="=", command=lambda:self.opera("="), style="operator_.TButton").grid(column=4, row=4, sticky=(E), ipady=ipadY_op)

        self.result_window = ttk.Label(self.mainframe, textvariable=self.display_window, width=40, background="black", foreground= "white", relief="sunken", font=("Courier",12))
        self.result_window.grid(columnspan=3, row=0, ipady=7)

        #button for expand
        self.expandcollapse = StringVar(value="Expand")
        ttk.Button(self.mainframe, textvariable=self.expandcollapse, command=self.expand).grid(column=5, row=1)

        #advanced calculation
        self.modb = ttk.Button(self.mainframe, text="MOD", command=lambda:self.opera("%"), style="specialbt.TButton")
        self.powb = ttk.Button(self.mainframe, text="POW", command=lambda:self.opera("**"), style="specialbt.TButton")
        self.fdivb = ttk.Button(self.mainframe, text="FDIV", command=lambda:self.opera("//"), style="specialbt.TButton")

        #converter
        self.bin = ttk.Button(self.mainframe, text="BIN", command=lambda:self.converter("b"), style="specialbt1.TButton")
        self.hex = ttk.Button(self.mainframe, text="HEX", command=lambda:self.converter("x"), style="specialbt1.TButton")
        self.int = ttk.Button(self.mainframe, text="INT", command=lambda:self.converter("i"), style="specialbt1.TButton")

        #binary input mode
        self.binary = ttk.Button(self.mainframe, text="BIN-M", command=lambda:self.converter("i"), style="specialbt1.TButton")
        self.hex_warning = ttk.Label(self.mainframe, text="Input hexdecimal from your keyboard.")

        #bit-wise operation
        self.andop = ttk.Button(self.mainframe, text="&", command=lambda:self.converter("b"), style="specialbt1.TButton")
 
    def window_update(self, *args):
        self.display_window.set(self.operator_display.get().ljust(2) + self.result_field.get().rjust(38))


    def button(self,val):
        #print(f"bt\nin\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")
        self.error_cl()
        if self.status == "f":
            self.clear_all("")
        elif self.status == "w":
            self.result_field.set("")
        self.status = "i"
        current = str(self.result_field.get())
        if len(current) < 12:
            if current == "0" and val != ".":
                value = val
            else:
                value = current + val
            self.result_field.set(value)
        #print(f"bt\nout\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")


    def opera(self, operator):
        #print(f"in\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")
        self.converter("i")
        self.error_cl()
        if self.status == "i":
            self.value.append(float(self.result_field.get()))
        self.status = "w"
        if len(self.value) == 2 and self.operator:
            result = calculate(self.value[0], self.value.pop(), self.operator)
            if result == "ee":
                self.result_field.set("ER")
                self.value = []
                return
            self.value[0] = result
            self.result_field.set(length_restrict(self.value[0]))
            self.operator = None
        if operator == "=":
            self.status = "f"
            self.operator_display.set(" ")
            return
        self.operator = operator
        self.operator_display.set(self.operators[operator])

        #print(f"out\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")


    def converter(self,format_):
        conve_table = {"b":2,"x":16}
        
        if self.mode == format_:
            return
        value = self.result_field.get()
        if value:
            if self.mode in "bx" and format_ == "i":
                self.result_field.set(int(value,conve_table[self.mode]))
            elif self.mode == "b" and format_ == "x":
                self.result_field.set(format(int(value,2), format_))
            elif self.mode == "x" and format_ == "b":
                self.result_field.set(format(int(value,16), format_))
            else:
                self.result_field.set(format(int(value), format_))
        self.bi_inputmode(format_)
        self.operator_display.set(format_)


    def bi_inputmode(self,mode):
        self.mode = mode
        self.numbers[0].state(["!disabled"])
        self.numbers[1].state(["!disabled"])
        if mode == "b":
            set_to = "disabled"
            st, ed = 2, 10
            self.hex_warning.grid_remove()
        elif mode == "i":
            set_to = "!disabled"
            st, ed = 0, 10
            self.hex_warning.grid_remove()
        else:
            set_to = "disabled"
            st, ed = 0, 10
            self.hex_warning.grid(columnspan=7, row=4)
        for i in range(st,ed):
            self.numbers[i].state([set_to])
        self.numbers["."].state([set_to])



    def clear_all(self,setvalue):
        self.error_cl()
        self.value = []
        self.operator = None
        self.result_field.set(setvalue)
        self.operator_display.set(" ")

    def error_cl(self):
        if self.result_field.get() == "ER":
            self.result_field.set("0")


        #expand buttons cluster

    def expand(self):

        if self.expandcollapse.get() == "Expand":
            self.modb.grid(column=6, row=0)
            self.powb.grid(column=6, row=1)
            self.fdivb.grid(column=6, row=2)
            self.bin.grid(column=7, row=0)
            self.hex.grid(column=7, row=1)
            self.int.grid(column=7, row=2)
            self.binary.grid(column=7, row=3)
            self.expandcollapse.set("Collapse")
        else:
            self.modb.grid_remove()
            self.powb.grid_remove()
            self.fdivb.grid_remove()
            self.bin.grid_remove()
            self.hex.grid_remove()
            self.int.grid_remove()
            self.binary.grid_remove()
            self.expandcollapse.set("Expand")




def create_root():
    root = Tk()
    return root

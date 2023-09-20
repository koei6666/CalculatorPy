from tkinter import *
from tkinter import ttk
from module import calculate,length_restrict,bitwiseop
from collections import deque

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title("CalculatorPy")
        self.root.resizable(False,False)

        #bind
        self.keybind = {
        "num":self.button,
        "c":[self.clear_all,"0"],
        "C":[self.clear_all,"0"],
        "plus":[self.opera,"+"],
        "minus":[self.opera,"-"],
        "asterisk":[self.opera,"*"],
        "slash":[self.opera,"/"],
        "Return":[self.opera,"="],
        ".":[self.button,"."],
        "m":[self.opera,"%"],
        "M":[self.opera,"%"],
        "p":[self.opera,"**"],
        "P":[self.opera,"**"],
        "f":[self.opera,"//"],
        "F":[self.opera,"//"],
        "b":[self.converter,"b"],
        "B":[self.converter,"b"],
        "x":[self.converter,"x"],
        "X":[self.converter,"x"],
        "i":[self.converter,"i"],
        "I":[self.converter,"I"]
        }


        self.key_bind()

        #dictionary
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
        self.history = deque()
        self.hiwindow_ = None
        self.scr_width = self.root.winfo_screenwidth()
        self.scr_height = self.root.winfo_screenheight()


        #screen cordinate
        self.root.geometry(f"+{int(0.15*self.scr_width)}+{int(0.2*self.scr_height)}")


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
        st.configure("history.TButton", relief="flat", font=("Courier",10), width=55, foreground="black")
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
        ttk.Button(self.mainframe, text="←", command=lambda:self.backspace(), style="operator_.TButton").grid(column=5, row=4, sticky=(E), ipady=ipadY_op)
        ttk.Button(self.mainframe, text="History", command=self.hiwindow).grid(column=5, row=0, ipady=ipadY_op)

        self.result_window = ttk.Label(self.mainframe, textvariable=self.display_window, width=27, background="black", foreground= "white", relief="sunken", font=("Courier",12))
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
        self.int = ttk.Button(self.mainframe, text="DEC", command=lambda:self.converter("i"), style="specialbt1.TButton")

        #binary input mode
        self.hex_warning = ttk.Label(self.mainframe, text="Hexdecimal is for convertion only.")

        #bit-wise operation
        self.andop = ttk.Button(self.mainframe, text="&", command=lambda:self.bitop("&"), style="specialbt1.TButton")
        self.invertop = ttk.Button(self.mainframe, text="~", command=lambda:self.bitop("~"), style="specialbt1.TButton")



    def key_bind(self,st=None,ed=None,unbind=None):
        keys = self.keybind.keys()
        self.root.bind("<Key-BackSpace>", lambda event:self.backspace())
        for index, key in enumerate(keys):
            if index == 0:
                continue
            self.root.bind(f"<Key-{key}>", lambda event, k=key: self.keybind[k][0](self.keybind[k][1]))
        if not unbind:
            for number in range(0,10):
                self.root.bind(f"<Key-{number}>", lambda event, n=number: self.keybind["num"](str(n)))
        else:
            for number in range(st,ed):
                self.root.unbind(f"<Key-{number}>")
            self.root.unbind("<Key-.")


    def window_update(self, *args):
        self.display_window.set(self.operator_display.get().ljust(2) + self.result_field.get().rjust(25))


    def keyboard(self,event):
        key = event.keysym
        self.display_window.set(key)

    def backspace(self):
        current = self.result_field.get()
        if current != "0" and len(current) > 1:
            current = current[:-1]
        else:
            current = "0"
        if len(self.value) == 1:
            self.value[0] = float(current)
        self.result_field.set(current)
        #print(f"\nvalue={self.value}\n")


    def button(self,val):
        #print(f"bt\nin\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")
        self.error_cl()
        if self.status == "f":
            self.clear_all("")
        elif self.status == "w":
            self.result_field.set("")

        current = str(self.result_field.get())

        if len(current) < 12:
            if current == "0" and val != ".":
                value = val
            else:
                if val == ".":
                    if "." in current:
                        self.status = "i"
                        return
                    elif self.status in "wf":
                        current = "0"
                value = current + val
            self.result_field.set(value)
            self.status = "i"
        #print(f"bt\nout\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")


    def opera(self, operator):
        #print(f"in\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")
        self.converter("i")
        self.error_cl()
        if self.status == "i":
            self.value.append(float(self.result_field.get()))
        self.status = "w"
        if len(self.value) == 2 and self.operator:
            output = calculate(self.value[0], self.value.pop(), self.operator)
            self.history.appendleft(output)
            result = output[0]
            if result == "ee":
                self.result_field.set("ER")
                self.value = []
                return
            self.value[0] = result
            self.result_field.set(length_restrict(self.value[0]))
            self.history_refresh()
            self.operator = None
        if operator == "=":
            self.status = "f"
            self.operator_display.set(" ")
            return
        self.operator = operator
        self.operator_display.set(self.operators[operator])

        #print(f"out\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}")



    def converter(self,format_):
        self.error_cl()
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
                try:
                    self.result_field.set(format(int(value), format_))
                except:
                    self.result_field.set("ER")
        self.bi_inputmode(format_)
        self.operator_display.set(format_)


    def bi_inputmode(self,mode):
        self.mode = mode
        self.numbers[0].state(["!disabled"])
        self.numbers[1].state(["!disabled"])
        self.key_bind()
        if mode == "b":
            set_to = ("disabled",1)
            st, ed = 2, 10
            self.hex_warning.grid_remove()
            #self.invertop.grid(column=8, row=0)
            #self.andop.grid(column=8, row=1)
        elif mode == "i":
            set_to = ("!disabled",0)
            st, ed = 0, 10
            self.hex_warning.grid_remove()
            #self.invertop.grid_remove()
            #self.andop.grid_remove()
        else:
            set_to = ("disabled",1)
            st, ed = 0, 10
            self.hex_warning.grid(columnspan=7, row=4)
            #self.invertop.grid_remove()
            #self.andop.grid_remove()
        for i in range(st,ed):
            self.numbers[i].state([set_to[0]])
            self.key_bind(st,ed,set_to[1])
        self.numbers["."].state([set_to[0]])

    def bitop(self,op):
        print(f"bt\nin\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")
        self.status = "w"
        if self.mode != "b":
            self.converter("b")
        current = self.result_field.get()
        if op == "~":
            inverted = [bitwiseop("~",current)]
            self.result_field.set(inverted[0])
            self.value = inverted
            return
        else:
            self.value.append(current)
            if len(self.value) == 3:
                self.value = [bitwiseop(self.value[1],self.value[0],self.value[2])]
                self.result_field.set(self.value[0])
                print(f"bt\nout\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")
            if op != "=":
                self.value.append(op)
                print(f"bt\nout\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")
                return
            self.value = []
            print(f"bt\nout\nvalue={self.value}\noperator={self.operator}\nstatus={self.status}\n")
            return



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

            self.expandcollapse.set("Collapse")
        else:
            self.modb.grid_remove()
            self.powb.grid_remove()
            self.fdivb.grid_remove()
            self.bin.grid_remove()
            self.hex.grid_remove()
            self.int.grid_remove()
            self.expandcollapse.set("Expand")

    def avaliablity_check(func):
        def inner(self):
            if self.hiwindow_ is not None and self.hiwindow_.winfo_exists():
                return func(self)
        return inner

    @avaliablity_check
    def history_refresh(self):
        for i in range(len(self.history)):
            ttk.Button(self.hiwindow_, style="history.TButton", text=self.history[i][1], command=lambda x=i:self.retrive(x)).grid(column=0, row=i+1)

    def retrive(self,number):
        result = self.history[number][0]
        self.clear_all("")
        self.value = [result]
        self.result_field.set(str(result))


    def hiwindow(self):
        self.hiwindow_ = Toplevel(self.root)
        self.hiwindow_.title = "History"
        self.hiwindow_.geometry(f"+{int(0.5*self.scr_width)}+{int(0.2*self.scr_height)}")
        st_h = ttk.Style()
        st_h.theme_use('alt')
        headline = "History".rjust(38," ")
        ttk.Label(self.hiwindow_, text=headline, width=45, font=("Courier",12)).grid(column=0, row=0)
        self.history_refresh()





def create_root():
    root = Tk()
    return root

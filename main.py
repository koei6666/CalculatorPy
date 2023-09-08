from module import calculate
from interface import Calculator,create_root

if __name__ == "__main__":

    root = create_root()
    Calculator(root)
    root.mainloop()

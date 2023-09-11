import operator as ope


def calculate(a, b, operator):
    funcdict = {
        "+":ope.add,"-":ope.sub,"*":ope.mul,"/":ope.truediv,"//":ope.floordiv,"**":ope.pow,"%":ope.mod
    }
    func = funcdict[operator]
    try:
        result = conditional_round(func(a,b))
    except:
        result = "ee"

    return result

def conditional_round(value):
    if int(value) == value:
        return int(value)
    else:
        return round(value,2)

def length_restrict(value):
    value = str(value)
    if len(value) > 11:
        return f"{float(value):.9e}"
    return value

def bitwiseop(op,a,b=None):
    out = ""
    if op == "~":
        for i in a:
            if i == "1":
                out += "0"
            else:
                out += "1"
        return out
    if b:
        range = min(len(a), len(b))
        if op == "&":
            pass
            

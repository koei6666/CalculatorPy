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

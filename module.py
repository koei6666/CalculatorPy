import operator as ope
#import traceback


def calculate(a, b, operator):
    funcdict = {
        "+":ope.add,"-":ope.sub,"*":ope.mul,"/":ope.truediv,"//":ope.floordiv,"**":ope.pow,"%":ope.mod
    }
    func = funcdict[operator]
    str_a = str(length_restrict(conditional_round(a)))
    str_b = str(length_restrict(conditional_round(b)))
    try:
        result = conditional_round(func(a,b))
        history_text = str_a + operator + str_b + "=" + str(length_restrict(result))
    except:
        result = "ee"
        #traceback.print_exc()
    return (result, history_text)

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
        if len(a) > len(b):
            b = b.zfill(len(a))
        else:
            a = a.zfill(len(b))
        if op == "&":
            y = len(a) - 1
            while y >= 0:
                if a[y] == "1" and b[y] == "1":
                    out = "1" + out
                else:
                    out = "0" + out
                y -= 1
            return out

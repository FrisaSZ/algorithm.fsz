def eval(exp):
    vals = []
    ops = []
    for c in exp:
        if c in '0123456789':
            vals.append(c)
        elif c in '+-*/':
            ops.append(c)
        elif c == '(':
            pass
        elif c == ')':
            op = ops.pop()
            val = vals.pop()
            rst = 0
            if op == '+':
                rst = float(vals.pop()) + float(val)
            elif op == '-':
                rst = float(vals.pop()) - float(val)
            elif op == '*':
                rst = float(vals.pop()) * float(val)
            elif op == '/':
                rst = float(vals.pop()) / float(val)
            else:
                pass
            vals.append(str(rst))
        else:
            pass
    return float(vals[-1])


print(eval('(1 + ((2 + 3) * (4 * 5)))'))

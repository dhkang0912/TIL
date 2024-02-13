s = '2+3*4/5'
prio = {'+':1, '*':2, '-':1, '/':2}

ST = []
result = []
for c in s:
    if c.isdigit():
        result.append(c)
    else:
        if ST and prio[ST[-1]] < prio[c] :
            ST.append(c)
        else:
            while ST and prio[ST[-1]] >= prio[c] :
                result.append(ST.pop())
            ST.append(c)

while ST:
    result.append(ST.pop())
print(result)
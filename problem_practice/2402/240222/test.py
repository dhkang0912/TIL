# 이진수 문자열을 십진수로 만들어 return
def binTodec(s):
    result = 0
    for c in s:
        result = result * 2 + int(c)
        # 십진수 경우로 예시를 들어서 이해할 수 있음
    return result


# 이진수를 십진수로 만들어 return
def binTobin(intV):
    s = ''
    while intV > 0:
        s += str(intV % 2)
        intV //= 2
    return s


# 16진수를 십진수로 만들어 return
def hexTodec(s):
    result = 0
    for c in s:
        if c.isdigit():
            result = result * 16 + int(c)
        else:
            result = result * 16 + ord(c) - ord('A') + 10
    return result


# 십진수를 16진수로 만들어 return
def decTohex(inv):
    s = ''
    while intV > 0:
        r = intv % 16
        if r < 10:
            s = str(inv % 16) + s
        else:
            s = chr((r - 10) + ord('A'))
        intV //= 16
    return s


def hexTobin(s):
    value = hexTodec(s)
    bins = decTohex(value)
    return bins


s = '11001'

print(binTodec(s))
print(binTobin(25))

print(hexTodec(s))
print(hexTodec('A0'))
print(decTohex(160))

hexs = 'AA0'
print(hexTobin(hexs))
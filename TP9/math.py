from arithmetiqueDansZ import *
def logarithmeDiscret(a: ElementDeZnZ, b: ElementDeZnZ):
    assert a.n == b.n
    m = sqrt(a.rep)
    if m < 0:
        return a.inverse()
    offset = 2
    i = round(m - offset)
    dictionnary = dict()
    aInv = a.inverse()
    found = dict.fromkeys(["i", "j"], 0)
    for j in range(1, i):
        calc = b * aInv**i
        dictionnary[calc.a] = j
    for ii in range(1, i):
        ai = (b * (a.inverse())**ii).n
        if ai in dictionnary.keys():
            found["i"] = ii
            found["j"] = dictionnary[ai]
    return m * (found["i"] + found["j"]) # x = m * i + j for -> a^x = b [p]

if __name__ == "__main__":
    a = ElementDeZnZ(456, 4567)
    b = ElementDeZnZ(23, 4567)
    print(a, b)
    log = logarithmeDiscret(a, b)
    print(log)
    print(a**log, b)

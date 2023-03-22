from arithmetiqueDansZ import *

def logarithmeDiscret(a: ElementDeZnZ, b: ElementDeZnZ):
    assert a.n == b.n
    m = int(sqrt(a.rep)) + 1
    if m < 0:
        return a.inverse()
    dictionnary = dict()
    aInv = a.inverse()
    i_, j_ = 0, 0
    for i in range(1, m):
        calc = b * (aInv**(-m))**i
        dictionnary[calc.a] = i
    for j in range(1, m):
        aj = (a**j).a
        if aj in dictionnary.keys():
            i_ = dictionnary[aj]
            j_ = j
            dictionnary[j] = aj
            break
    if all(x == 0 for x in [i_, j_]):
        return False
    return m * i + j, dictionnary

if __name__ == "__main__":
    a = ElementDeZnZ(2, 97)
    b = ElementDeZnZ(24, 97)
    print(a, b)
    log = logarithmeDiscret(a, b)
    print(log)
    print(a**log, b)

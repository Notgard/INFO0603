import pickle
from sympy import primerange, isprime
from arithmetiqueDansZEtd import estPremier, primeNumbers
from typing import List


def estPremierOuPseudoPremierDansLaBase(n, a):
    """Indique si un nombre n est un pseudo premier ou non, pour une base a donnée
    >>> estPremierOuPseudoPremierDansLaBase(121, 3)
    True
    >>> estPremierOuPseudoPremierDansLaBase(121, 2)
    False
    """
    s, t = 0, n-1

    while t % 2 == 0:
        s += 1
        t >>= 1

    x = pow(a, t, n)

    if (x == 1 or x == n - 1):
        return True

    for _ in range(s):
        x = pow(x, 2, n)
        if x == 1 or x == n-1:
            return True

    return False


def estPremierOuPseudoPremierDansLesBase(n, la):
    """Indique sir un nombre n est pseudo premier dans les bases présentes dans la
    >>> estPremierOuPseudoPremierDansLesBase(121, [2, 3])
    False
    >>> allPrimes = list(primerange(0, 7919-1)); estPremierOuPseudoPremierDansLesBase(7919, allPrimes)
    True
    """
    res = []
    pseudoPrimes = []
    for a in la:
        if a != n:
            res.append((n, a, estPremierOuPseudoPremierDansLaBase(n, a)))
            pseudoPrimes.append(estPremierOuPseudoPremierDansLaBase(n, a))
    #print(res)
    return all(pseudoPrimes)

def estPremierMR(n):
    """Renvoie si un nombre est premier ou non en utilisant l'algorithme Miller-Rabin
    >>> estPremierMR(7874)
    False
    >>> estPremierMR(7873)
    True
    """
    #if not estPremierOuPseudoPremierDansLesBase(n, list(primerange(0, n-1))):
    if n == 2:
        return True
    if not estPremierOuPseudoPremierDansLaBase(n, 2):
        return False
    elif n in readPrimesFromFile():
        return True
    else:
        return isprime(n)


def nombresPremiers(nmax):
    primeNumbers = []
    for n in range(2, 2**nmax):
        if estPremierMR(n):
            primeNumbers.append(n)
    return primeNumbers


def writePrimesToFile(nmax):
    nPremiers = nombresPremiers(nmax)
    pickle.dump(nPremiers, open('ListeDePremiers.p', 'wb'))


def readPrimesFromFile() -> List:
    return pickle.load(open('ListeDePremiers.p', 'rb'))

def demo():
    n = 100
    allPrimes = list(primerange(0, n))
    falsePositives = set()
    for n in range(2, 2**16):
        lPrimes = [2]
        index = 0
        if estPremierOuPseudoPremierDansLaBase(n, 2) and not estPremier(n):
            index += 1
            lPrimes.append(allPrimes[index])
            falsePositives.add(n)

    n = 2
    bases = [2, 3]
    while not (estPremierOuPseudoPremierDansLesBase(n, bases) and not estPremier(n)):
        n+=1
    print(f"Premier Faux positif dans les bases {bases} >>", n)
    #Suite A001567 de l'OEIS jusque 2^16
    print("False Positives in base 2 : ", sorted(falsePositives))

    n = 2
    bases = list(primerange(1, 15))
    while not (estPremierOuPseudoPremierDansLesBase(n, bases) and not estPremier(n)):
        n+=1
    print(f"Premier faux positif dans les bases {bases} >>", n)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    demo()

    #writePrimesToFile(22)
    #print(readPrimesFromFile())
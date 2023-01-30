import copy
from random import randint, choice
from math import sqrt, log
from sympy import isprime
from arithmetiqueDansZ import ElementDeZnZ, estPremier
from hashlib import sha256
from CodeurHachage import *

# Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/
# Voir Au coeur du Bitcoin - Programmer la Blockchain ouverte - collection O'Reilly
# Voir https://www.johndcook.com/blog/2018/08/14/bitcoin-elliptic-curves/
class ElemtE07(object):
    "Ensemble des solutions de Y²=X^3+7 dans Fp Courbe secp256k1"

    def __init__(self, x, y=None, p=None):
        """
        Défini par deux ElmntZnZ mais seul le modulo de x est utilisé . Celui de y doit donc lui être égal.
        Avec l'élément neutre ayant self.y='Inf'
        ElemtE07(7,6,11) doit renvoyer une erreur
        >>> ElemtE07(ElementDeZnZ(7,11),ElementDeZnZ(8,11))
        ElemtE07(7,8,11)
        >>>
        >>> ElemtE07(1,"Inf",11)
        ElemtE07(1,"INF",11)
        """
        if isinstance(x, int) and isinstance(y, int):
            assert p != None and estPremier(p), "Le modulo est manquant"
            self.x = ElementDeZnZ(x, p)
            self.y = ElementDeZnZ(y, p)
            self.p = p
        elif isinstance(x, ElementDeZnZ) and isinstance(y, ElementDeZnZ):
            assert x.n == y.n
            self.x = x
            self.y = y
            self.p = x.n
        elif isinstance(x, str) and isinstance(y, int):
            assert p != None and estPremier(p), "Le modulo est manquant"
            if x.upper() == 'INF':
                self.x = x.upper()
            self.y = ElementDeZnZ(y, p)
            self.p = p
        elif isinstance(x, int) and isinstance(y, str):
            assert p != None and estPremier(p), "Le modulo est manquant"
            self.x = ElementDeZnZ(x, p)
            if y.upper() == 'INF':
                self.y = y.upper()
            self.p = p
        elif isinstance(x, str) and isinstance(y, ElementDeZnZ):
            if x.upper() == 'INF':
                self.x = x.upper()
            self.y = y
            self.p = y.n
        elif isinstance(x, ElementDeZnZ) and isinstance(y, str):
            self.x = x
            if y.upper() == 'INF':
                self.y = y.upper()
            self.p = x.n
        elif isinstance(x, ElemtE07):
            self.x = x.x
            self.y = x.y
            self.p = x.p

        if isinstance(self.y, int):
            assert self.y**2 == self.x**3 + 7

    @staticmethod
    def lDesElements(p=47):
        """
        >>> ElemtE07.lDesElements(5)
        [ElemtE07(0,"INF",5), ElemtE07(2,0,5), ElemtE07(3,2,5), ElemtE07(3,3,5), ElemtE07(4,1,5), ElemtE07(4,4,5)]
        >>> len(ElemtE07.lDesElements(11))
        12
        >>> ElemtE07(6,5,11) in (ElemtE07.lDesElements(11))
        True
        """
        lElements = [ElemtE07(0, 'Inf', p)]
        for x in range(0, p):
            for y in range(0, p):
                if ElementDeZnZ(y**2, p) == ElementDeZnZ((x**3) + 7, p):
                    lElements.append(ElemtE07(x, y, p))
        return lElements

    def __hash__(self):
        """On fera une fonction injective afin de l'utiliser également dans binCode"""
        #return sha256(self.__repr__())
        return CodeurHachage().binCode(Binaire603(self.__repr__))
    
    @staticmethod    
    def ElemtE07DepuisHash(h, p):
        """
        >>> h=ElemtE07(6,5,11).__hash__()
        >>> ElemtE07.ElemtE07DepuisHash(h,11)
        ElemtE07(6,5,11)
        """
        raise NotImplementedError
    
    @staticmethod    
    def eDesElements(p=47, verbose=False):
        """
        >>> ElemtE07.eDesElements(5)==set(ElemtE07.lDesElements(5))
        True
        >>> ElemtE07(8,3,17) in (ElemtE07.eDesElements(17))
        True
        """
        return set(ElemtE07.lDesElements(p))

    def __str__(self):
        """
        >>> print(ElemtE07(ElementDeZnZ(3,47),ElementDeZnZ(9,47)))
        (3,9)[47]
        """
        if self == 0:
            return "O(à l'infini)"
        else:
            return f"({self.x.rep},{self.y.rep})[{self.x.n}]"

    def __repr__(self):
        """
        """
        if isinstance(self.y, ElementDeZnZ):
            valy = self.y.rep
        elif isinstance(self.y, str):
            valy = f'"{self.y}"'
        else:
            valy = self.y
        return f"ElemtE07({self.x.rep},{valy},{self.x.n})"

    def __add__(self, other):
        """
        >>> ElemtE07(2,2,11)+ElemtE07(3,1,11)
        ElemtE07(7,3,11)
        >>> (ElemtE07(3,"INF",47)+ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(3,9,47)
        >>> ElemtE07(2,2,11)+ElemtE07(2,9,11)
        ElemtE07(5,0,11)
        """
        assert self.p == other.p
        
        if self.estNeutre():
            return other
        elif other.estNeutre():
            return self
        elif self.x == other.x:
            return self.double()
        else:
            lambdA = (self.y - other.y) * (self.x - other.x).inverse()
            x = (lambdA**2) - self.x - other.x
            y = (self.y + lambdA * (x - self.x)) * lambdA
            return ElemtE07(x, y, self.p)

    def estNeutre(self):
        return isinstance(self.y, str)

    def double(self):
        """
        >>> ElemtE07(2,2,11).double()
        ElemtE07(5,0,11)
        """
        lambdA = (3*(self.x**2)) * (2*self.y).inverse()
        x = (lambdA**2) - 2 * self.x
        y = (self.y + lambdA * (x - self.x)) * lambdA
        return ElemtE07(x, y)

    def lOrbite(self):
        """
        >>> ElemtE07(2,2,11).lOrbite()
        [ElemtE07(2,2,11), ElemtE07(5,0,11), ElemtE07(2,9,11), ElemtE07(0,"INF",11)]
        """
        lOrbites = [self]


    def __mul__(self, other):
        """
        >>> ElemtE07(6,5,11)*3
        ElemtE07(5,0,11)
        >>> ElemtE07(15,13,17)*0
        ElemtE07(0,"INF",17)
        """
        start = ElemtE07(0, "Inf", self.p)
        if isinstance(other, int):
            if other != 0:
                start = other.double()
                for _ in range(0, other//2):
                    start += start.double()
            elif other == 1:
                return self
        return start

    def __rmul__(self, other):
        """
        >>> 2*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        >>> 2*(ElemtE07(3,"INF",47)+3*ElemtE07(3,9,47))+ElemtE07(3,"INF",47)
        ElemtE07(43,32,47)
        """
        raise NotImplementedError

    def __eq__(self, other):
        """
        >>> 3*ElemtE07(6,5,11)==ElemtE07(5,0,11)
        True
        >>> ElemtE07(0,"Inf",47)==0
        True
        >>> ElemtE07(3,9,47)==ElemtE07(3,"Inf",47) or ElemtE07(3,"Inf",47)==ElemtE07(3,9,47)
        False
        """
        if isinstance(other, int):
            if self.estNeutre():
                return self.x == other
            else:
                return self.x == self.y == other
        elif isinstance(other, ElemtE07):
            if self.estNeutre() and not other.estNeutre():
                return False
            elif other.estNeutre() and not self.estNeutre():
                return False
            else:
                return self.x == other.x and self.y == other.y

    def __neg__(self):
        """
        >>> -ElemtE07(7,3,11)
        ElemtE07(7,8,11)
        """
        return ElemtE07(self.x, -self.y, self.p)

    def __sub__(self, other):
        """
        >>> ElemtE07(3,10,11)-ElemtE07(7,3,11)
        ElemtE07(4,7,11)
        >>> ElemtE07(3,9,47)-ElemtE07(3,9,47)==0
        True
        """
        return ElemtE07(self.x-other.x, self.y-other.y, self.p)

    @staticmethod
    def ordreCourbe(p=17):
        """
        >>> ElemtE07.ordreCourbe(11)
        12
        """
        return len(ElemtE07.lDesElements(p))

    def ordrePoint(self):
        """
        >>> ElemtE07(3,10,11).ordrePoint()
        3
        >>> ElemtE07(7,3,11).ordrePoint()
        12
        """
        return len(self.lOrbite())

    def estGenerateur(self):
        """
        >>> ElemtE07(7,3,11).estGenerateur()
        True
        >>> ElemtE07(3,10,11).estGenerateur()
        False
        """
        return ElemtE07.ordreCourbe(self.x.n) == self.ordrePoint()

    @staticmethod
    def lDesElementsGenerateurs(p=47):
        """
        >>> ElemtE07.lDesElementsGenerateurs(11)
        [ElemtE07(4,4,11), ElemtE07(4,7,11), ElemtE07(7,3,11), ElemtE07(7,8,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if e.estGenerateur()]

    @staticmethod
    def lDesElementsDOrdrePremier(p=47):
        """
        >>> ElemtE07.lDesElementsDOrdrePremier(11)
        [ElemtE07(3,1,11), ElemtE07(3,10,11), ElemtE07(5,0,11)]
        """
        return [e for e in ElemtE07.lDesElements(p) if estPremier(e.ordrePoint())]

    @staticmethod
    def elemtE07APartirDeX(x: ElementDeZnZ):
        """
        Renvoie un point avec x ou une valeur proche de x comme abscisse
        >>> ElemtE07.elemtE07APartirDeX(ElementDeZnZ(2,11))
        ElemtE07(2,2,11)
        """
        xx, p = ElementDeZnZ(x), x.n
        assert p % 2 == 1
        y2 = xx**3+7
        while not(y2.estUnCarre()):  # yy est une racine carré
            xx = xx+1
            y2 = xx**3+7
        # print(xx,y2)
        return ElemtE07(xx, y2.racineCarree())

    @staticmethod
    def randElemtE07(p):
        """Renvoie un élément non nul au hasard"""
        return ElemtE07.elemtE07APartirDeX(ElementDeZnZ(randint(0, p-1), p))

    @staticmethod
    def randGenerateurE07(p=47):
        """Renvoie un élément non nul au hasard
        >>> ElemtE07.randGenerateurE07(47).estGenerateur()
        True
        """
        el = ElemtE07.eDesElements(p)
        lel = list(el)
        r = choice(lel)
        while r.ordrePoint() != len(lel):
            r = choice(lel)
        return r

#### PUT BACK HERE


if __name__ == "__main__":

    #ElemtE07.demo(p)


    import doctest
    doctest.run_docstring_examples(ElemtE07.__add__, globals())
    doctest.run_docstring_examples(ElemtE07.double, globals())
    print(ElemtE07.lDesElements(11))
    print(ElemtE07(3, 1, 11)+ElemtE07(4, 4, 11))

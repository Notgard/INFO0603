from arithmetiqueDansZ import *
from Binaire603 import *

class PolF2(list):
    "Polynôme dans F2"

    def __init__(self, x):
        """Défini par une liste d'ElmntZnZ ou un entier
        >>> PolF2([ElementDeZnZ(1,2),0,1,0,1])
        PolF2([ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        >>> PolF2(0b1000110010) #Entier -> Polynome dans F2
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2), ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        >>> PolF2(0)
        PolF2([ElementDeZnZ(0,2)])
        """
        if isinstance(x, PolF2):
            super().__init__(x)

        elif isinstance(x, list):
            lmono= list()
            for val in reversed(x):
                if isinstance(val, ElementDeZnZ):
                    assert val.a != 2, f"{val} is not an element of finite field F2"
                    lmono.append(val)
                elif isinstance(val, int):
                    xpol = ElementDeZnZ(val, 2)
                    lmono.append(xpol)
            super().__init__(lmono)

        elif isinstance(x, int):
            lmono= list()
            binaire = bin(x)[2:]
            for b in reversed(binaire):
                xpol = ElementDeZnZ(int(b), 2)
                lmono.append(xpol)
            super().__init__(lmono)

    def append(self, item):
        if isinstance(item, PolF2):
            self += [i for i in item]
        else:
            super(PolF2, self).append(item)  #append the item to itself (the list)

    def __repr__(self):
        """Renvoie une chaine de caractère représentant le polynome"""
        string="PolF2(["
        for mono in self:
            if isinstance(mono, ElementDeZnZ):
                string+=mono.__repr__()+", "
        return string[:-2] + "])"
    
    @staticmethod
    def monome(degree):
        """
        X² = 100 = X² + 0
        >>> PolF2.monome(2)
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        """
        return PolF2([1] + [0]*degree)

    def degre(self):
        """
        >> > PolF2(0b100011).degre()
        5
        """
        return len(self) - 1
    def distanceHamming(self, other):
        """
        >>> PolF2(0b100011).distanceHamming(PolF2(0b1100011))
        1
        """
        xpol = self+other
        return sum(1 for x in xpol if x.rep == 1)
    def __add__(self,other):
        """
        Effectue un XOR entre 2 polynomes
        >>> PolF2(0b100011)+PolF2(0b1100011)
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        >>> PolF2(0b1100011) + PolF2(0b100011)
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        """
        if isinstance(other, int):
            return PolF2(int(self) ^ other)
        elif isinstance(other, PolF2):
            return PolF2(int(self) ^ int(other))
        # slow version not practical 
        # nself, nother = len(self),  len(other)
        # offset = nother-nself if nself > nother else nself-nother
        # res = None
        # if nself == nother:
        #     res = [sum(x) for x in zip(self, other)]
        # else:
        #     res = [sum(x) for x in zip(self, other)] + self[offset:]
        # return PolF2(res[::-1])    

    def __mul__(self, other):
        """
        >>> PolF2.monome(2)*PolF2.monome(1)
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        """
        #return PolF2(int(self)*int(other))
        if isinstance(other, PolF2):
            res = PolF2(0)
            for key, pol in enumerate(other):
                if pol.rep == 1:
                    # multiply for every 1 value bit
                    shift = key-1 if key > 0 else key
                    respol = int(self) << (shift)
                    res.append(PolF2(respol))
            return res

    
    def __mod__(self,other):
        """
        >>> PolF2(0b11000101) % PolF2(0b11000)
        PolF2([ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        """
        selfpol = PolF2(self)
        otherdeg = other.degre()
        while otherdeg <= selfpol.degre():
            m = PolF2.monome(selfpol.degre() - otherdeg) 
            selfpol = selfpol + other * m
        return selfpol

    def __floordiv__(self, other):
        """
        >>> PolF2(0b11000101)//PolF2(0b11000)
        PolF2([ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)])
        """
        #return PolF2(int(self)//int(other))
        pol = PolF2([])
        selfpol = PolF2(self)
        while other.degre() <= selfpol.degre():
            m = PolF2.monome(selfpol.degre() - other.degre()) 
            pol.append(m)
            selfpol = selfpol + other * m
        return pol
    
    def __int__(self):
        """
        249 = 11111001 = x7 + x6 + x5 + x4 + x3 + 1
        >>> int(PolF2([ElementDeZnZ(1, 2), ElementDeZnZ(0, 2), ElementDeZnZ(1, 2)]))
        5
        >>> int(PolF2([ElementDeZnZ(1,2), ElementDeZnZ(1,2), ElementDeZnZ(1,2), ElementDeZnZ(1,2), ElementDeZnZ(1,2), ElementDeZnZ(0,2), ElementDeZnZ(0,2), ElementDeZnZ(1,2)]))
        249
        """
        string = "".join([str(x.rep) for x in reversed(self)])
        return int(string, 2)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
from Binaire603 import *
from CodeurCA import *
from ChiffreurAffine import *
from arithmetiqueDansZ import *
from sympy import *
import matplotlib
import math

class CodeurHachage(object):
    def __init__(self, nbits=8, chiffreur=ChiffreurAffine, size=6):
        self.chiffreur = chiffreur
        self.offset = size
        self.nbits = 2**nbits
        self.IV = Binaire603([hb % 256 for hb in primerange(0, self.nbits)])

    def __str__(self):
        raise NotImplementedError

    def __repr__(self):
        raise NotImplementedError

    def hash(self, monBin: Binaire603) -> Binaire603:
        h = [hb % 256 for hb in primerange(0, self.nbits)]
        for _ in range(len(monBin)):
            h = self.chiffreur().binCode(Binaire603(h))
            h = h[:self.offset]
        return Binaire603(h)

    def hashDM(self, monBin: Binaire603) -> Binaire603:
        h = self.IV
        for bini in range(len(monBin)):
            h = self.chiffreur(nextprime(monBin[bini])).binCode(h)
        # Faire un unique XOR à la fin avec la valeur initiale
        reshash = Binaire603([x ^ y for x, y in zip(h, self.IV)])
        return reshash

    def binCode(self, monBinD: Binaire603) -> Binaire603:
        nbBitsq = round(log(self.q, 2))+1  # Nombre de bits de p
        nbBitsp = round(log(self.p, 2))+1
        nbOctetsALire = ((nbBitsq*2)-nbBitsp)//8
        Mk = self.init
        # Construction de Merkle-Damgård
        pos = 0, 0
        while pos < len(monBinD):
            x = Mk.a//self.q  # Par def de q x est dans [0..2]
            Mk = ElementDeZnZ(Mk, self.q)
            pos = monBinD.lisOctet(pos)
        i = 0
        while i < nbOctetsALire and pos < len(monBinD):
            oc, pos = monBinD.lisOctet(pos)
            x = x*256+oc  # Inférieur à q car q>2*256+255
            i += 1
        Mk = (self.alpha**x)*(self.beta**Mk.a)
        monBinC = Binaire603([])
        monBinC.ajouteLongueValeur(Mk.a)
        return Binaire603(monBinC[1:])
    
    def proba_collision(self, n, m):
        p = 1 - math.exp((-n*(n-1))/(2*m))
        return p

    def demo_doubon(self, nbits, tries):
        yvalues = zip(range(1, tries+1), range(1, nbits+1))
        plt.plot([i for i in range(0, nbits)], [self.proba_collision(t, n) for t, n in yvalues], linestyle='solid', marker='', color='b')
        plt.xlabel("Nombre de bits de la clé")
        plt.ylabel("Log2(Nombres tentatives)")
        plt.ylim(bottom=0.02)
        plt.title("Probabilité de doublons des clés de hachage parfaite")
        plt.show()


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    hash = CodeurHachage(4)
    binaire = Binaire603("Bonjour les amiss")
    print(hash.hash(binaire))
    print(hash.hashDM(binaire))
    hash.demo_doubon(2**6, 2**16)

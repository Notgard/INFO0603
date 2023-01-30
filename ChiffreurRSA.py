from random import random, randrange
import random
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603
from premiers import *
from typing import Tuple
from time import time

from CodeurCA import CodeurCA

class ChiffreurRSA(CodeurCA):
    """
    Classe correspondant à un chiffreur par bloc en utilisant le chiffrement de RSA
    """
    def __init__(self, keysize=16):
        self.keysize = keysize
        while True:
            rand = random.randrange(2**(keysize-1), 2**keysize)
            if estPremierMR(rand):
                self.p = rand
                break
        while True:
            rand = rand = random.randrange(2**(keysize-1), 2**keysize)
            if estPremierMR(rand) and rand != self.p:
                self.q = rand
                break
        self.n = self.p * self.q

    def __str__(self):
        return f"Chiffreur RSA '{self.p}, {self.q}'"
    def __repr__(self):
        return f"ChiffreurRSA('{self.p},{self.q}')"

    def generateRSAKeys(self)->Tuple[int, int, int]:
        phi_n = indicatriceEuler(self.n)
        e = 2
        while e < phi_n:
            if PGCD(e, phi_n) == 1:
                break
            e = nbPremierSuivant(e)
        d = ElementDeZnZ(e, phi_n).inverse().val
        self.e, self.d = e, d
        return self.e, self.n, self.d


    def binCode(self,monBinD:Binaire603)->List:
        return [(ElementDeZnZ(bin, self.n)**self.e).val for bin in monBinD]


    def binDecode(self,monBinC:Binaire603)->List:
        return [(ElementDeZnZ(bin, self.n)**self.d).val for bin in monBinC]

    def demo():
        monCodeur=ChiffreurRSA(8)
        e, n, d = monCodeur.generateRSAKeys()
        for k in range(3):
            monBin=Binaire603.exBin603(num=k,taille=25)
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurRSA(9)
        e, n, d = chif.generateRSAKeys()
        code = chif.binCode(lb)
        lbc=Binaire603([bin%256 for bin in code])
        lbd=Binaire603(chif.binDecode(code))
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    start = time()
    chif = ChiffreurRSA(10)
    e, n, d = chif.generateRSAKeys()
    end = time()

    print("Temps passé pour générer les clés RSA", end - start)

    print("e:", e, "n:", n, "d", d)

    montext='Bonjour les amis'
    binaire = Binaire603(montext)
    print("Message Originale >>", binaire.toString(), [bin for bin in binaire])
    code = chif.binCode(binaire)
    print("Message chiffré >>", Binaire603([c%256 for c in code]).toString(), code)
    decode = chif.binDecode(code)
    print("Message déchiffré >>", Binaire603(decode).toString(), decode)

    ChiffreurRSA.demo()
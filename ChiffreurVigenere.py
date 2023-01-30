# Créé par vala0004, le 01/12/2021 en Python 3.7
# Créé par vala0004, le 30/11/2021 en Python 3.7
from math import log
from random import random,randint
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603
import string

from CodeurCA import CodeurCA

class ChiffreurVigenere(CodeurCA):
    """"""
    def __init__(self, key, alphabet=""):
        if not isinstance(key, str):
            raise TypeError("key must be a string")
        self.key = key
        self.alphabet = alphabet

    def __str__(self):
        return f"Chiffreur Vigenère de clé '{self.key}'"
    def __repr__(self):
        return f"ChiffreurVigenère('{self.key}')"

    def inRange(self, min, value, offset, m):
        return (value - min + (offset % m) + m) % m + min


    def binCode(self,monBinD:Binaire603)->Binaire603:
        """
        >>> ChiffreurVigenere("Bonjour").binCode(Binaire603("hello"))
        Binaire603([ 0xaa, 0xd4, 0xda, 0xd6, 0xde])
        """
        if len(self.alphabet) == 0:
            binKey = [ord(keyC) for keyC in self.key]
        else:
            binKey = [self.alphabet.index(keyC) for keyC in self.key]
        #return Binaire603([self.inRange(65, bin, binKey[index%len(self.key)], 122-64) for index, bin in enumerate(monBinD)])
        return Binaire603([(bin + binKey[index%len(self.key)]) % 256 for index, bin in enumerate(monBinD)])

    def binDecode(self,monBinC:Binaire603)->Binaire603:
        """
        >>> binCode = ChiffreurVigenere("Bonjour").binCode(Binaire603("hello")); ChiffreurVigenere("Bonjour").binDecode(binCode).toString()
        'hello'
        """
        if len(self.alphabet) == 0:
            binKey = [ord(keyC) for keyC in self.key]
        else:
            binKey = [self.alphabet.index(keyC) for keyC in self.key]
        return Binaire603([(bin - binKey[index%len(self.key)]) % 256 for index, bin in enumerate(monBinC)])

    def demo():
        monCodeur=ChiffreurVigenere("key")
        for k in range(3):
            monBin=Binaire603.exBin603(num=k,taille=25)
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurVigenere("key")
        lbc=chif.binCode(lb)
        lbd=chif.binDecode(lbc)
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurVigenere.demo()
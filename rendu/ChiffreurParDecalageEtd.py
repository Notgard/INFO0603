# Créé par vala0004, le 01/12/2021 en Python 3.7
# Créé par vala0004, le 30/11/2021 en Python 3.7
from math import log
from random import random,randint
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603

from CodeurCA import CodeurCA
class ChiffreurParDecalage(CodeurCA):
    """Classe représentant un chiffreur par décalage
    """
    def __init__(self, decal=10):
        self.decal = decal

    def __str__(self):
        return f"Chiffreur par décalage de {self.decal}"
    def __repr__(self):
        return f"ChiffreurParDecalage({self.decal})"


    def binCode(self,monBinD:Binaire603)->Binaire603:
        """
        >>> ChiffreurParDecalage(2).binCode(Binaire603([ 0x01, 0x02, 0x03, 0x04, 0xFF]))
        Binaire603([ 0x03, 0x04, 0x05, 0x06, 0x01])
        >>> (ChiffreurParDecalage(1).binCode(Binaire603("Bonjour"))).toString()
        'Cpokpvs'
        """
        return Binaire603([(bin + self.decal) % 256 for bin in monBinD])

    def binDecode(self,monBinC:Binaire603)->Binaire603:
        """
        >>> ChiffreurParDecalage(2).binDecode(Binaire603([1,2,3,4,255]))
        Binaire603([ 0xff, 0x00, 0x01, 0x02, 0xfd])
        """
        return Binaire603([(bin - self.decal) % 256 for bin in monBinC])

    def demo():
        monCodeur=ChiffreurParDecalage(13)
        for k in range(3):
            monBin=Binaire603.exBin603(num=k,taille=25)
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurParDecalage(1)
        lbc=chif.binCode(lb)
        lbd=chif.binDecode(lbc)
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurParDecalage.demo()
    print([bin for bin in Binaire603("helloaz AZ")])
    print(Binaire603("helloza"))
    print((ChiffreurParDecalage(0).binCode(Binaire603("z"))).toString())

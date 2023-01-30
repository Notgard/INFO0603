
from Binaire603 import *
from CodeurCA import *
from bijectionDOctets import fPermut

class CodeurHachage(CodeurCA):
    def __init__(self, f = fPermut):
        self.f = f

    def __str__(self):
        raise NotImplementedError# Ne pas toucher
    def __repr__(self):
        raise NotImplementedError# Ne pas toucher

    def binCode(self,monBinD:Binaire603)->Binaire603:
        res = 0
        for bin in monBinD:
            res += bin * 16 ^ 0b00001111
        return Binaire603([res, res-1])

    def binDecode(self,monBinC:Binaire603)->Binaire603:
        raise NotImplementedError

if __name__ == "__main__":
    import doctest
    doctest.testmod()
##    monCodeur=CodeurCA() #A modifier si repris dans une classe en héritant
##    for k in range(5):
##        monBin=Binaire603.exBin603(num=k,taille=25)
##        print("Bin:",monBin)
##        monBinCr=monCodeur.binCode(monBin)
##        print("Bin Codée:",monBinCr)
##        print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)



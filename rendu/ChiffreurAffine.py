from arithmetiqueDansZ import *
from Binaire603 import Binaire603

from CodeurCA import CodeurCA

class ChiffreurAffine(CodeurCA):
    """"""
    def __init__(self, a=13, b=5):
        self.a = ElementDeZnZ(a, 256)
        fstring = f"Une exception a été détectée lors de la création du chiffrement ({self.a} n'est pas premier avec 256)."
        assert self.a.estInversible(), fstring
        self.b = ElementDeZnZ(b, 256)

    def __str__(self):
        return f"Chiffreur affine avec {self.a} et {self.b}"
    def __repr__(self):
        return f"ChiffreurAffine({self.a}, {self.b})"


    def binCode(self,monBinD:Binaire603)->Binaire603:
        """
        >>> ChiffreurAffine(3, 15).binCode(Binaire603([ 0x01, 0x02, 0x03, 0x04, 0xFF]))
        Binaire603([ 0x12, 0x15, 0x18, 0x1b, 0x0c])
        >>> (ChiffreurAffine(1, 1).binCode(Binaire603("Bonjour"))).toString()
        'Cpokpvs'
        """
        return Binaire603([(self.a * bin + self.b).rep for bin in monBinD])

    def binDecode(self,monBinC:Binaire603)->Binaire603:
        """
        >>> ChiffreurAffine(5, 11).binDecode(Binaire603([1,2,3,4,255]))
        Binaire603([ 0xfe, 0xcb, 0x98, 0x65, 0x64])
        """
        invA = self.a.inverse().rep
        return Binaire603([(invA * (bin - self.b)).rep for bin in monBinC])

    def demo():
        monCodeur=ChiffreurAffine()
        for k in range(3):
            monBin=Binaire603.exBin603(num=k,taille=25)
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurAffine()
        lbc=chif.binCode(lb)
        lbd=chif.binDecode(lbc)
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")
        print()
        monBin = Binaire603([0x00, 0x01, 0x02, 0x010, 0x20, 0x40, 0x80])
        for monCodeur in [ChiffreurAffine(3, 5) , ChiffreurAffine(1, 1) , ChiffreurAffine(1, 0), ChiffreurAffine(7, 5)]:
            print(f"Codage avec {monCodeur} : ")
            print("Bin : ", monBin)
            monBinC = monCodeur.binCode(monBin)
            print("Bin Codé: ", monBinC)
            monBinD = monCodeur.binDecode(monBinC)
            print("Bin Décodé:", monBinD)
            print("monBinD (décodé) est égal à Monbin ?", monBinD==monBin)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    ChiffreurAffine.demo()

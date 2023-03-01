from ElemtE07Etd import *
from Binaire603 import *
from Texte603 import *

M = ElemtE07.elemtE07APartirDeX(ElemtE07(m, self.p))
monBinC.ajouteMot40b(MP.__hash__())
h, pos = monBinC.lisMot(5, pos)
MP = ElemtE07.ElemtE07DepuisHash(h, self.p)

class CodeurE0765537(object):
    """
    Codeur à partir de la courbe elliptique sur F65537
    """
    def __init__(self, a, B, G=ElemtE07(47106, 21934, 65537), p=65537):
        NotImplementedError
    def __str__(self):
        return f"CodeurE0765537 avec la clé privé {self.a =} et sa clé publique {self.A =}, la clé publique d'un tier {self.B = }, avec comme point générateur {self.G =} sur F{self.p}"
    def __repr__(self):
        NotImplementedError
    def binCode(self, monBinD: Binaire603) -> Binaire603:
        NotImplementedError
    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        NotImplementedError

if __name__ == "__main__":
    # Exemple d'utilisation ;
    mes = Texte603("Bonjour les amis !")
    print(f"Message à coder :{mes}")
    binc = ca.binCode(mes.toBinaire603())
    print(f"Message codé avec la clé secrète de {a=} et la clé publique {B=}: {Texte603(binc)}")
    bind = cb.binDecode(binc)
    print(f"Message décodé avec la clé secrète de {b=} et la clé publique {A=}: {Texte603(bind)}")

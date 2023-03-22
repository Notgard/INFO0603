from PolF2 import *
from CodeurCA import *

class CodeurCRC8(CodeurCA):
    """CodeurCRC codant en 40bits des blocs 32bits avec CRC sur 8bits"""

    def __init__(self, polG=PolF2(0b110011011)):
        # Choix du polynome générateur
        if isinstance(polG, CodeurCRC8):
            self.polG = polG.polG
        elif isinstance(polG, PolF2):
            self.polG = polG

    def blocCode(self, M, verbose=False):
        """Renvoie M codé en CRC avec un octet de plus
        >>> print(f"0x{CodeurCRC8().blocCode(0xab345678):x}")
        0xab34567821
        """
        polM = PolF2(M)
        assert polM.degre() >= self.polG.degre(), f"({polM.degre()}<{self.polG.degre()}) Le polynome générateur {self.polG} devrait avoir un degrée inférieur ou égal au degrée du message"
        # Ajout de k bits de valeur 0
        k = self.polG.degre()
        polMx = polM * PolF2.monome(k)
        reste = polMx % self.polG
        # Ajout des bits du reste
        polT = polM + reste
        return int(polT)
    
    def estBlocValide(self, valc):
        """
        >>> CodeurCRC8().estBlocValide(0xab34567821)
        True
        >>> CodeurCRC8().estBlocValide(0xab34567820)
        """
        return int(PolF2(valc) % self.polG) == 0

    def blocValideLePlusProche(self, valc):
        """
        >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab34567821):x}")
        0xab34567821
        >>> print(f"0x{CodeurCRC8().blocValideLePlusProche(0xab35567821):x}")
        0xab34567821
        """

    def blocDecode(self, valc):
        """
        >>> print(f"0x{CodeurCRC8().blocDecode(0xab34567821):x}")
        0xab345678
        >>> print(f"0x{CodeurCRC8().blocDecode(0xbb34567821):x}")
        0xab345678
        """
    def blocAvecErreur(val, nbBits=32, nbErreurs=1):
        """Renvoie le bloc val avec nbErreurs bits changés"""

    def binCode(self, monBinD, verbose=True, nbErreurs=0):
        pass

    def binDecode(self, monBinC):
        pass

    def testDistance(self, nmax=0x101):
        """Affiche la distance minimales entre les codage des blocs 0 ) nmax"""

if __name__ == '__main__':
    import doctest
    doctest.testmod()

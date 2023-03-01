from Binaire603 import *
from CodeurCA import *
from Image603Etd import *


class CompresserRLE(CodeurCA):
    """ Class CompresserRLE (RunLength Encoding) """

    def __init__(self, char=61):
        if (isinstance(char, str)):
            self.char = ord(char)
        else:
            self.char = char

    def __str__(self):
        return f"CompresserRLE()"

    def __repr__(self):
        return f"CompresserRLE()"

    def binCode(self, monBinD: Binaire603, PCX=False) -> Binaire603:
        """
        Fonction qui encode un Binaire603
        """
        monBinC = []
        count = 1  # compteur
        tmp = monBinD[0]  # valeur precedente

        for ibin in range(1, len(monBinD)):
            if monBinD[ibin] == tmp:
                count += 1
                if PCX:  # Compression PCX
                    if count == 63:
                        monBinC.append(count | 0xC0)
                        monBinC.append(tmp)
                        count = 1
                else:
                    if count == 255:
                        monBinC.append(count)
                        monBinC.append(tmp)
                        count = 1
            else:
                if PCX:  # compression PCX
                    if count > 1:
                        monBinC.append(count | 0xC0)
                        monBinC.append(tmp)
                    else:
                        monBinC.append(tmp)
                else:
                    monBinC.append(count)
                    monBinC.append(tmp)
                tmp = monBinD[ibin]
                count = 1
        if PCX:
            if count > 1:
                monBinC.append(count | 0xC0)
                monBinC.append(tmp)
            else:
                monBinC.append(tmp)
        else:
            monBinC.append(count)
            monBinC.append(tmp)

        return Binaire603(monBinC)

    def binDecode(self, monBinC: Binaire603, PCX=False) -> Binaire603:
        """
        Fonction qui decode un Binaire603
        """
        i = 0
        monBinD = []

        while (i < len(monBinC)):
            if PCX:
                count = monBinC[i] & 0x3F
                if monBinC[i] & 0xC0: #verification d'octet répeté
                    octet = monBinC[i + 1]
                    i += 2
                else: #pas de répétition 
                    octet = monBinC[i] 
                    i += 1
                for _ in range(count): # decode toutes les répetitions
                    monBinD.append(octet)
            else:
                if (monBinC[i] == self.char):
                    monBinD += [monBinC[i+2]] * monBinC[i+1]
                    i += 3
                else:
                    monBinD.append(monBinC[i])
                    i += 1
        return Binaire603(monBinD)

    def demo():
        comp = CompresserRLE()
        PCX = False
        print("\nRLE: Format classique\n")
        for file in ["img/Coul10a.bmp", "img/Coul10b.bmp"]:
            print("-----------------------------------------------------------------------")
            print(f"\nCompression de l'image {file} :\n")
            print("-----------------------------------------------------------------------")
            img = Image603.imgDepuisBmp(file)
            imgBinaire = img.toBinaire603()
            monBinC = comp.binCode(imgBinaire, PCX)
            print(monBinC)
            monBinD = comp.binDecode(monBinC, PCX)
            print(monBinD)
        PCX = True
        print("\nCodage RLE: Format PCX\n")
        for file in ["img/Coul10a.bmp", "img/Coul10b.bmp"]:
            print("-----------------------------------------------------------------------")
            print(f"\nCompression de l'image {file} :\n")
            print("-----------------------------------------------------------------------")
            img = Image603.imgDepuisBmp(file)
            imgBinaire = img.toBinaire603()
            monBinC = comp.binCode(imgBinaire, PCX)
            print(monBinC)
            monBinD = comp.binDecode(monBinC, PCX)
            print(monBinD)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    CompresserRLE.demo()

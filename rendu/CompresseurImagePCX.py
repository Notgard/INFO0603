from Binaire603 import *
from CodeurCA import *
from Image603Etd import *
from CompresseurRLE import *

class CompresseurImagePCX(CodeurCA):
    """Class CompresseurImagePCX permettant de compresser une image en utilisant le format PCX du codage RLE"""

    def __init__(self):
        self.char = 0xC0

    def __str__(self):
        return f"CompresseurImagePCX()"

    def __repr__(self):
        return f"CompresseurImagePCX()"

    def binCode(self, imgBinC: Binaire603) -> Binaire603:
        """
        Fonction qui encode le Binaire603 d'une image Image603 au format PCX, dans un Binaire603
        """

        img = Image603.fromBinaire603(imgBinC)
        monBin = [img.ht, img.lg]
        palette = img.dPalette()
        indexCoul = [palette[img.coul[ix][iy]][0] for ix, iy in img.iterXY()]

        monBin += indexCoul

        monBinC = Binaire603(monBin)
        return (CompresserRLE()).binCode(monBinC)

    def binDecode(self, monBinC: Binaire603) -> Binaire603:
        """
        Fonction qui decode un Binaire603
        """
        #Décompression du Binaire603
        uncompressedBin = (CompresserRLE()).binDecode(monBinC)
        #Recuperer le Binaire603 de l'image
        #Récuperer les indxes des pixels
        #reconstruire l'image
        #renvoyer le Binaire603 de l'image Image603


    def demo():
        comp_pcx = CompresseurImagePCX()
        for file in ["img/Coul10a.bmp", "img/Coul10b.bmp"]:
            print("-----------------------------------------------------------------------")
            print(f"\nCompression de l'image {file}...\n")
            print("-----------------------------------------------------------------------")
            img = Image603.imgDepuisBmp(file)
            imgBincode = img.toBinaire603()
            pcxCompressedBinCode = comp_pcx.binCode(imgBincode)
            print("Le Binaire 603")
            print(pcxCompressedBinCode)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    CompresseurImagePCX.demo()

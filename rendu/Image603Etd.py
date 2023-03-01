# Créé par Nous, le 15/11/2021 en Python 3.7
from PIL import Image  # Simplement pour pouvoir afficher les images
from Binaire603 import *


class Image603(object):
    def __init__(self, lg=200, ht=100):
        "Une Image603 contient un tableau de triplet d'octet représentant la couleur de chaque pixel"
        self.lg, self.ht = lg, ht
        self.coul = [[(ix % 256, iy % 256, (ix*ix+iy*iy) % 256)
                      for iy in range(ht)] for ix in range(lg)]

    def exImage603(num=0, lg=20, ht=20):
        """Renvoie une image lg×ht pixels en exemple avec num :
            0: image standart
            1: image blanche
            2: image ligne et verticales horizontales
            """
        if num == 0:
            res = Image603(lg, ht)
        elif num == 1:
            res = Image603(lg, ht)
            for ix, iy in res.iterXY():
                res.coul[ix][iy] = (255, 255, 255)
        elif num == 2:
            res = Image603(lg, ht)
            for ix, iy in res.iterXY():
                if ix % 2 == 0:
                    if iy % 2 == 0:
                        res.coul[ix][iy] = (0, 0, 0)
                    else:
                        res.coul[ix][iy] = (255, 0, 0)
                else:
                    if iy % 2 == 0:
                        res.coul[ix][iy] = (0, 255, 0)
                    else:
                        res.coul[ix][iy] = (0, 0, 255)
        return res

    def iterXY(self):
        """Un itérateur renvoyant (i,j) pour tous les pixels de l'image
            for ix, iy in self.iterXY():
                print(f"Le pixel({ix},{iy} a pour couleur le triplet {self.coul[ix][iy]}")
                """
        for ix in range(self.lg):
            for iy in range(self.ht):
                # Un return mais qui reprendra l'exécution à cet endroit au prochain appel
                yield (ix, iy)

    def affiche(self):
        monImagePIL = Image.new('RGB', (self.lg, self.ht))
        for ix, iy in self.iterXY():
            monImagePIL.putpixel((ix, iy), self.coul[ix][iy])
        monImagePIL.show()

    def imgDepuisBmp(nom_fichier="NB10", verbose=True):
        """Renvoie une Image603 d'après un fichier BMP à 16 couleurs
        https://www.commentcamarche.net/contents/1200-bmp-format-bmp"""

        b = Binaire603.bin603DepuisFichier(nom_fichier, verbose=verbose)
        if verbose:
            print(f"Signature : {b[0]:x}{b[1]:x}")
        taille = b[2]+256*(b[3]+256*(b[4]+256*(b[5])))
        if verbose:
            print(f"Taille : {taille}octets")

        if verbose:
            print(f"Champs réservé : {b[6:10]}")

        pos = 10
        offset = b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))
        if verbose:
            print(f"Offset (décalage) de l'image : {offset} octets")

        pos = 14
        tailleEntete = b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))
        if verbose:
            print(f"Taille de l'entête : {tailleEntete} octets")

        pos = 18
        #print(f"largeur : {b[pos]:x},{b[pos+1]:x},{b[pos+2]:x},{b[pos+3]:x}octets")
        largeur = b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))
        if verbose:
            print(f"largeur : {largeur} px")
        pos = 22
        hauteur = b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))
        if verbose:
            print(f"hauteur : {hauteur} px")
        pos = 26
        if verbose:
            print(f"Nb Plans : {b[pos]+256*(b[pos+1])}")
        pos = 28
        profCodage = b[pos]+256*(b[pos+1])
        if verbose:
            print(
                f"Prof de codages (nb de bits pour coder une couleur) : {profCodage}bits")
        nbCoul = 2**(profCodage)
        pos = 30
        if verbose:
            print(
                f"Méthode de compression : {b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))}")
        pos = 34
        if verbose:
            print(
                f"Taille totale : {b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))}octets")
        pos = 38
        if verbose:
            print(
                f"Nbpx par m H : {b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))}octets")
        pos = 42
        if verbose:
            print(
                f"Nbpx par m H : {b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))}octets")
        pos = 46
        nbCoulPalette = b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))
        if verbose:
            print(f"NbCouleur de la palette : {nbCoulPalette} couleurs")

        pos = 50
        if verbose:
            print(
                f"NbCouleur importantes de la palette : {b[pos]+256*(b[pos+1]+256*(b[pos+2]+256*(b[pos+3])))}octets")
        pos = 54
        lcoul = []
        for k in range(nbCoulPalette):
            if verbose:
                print(
                    f"Couleur {k}:({b[pos]:x},{b[pos+1]:x},{b[pos+2]:x}),{b[pos+3]:x}")
            lcoul += [(b[pos+2], b[pos+1], b[pos])]  # RGB
            pos += 4
        if verbose:
            print(f"Position :{pos} et Offset : {offset}")
        pos = offset
        monImage603 = Image603(largeur, hauteur)
        if profCodage == 4:
            nbOctetsParLigne = hauteur//2+hauteur % 2
            for i in range(hauteur):
                ch = ""
                for j in range(nbOctetsParLigne):
                    if verbose:
                        ch += f"{b[pos]//16:x}"+f"{b[pos]%16:x}"
                    ix, iy = (2*j, hauteur-1-i)

                    monImage603.coul[ix][iy] = lcoul[b[pos]//16]
                    monImage603.coul[ix+1][iy] = lcoul[b[pos] % 16]

                    pos += 1
                if verbose:
                    print(ch)
                # Chaque ligne de l'image doit comporter un nombre total d'octets qui soit un multiple de 4
                if (nbOctetsParLigne) % 4 > 0:
                    pos += (4-(nbOctetsParLigne % 4))
        elif profCodage == 8:
            nbOctetsParLigne = hauteur
            for i in range(hauteur):
                ch = ""
                for j in range(nbOctetsParLigne):
                    if verbose:
                        ch += f"{b[pos]:x}"
                    ix, iy = (j, hauteur-1-i)
                    monImage603.coul[ix][iy] = lcoul[b[pos]]
                    pos += 1
                if verbose:
                    print(ch)
                # Chaque ligne de l'image doit comporter un nombre total d'octets qui soit un multiple de 4
                if (nbOctetsParLigne) % 4 > 0:
                    pos += (4-(nbOctetsParLigne % 4))
        elif profCodage == 24:
            nbOctetsParLigne = hauteur
            for i in range(hauteur):
                ch = ""
                for j in range(nbOctetsParLigne):
                    if verbose:
                        ch += f"{b[pos]:x}"
                    ix, iy = (j, hauteur-1-i)
                    monImage603.coul[ix][iy] = (b[pos], b[pos+1], b[pos+2])
                    pos += 3
                if verbose:
                    print(ch)
                # Chaque ligne de l'image doit comporter un nombre total d'octets qui soit un multiple de 4
                if (nbOctetsParLigne) % 4 > 0:
                    pos += (4-(nbOctetsParLigne % 4))
        return monImage603

    def dPalette(self):
        """renvoie le dictionnaire de l'index et de l'effectif des couleurs
        la première couleur est à l'index 0
        dCoul[(255,0,0)]==(5,18) signifie que le rouge est à l'index 5 et est utilisé par 18 pixels
        >>> len(Image603.exImage603(2).dPalette()) #Nombre de couleurs
        4
        >>> Image603.exImage603(2).dPalette()[(255,0,0)] #Effectif des pixels rouges
        (1, 100)
        """
        dCoul = {}
        indx = 0
        for ix, iy in self.iterXY():
            co = self.coul[ix][iy]
            if not(co in dCoul):
                dCoul[co] = (indx, 1)
                indx += 1
            else:
                dCoul[co] = (dCoul[co][0], dCoul[co][1]+1)
        return dCoul
    
    def toBinaire603(self) -> Binaire603:
        "renvoie un binaire603 d'après l'image"
        lbin = [self.lg, self.ht]
        for ix, iy in self.iterXY():
            r, g, b = self.coul[ix][iy]
            lbin += [r, g, b]
        return Binaire603(lbin)

    def fromBinaire603(monBin):
        "renvoie une image d'après un binaire603 généré par toBinaire603"
        lg, ht = monBin[:2]
        coul = []
        for ibin in range(2, len(monBin), 3):
            rgb = []
            for icol in range(ibin, ibin+3):
                rgb.append(monBin[icol])
            coul.append(tuple(rgb))
        cl = list()
        for d in range(1, ht+1):
            cl.append(coul[(d*lg)-lg:d*lg])
        img = Image603(lg, ht)
        img.coul = cl
        return img

    def demo():
        im2 = Image603.imgDepuisBmp("img/Coul10a.bmp", verbose=True)
        im2.affiche()
        print(im2.dPalette())
        mb=im2.toBinaire603()
        print("Le Binaire 603")
        print(mb)
        im3 = Image603.fromBinaire603(mb)
        print("Image récupérée du Binaire603")
        print(im3.dPalette())
        print(im3.coul)
        im3.affiche()



if __name__ == "__main__":
    import doctest
    doctest.testmod()
    Image603.demo()

from math import log
from random import random,randint
import random
from arithmetiqueDansZEtd import *
from Binaire603 import Binaire603
from bijectionDOctets import fPermut

from CodeurCA import CodeurCA

class ChiffreurFeistel(CodeurCA):
    """
    Classe correspondant à un chiffreur par bloc en utilisant le chiffrement de Feistel
    """
    def __init__(self, rounds:int, key:int, function=fPermut.f):
        self.f = function
        self.key = key
        self.rounds = rounds

    def __str__(self):
        return f"Chiffreur Feistel '{self.f}'"
    def __repr__(self):
        return f"ChiffreurFeistel('{self.f}')"


    def binCode(self,monBinD:Binaire603)->Binaire603:
        random.seed(self.key)
        lk=[random.randint(0, 255) %16 for _ in range(self.rounds)] #16o blocks
        bytesChiffre=[]
        for oc in monBinD:
            left, right = (oc & 0b11110000) >> 4, oc & 0b00001111
            for r in range(self.rounds):
                k = lk[r]
                left, right = right, left ^ self.f(k, right)
            bytesChiffre.append((left << 4) | right)
        return Binaire603(bytesChiffre)


    def binDecode(self,monBinC:Binaire603)->Binaire603:
        random.seed(self.key)
        lk=[random.randint(0, 255) %16 for _ in range(self.rounds)] #16o blocks
        bytesDechiffre = []
        for oc in monBinC:
            left, right = (oc & 0b11110000) >> 4, oc & 0b00001111
            for r in reversed(range(self.rounds)):
                k = lk[r]
                right, left = left, right ^ self.f(k, left)
            bytesDechiffre.append((left << 4) | right)
        return Binaire603(bytesDechiffre)

    def demo():
        monCodeur=ChiffreurFeistel(12345, 6)
        for k in range(3):
            monBin=Binaire603.exBin603(num=k,taille=25)
            print("Bin:",monBin)
            monBinCr=monCodeur.binCode(monBin)
            print("Bin Codée:",monBinCr)
            print("monBinCr décodé est égal à Monbin ?",monCodeur.binDecode(monBinCr)==monBin)

        montext='Bonjour les amis !'
        lb=Binaire603(montext)
        chif=ChiffreurFeistel(12345, 6)
        lbc=chif.binCode(lb)
        lbd=chif.binDecode(lbc)
        print(f"{chif} a codé le texte '{montext}' en '{lbc.toString()}' et a décodé en '{lbd.toString()}' ")


if __name__ == "__main__":
    import doctest
    doctest.testmod()   
    ChiffreurFeistel.demo()
    
    montext='Bonjour'
    lb=Binaire603(montext)
    chif=ChiffreurFeistel(12345, 6)
    lbc=chif.binCode(lb)
    print(lbc.toString())
    lbd=chif.binDecode(lbc)
    print(lbd.toString()) 

    binaire = Binaire603("Bonjour")
    print("Original ", binaire.toString())
    def encrypt(binaire):
        key = 4
        r = 6
        random.seed(key)
        lk=[random.randint(0, 255) %16 for _ in range(r)]
        #print(lk)
        b=[]
        for oc in binaire:
            #print(oc)
            left, right = (oc & 0b11110000) >> 4, oc & 0b00001111
            #print(bin(oc), bin(left), bin(right))
            for i in range(r):
                k = lk[i]
                #print("key ", k)
                left, right = right, left ^ fPermut.f(k, right)
                #print("left and right ", bin(left), bin(right))
                #print("combined ", (left << 4) | right, bin((left << 4) | right))
                #print()
            b.append((left << 4) | right)
        bina = Binaire603(b)
        return bina

    bina = encrypt(binaire)

    print("Encoded ", bina.toString())

    def decrypt(bina):
        key = 4
        r = 6
        random.seed(key)
        lkk=[random.randint(0, 255) %16 for _ in range(r)]
        #print(lkk)
        newbin = []
        for j in bina:
            #print(j)
            left, right = (j & 0b11110000) >> 4, j & 0b00001111
            #print(bin(j), bin(left), bin(right))
            for i in reversed(range(r)):
                k = lkk[i]
                #print("key ", k)
                right, left = left, right ^ fPermut.f(k, left)
                #print("left and right ", bin(left), bin(right))
                #print("combined ", (left << 4) | right, bin((left << 4) | right))
                #print()
            newbin.append((left << 4) | right)
        return Binaire603(newbin)
    newbin = decrypt(bina)
    print("Decoded ", newbin.toString())

    print(binaire.toString())
    chif = ChiffreurFeistel(6, 4)

    code = chif.binCode(binaire)
    bina = encrypt(binaire)
    print("Encoded ", bina.toString())
    print("Encoded with cipher ", code.toString())

    decode = chif.binDecode(code)
    newbin = decrypt(bina)
    print("Decoded ", newbin.toString())
    print("Decoded with cipher ", decode.toString())

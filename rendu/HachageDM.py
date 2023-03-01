import hashlib
from Binaire603 import *
from CodeurCA import *
from ChiffreurAffine import *
from arithmetiqueDansZ import *

class CodeurHachage(object):
    def __init__(self, chiffreur: CodeurCA = ChiffreurAffine):
        self.chiffreur = chiffreur
        self.rounds = 16
        self.offset = 4

    def __str__(self):
        raise NotImplementedError
    def __repr__(self):
        raise NotImplementedError

    def hash(self, monBin: Binaire603) -> Binaire603:
        h = monBin[:self.offset]
        for _ in range(self.rounds):
            h = self.chiffreur.binCode(Binaire603(h))
            h += h[:self.offset]
        return h
    
    def binCode(self,monBinD:Binaire603)->Binaire603:
        nbBitsq=round(log(self.q,2))+1 #Nombre de bits de p
        nbBitsp=round(log(self.p,2))+1
        nbOctetsALire=((nbBitsq*2)-nbBitsp)//8
        Mk=self.init
        #Construction de Merkle-Damgård
        pos=0,0
        while pos<len(monBinD):
            x=Mk.a//self.q #Par def de q x est dans [0..2]
            Mk=ElementDeZnZ(Mk,self.q)
            pos=monBinD.lisOctet(pos)
        i=0
        while i<nbOctetsALire and pos<len(monBinD):
            oc,pos=monBinD.lisOctet(pos)
            x=x*256+oc #Inférieur à q car q>2*256+255
            i+=1
        Mk=(self.alpha**x)*(self.beta**Mk.a)
        monBinC=Binaire603([])
        monBinC.ajouteLongueValeur(Mk.a)
        return Binaire603(monBinC[1:])


if __name__ == "__main__":
    import doctest
    doctest.testmod()



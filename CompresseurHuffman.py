from Binaire603 import *
import BinaryTree


class CompresseurHuffman(object):
    def __init__(self) -> None:
        pass

    def dicoFrequences(self, monBin: Binaire603 = None):
        assert isinstance(monBin, Binaire603), "monBin n'est pas un Binaire603"
        lf = monBin.lFrequences()
        lbin = sorted(list(set([strbin for strbin in monBin.toString()])))
        lf = list(filter(lambda x: x != 0, lf))
        return dict(zip(lbin, lf))

    def arbreDepuisListe(lp):
        pass


if __name__ == "__main__":
    comp = CompresseurHuffman()
    binaire = Binaire603("aaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbbccdeeeeeeeeeeeeeeeeeee")
    dico = comp.dicoFrequences(binaire)
    print(dico)
    print(dico.items())

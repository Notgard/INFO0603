from Binaire603 import *
from BinaryTree import *


class CompresseurHuffman(object):
    def __init__(self) -> None:
        pass
    
    @staticmethod
    def dicoFrequences(monBin: Binaire603 = None, binValue=False):
        assert isinstance(monBin, Binaire603), "monBin n'est pas un Binaire603"
        lf = monBin.lFrequences()
        if binValue:
            lbin = list(set([bin for bin in monBin]))
        else:
            lbin = sorted(list(set([strbin for strbin in monBin.toString()])))
        lf = list(filter(lambda x: x != 0, lf))
        return dict(zip(lbin, lf))

    @staticmethod
    def arbreDepuisListe(lp: list, verbose=False) -> BinaryTree:
        while len(lp) != 1:
            lp.sort(key = lambda x: x.data if isinstance(x, BinaryTree) else x[1], reverse=True)
            if verbose:
                print(">>>> ", lp)
            br1 = lp.pop()
            br2 = lp.pop()
            if(all(isinstance(br, tuple) for br in [br1, br2])):
                tree = BinaryTree()
                tree.add(br1)
                tree.add(br2)
                lp.append(tree)
            elif isinstance(br1, BinaryTree):
                br1.add(br2)
                lp.append(br1)
            elif isinstance(br2, BinaryTree):
                br2.add(br1)
                lp.append(br2)
        return lp[0]
    
    @staticmethod
    def dicoHuffmanDepuisArbre(tree: BinaryTree) -> tuple:
        def dicoRecursive(dc, tree, prefix=""):
            if not tree.estFeuille():
                dicoRecursive(dc, tree.left, prefix + "0")
                dicoRecursive(dc, tree.right, prefix + "1")
            else:
                dc[tree.data[0]] = prefix
        map = dict()
        dicoRecursive(map, tree)
        map = dict(sorted(map.items(), key=lambda item: item[1], reverse=False))
        inv_map = {v: k for k, v in map.items()}
        return (inv_map, map)

    @staticmethod
    #L'encode ne fonctionne pas bien avec des valeur de Binaire603 reflétant le dictionnaire de Huffman
    def codageHuffman(monBin: Binaire603, binValue=False):
        if binValue:
            huffmanString = "".join(str(bin) for bin in monBin)
        else:
            huffmanString = "".join(bin for bin in monBin.toString())
        df = CompresseurHuffman.dicoFrequences(monBin, binValue)
        lp = [item for item in df.items()]
        arbre = CompresseurHuffman.arbreDepuisListe(lp)
        dico = CompresseurHuffman.dicoHuffmanDepuisArbre(arbre)
        for code, index in dico[0].items():
            if binValue:
                huffmanString = huffmanString.replace(str(index), code)
            else:
                huffmanString = huffmanString.replace(index, code)
        cursor = 0
        dicoRepetition = dict.fromkeys(dico[0].keys(), 0)
        codage = list(dico[1].values())
        while cursor < len(huffmanString):
            offset = cursor+1
            while True:
                if huffmanString[cursor:offset] not in codage:
                    offset += 1
                else:
                    dicoRepetition[huffmanString[cursor:offset]] += 1
                    break
            cursor = offset
        dicoInv = {v: k for k, v in dicoRepetition.items()}
        return (dico, dicoRepetition, dicoInv)
    
    def binCode(self, monBin: Binaire603):
        lbin = []
        dicoHuffman = CompresseurHuffman.codageHuffman(monBin, True)[0]
        for bin in monBin:
            lbin.append(dicoHuffman[1][bin])
        print("".join(lbin))
        return Binaire603("".join(lbin))

    def binDecode(self, monBinC: Binaire603):
        lbin = []
        dicoHuffman = CompresseurHuffman.codageHuffman(monBinC, True)[0]
        print(CompresseurHuffman.codageHuffman(monBinC, False))
        for bin in monBinC:
            print(bin)

    def demo():
        monCodeur=CompresseurHuffman()
        monBin=Binaire603([6,6,6,6,6,5,5,5,5,6,6,6,7,8,9,8,8])
        monBinC=monCodeur.binCode(monBin)
        monBin==monCodeur.binDecode(monBinC)

if __name__ == "__main__":
    comp = CompresseurHuffman()
    # Exemple utilisé dans Compression Huffman, Théorie des Codes, Dunod
    binaire = Binaire603("aaaaaaaaaadddddddcccccbbbbeef")
    binaire = Binaire603([5,5,5,5,5,5,5,5,6,6,6,7,7,9])
    dico = CompresseurHuffman.dicoFrequences(binaire, True)
    print(dico)
    for item in dico.items():
        print(item)
    lp = [item for item in dico.items()]
    tree = CompresseurHuffman.arbreDepuisListe(lp, True)
    tree.printTree()
    encodeHuffman = CompresseurHuffman.dicoHuffmanDepuisArbre(tree)
    print(encodeHuffman)
    code = CompresseurHuffman.codageHuffman(binaire, True)
    print(code)
    res = comp.binCode(binaire)
    print(res)
    comp.binDecode(res)

from Binaire603 import *

class  CompresseurParRepetition(object):
    def __init__(self) -> None:
        pass

    def __repr__(self) -> str:
        return "CmpresseurParRépetition({})"

    def __str__(self) -> str:
        return f"Classe Compresseur par Répetition"

    """
    >>> CompresseurParRepetition()(Binaire603([1, 2, 3, 4, 5, 6, 7, 7, 7, 4, 7, 7, 1]))
    Bianire603([1, 1, 1, 2, 1, 3, 1, 4, 1, 5, 1, 6, 3, 7, 1, 4, 2, 7, 1, 1])
    """
    def __call__(self, monBin: Binaire603)-> Binaire603:
        #Peut etre utiliser des dictionnaires pour simplifier la tâche en python
        compressed = list()
        size = len(monBin)-1
        for nbin in range(len(monBin)):
            reps, next = 1, nbin+1
            while True:
                if next > size or monBin[next] != monBin[nbin]:
                    break
                reps, next = reps+1, next+1
            if monBin[nbin] != monBin[nbin-1] or nbin == 0:
                compressed += [reps, monBin[nbin]]
        return Binaire603(compressed)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    comp = CompresseurParRepetition()
    texte = "aaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbcccccccccccccddddddddddddddd"
    binaire = Binaire603(texte)
    print(binaire)
    binCompress = comp(binaire)
    print(binCompress)
    print("Entropie du texte compressé: ", binCompress.entropie())
    print("Entropie du texte non compressé: ", binaire.entropie())






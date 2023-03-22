from Binaire603 import *

class algorithmeLuhn(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def validationBin(monBin: Binaire603):
        copy = [b for b in monBin]
        for i in range(len(monBin)-2, 0, -2):
            print(i)
            copy[i] *= 2
            if copy[i] > 9:
                copy[i] %=  9
        return (sum(copy) % 10) == 0

if __name__ == '__main__':
    binaire = Binaire603([9, 7, 2, 4, 8, 7,0, 8, 6])
    print("La valeur est valide!" if algorithmeLuhn.validationBin(binaire) else "La valeur n'est pas valide...")
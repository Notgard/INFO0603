from Binaire603 import *
from ChiffreurParDecalageEtd import *
from ChiffreurAffine import *
from ChiffreurVigenere import *
from ChiffreurFeistel import *

"""
Chiffre1.TXT : Chiffreur par Décalage par 5
Chiffre2.TXT : Chiffreur Affine avec clés a=3 et b=1
Chiffre3.TXT : Chiffreur Vigenère avec clé 'Bonjour'
Chiffre4.TXT : ???
"""

def decryptDecalageOrAffine(docChiffre, maxKeys=10, showGraph=False):
    docChiffreBin = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+".TXT")
    if docChiffre[-1] == "1":
        docDechiffre = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+"Decode.TXT")
    else:
        docDechiffre = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+"D.TXT")
    if showGraph:
        docChiffreBin.afficheHistogrammeDesFrequences(titre="Fréquences des lettres dans " + docChiffre)
    frequenceDeChiffre = Binaire603(docDechiffre).lFrequences()
    keys = dict()
    for a in range(1, maxKeys):
        for b in range(1, maxKeys):
            if sontPremiers(a, 256):
                docDechiffreBin = ChiffreurAffine(a, b).binDecode(docChiffreBin)
            else:
                docDechiffreBin = ChiffreurParDecalage(a).binDecode(docChiffreBin)
            if frequenceDeChiffre == docDechiffreBin.lFrequences():
                keys[docChiffre] = (a, b)
                if showGraph:   
                    if a == 1:
                        docDechiffreBin.afficheHistogrammeDesFrequences(titre="Fréquences des lettres déchiffrés dans " + docChiffre + " en a: " + str(a) + " et b: " + str(b) + "(Décalage)")
                    else:
                        docDechiffreBin.afficheHistogrammeDesFrequences(titre="Fréquences des lettres déchiffrés dans " + docChiffre + " en a: " + str(a) + " et b: " + str(b))
                break
        else:
            continue
        break
    print(keys)

"""
    Problème avec résolution de l'équation afin de retrouver les valeurs a et b pour le chiffrage affine
"""
binChiffre = Binaire603.bin603DepuisFichier("./txt/"+"Chiffre2"+".TXT")

lf = binChiffre.lFrequences()
lbTries=sorted([k for k in range(256)], key=lambda b:lf[b],reverse=True)
lbTriesNonNuls=[b for b in lbTries if lf[b]>0]
chars = [f"{b:02x}" for b in lbTriesNonNuls]
lf.sort()
mx = max(lf) #space
lf.pop()
codeE = max(lf) #e
mx = int(chars[0])
codeE = int(chars[1])
inv = ElementDeZnZ(20-65).inverse()
#print(inv, inv*(61-30), inv*(20*61-65*30))
a =  (mx - codeE) * inv
b = (mx-20)*a
print(a, b)


def indice_de_coincidence(binChiffre:Binaire603):
    lc=[0]*256
    for oc in binChiffre: #every letter (0..255)
        lc[oc]+=1 #lc[61] (61=a) = n
    nq = sum(lc)
    offset = sum(n * (n-1) for n in lc)
    return offset/(nq * (nq-1))


def decryptVigenere(binChiffre:Binaire603):
    index = indice_de_coincidence(binChiffre)
    print("Indice de coincidence de l'entièreté du fichier:", index)
    for keyl in range(1, 25):
        columns = [binChiffre[i::keyl] for i in range(keyl)]
        column_ics = [indice_de_coincidence(column) for column in columns]
        if all(0.06 < index - column_ic < 0.05 for column_ic in column_ics):
            print("possible key length: ", keyl)


def liste_indices(binChiffre:Binaire603, n:int):
    res=[0]
    for i in range(1, n + 1):
        res.append(sum(indice_de_coincidence(binChiffre[k::i]) for k in range(i)))
        res[-1] /= i
    return res


def key_lengths(binChiffre:Binaire603, limit=0.068, nmax=12):
    p = [(lcle, i) for lcle, i in enumerate(liste_indices(binChiffre, nmax)) if i > limit]
    return p


def show_indices_graph(chiffreBin:Binaire603, max_key):
    list_indices = liste_indices(chiffreBin, max_key)
    print(list_indices, len(list_indices))
    plt.plot(list_indices, linestyle='solid', marker='o', color='b')
    plt.xticks(range(max_key+1))
    plt.xlabel("Taille de clés possibles")
    plt.ylabel("Indice de Coïncidence")
    plt.ylim(bottom=0.02)
    plt.title("Fréquences des tailles de clés par indice de coïncidence")
    plt.show()


def cesar(monBin:Binaire603, decalage:int)->Binaire603:
    """
    >>> cesar(Binaire603("ae"), 1)
    Binaire603("bf")
    """
    return Binaire603([(bin + decalage) % 256 for bin in monBin])

#trash this one later ^^^^

def test(docChiffreBin:Binaire603, keyLength:int):
    lenText = len(docChiffreBin)
    firstSlice = docChiffreBin[0:lenText:keyLength]
    decalages = [0]
    for k in range(1, keyLength):
        icMax = 0
        decalage = -1
        kSlice = docChiffreBin[k:lenText:keyLength]
        for d in range(0, 255):
            cesarList = [bin for bin in cesar(kSlice, d)]
            ic = indice_de_coincidence(Binaire603(firstSlice + cesarList))
            if ic > icMax:
                icMax = ic
                decalage = d
        decalages.append(decalage)
    return decalages

def decryptFeistel(docChiffre, key, rounds):
    frequenceDeChiffre = Binaire603.bin603DepuisFichier(os.listdir()[1]+"/txt/Chiffre4D.TXT").lFrequences()
    binaireCode = Binaire603.bin603DepuisFichier(os.listdir()[1]+"/txt/"+docChiffre+".TXT")
    for k in range(key):
        for r in range(rounds):
            chif = ChiffreurFeistel(r, k)
            binaireDecode = chif.binDecode(binaireCode)
            if frequenceDeChiffre == binaireDecode.lFrequences():
                print({"Chiffre4": (k, r)})
                break
        else:
            continue
        break

docChiffres = ["Chiffre1", "Chiffre2", "Chiffre3", "Chiffre4"]

for docChiffre in docChiffres:
    if docChiffre[-1] == "3":
        docChiffreBin = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+".TXT")
        #print(indice_de_coincidence(docChiffreBin))
        #print(key_lengths(docChiffreBin, nmax=30))
        show_indices_graph(docChiffreBin, 20)
        # D'après le graphe, les tailles de clées les plus plosibles sont 7 et 14
        possible_key_length = 7
        #print(test(docChiffreBin, possible_key_length))
        dechiffre = ChiffreurVigenere("Bonjour").binDecode(docChiffreBin)
        dechiffre.afficheHistogrammeDesFrequences(titre="Fréquences des lettres avec clé: 'Bonjour' dans " + docChiffre)
    elif docChiffre[-1] == "4":
        print("Chiffreur par Feistel", docChiffre)
        decryptFeistel(docChiffre, 10, 10)
    else:
        print("Chiffreur par Decalage ou Affine", docChiffre)
        decryptDecalageOrAffine(docChiffre, 10, True)
    if docChiffre[-1] == "1":
        docDechiffreBin = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+"Decode.TXT")
    else:
        docDechiffreBin = Binaire603.bin603DepuisFichier("./txt/"+docChiffre+"D.TXT")
    docDechiffreBin.afficheHistogrammeDesFrequences(titre="Fréquences des lettres déchiffrés dans " + docChiffre)

#docDechiffre = ["Chiffre1Decode", "Chiffre2D", "Chiffre3D", "Chiffre4D"]
#for nf in docDechiffre:
#    docDechiffreBin = Binaire603.bin603DepuisFichier(os.listdir()[0]+"/txt/"+nf+".TXT")
#    docDechiffreBin.afficheHistogrammeDesFrequences(titre="Fréquences des lettres dans " + nf)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
from random import *
from math import sqrt,log
from sympy import isprime

def secondDiviseur(a):
    """Renvoie le premier diviseur de a supérieur à 1

    >>> secondDiviseur(15845465)
    5
    >>> secondDiviseur(1)==1 and secondDiviseur(2)==2 and secondDiviseur(6)==2
    True
    >>> secondDiviseur(153)==3 and secondDiviseur(157)==157 and secondDiviseur(13)==13
    True
    """
    if a==1: return 1
    if a%2==0: return 2
    ra=int(sqrt(a))+1
    d=3
    while d<=ra and a%d!=0:
        d+=2
    if d>ra:
        return a
    else :
        return d

def eDiviseurs(a):
    """renvoie l'ensemble des diviseurs positifs de A

    >>> eDiviseurs(60)=={1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 60, 30}
    True
    >>> eDiviseurs(1)==set({1}) and eDiviseurs(13)==set({1, 13})
    True
    """
    ed=set({1,a})
    d=secondDiviseur(a)
    if d!=a:
        ed.add(d)
        ed.add(a//d)
        for d2 in range(2,a//d):
            if a%d2==0:
                ed.add(d2)
    return ed


def lPGCD(a,b):
    """ Renvoie le couple : (liste des dividendes,le PGCD)

    >>> lPGCD(360,304)
    ([1, 5, 2], 8)
    >>> lPGCD(517,513)
    ([1, 128], 1)
    >>> lPGCD(513,517)
    ([0, 1, 128], 1)
    """
    lq=[]
    on_n_a_pas_fini=True
    while (on_n_a_pas_fini):
        q,r = a//b , a%b
        if r==0:
            on_n_a_pas_fini=False
        else:
            lq+=[q]
            a,b=b,r
    return lq,b
def PGCD(a,b):
    """
    >>> PGCD(360,304)
    8
    >>> PGCD(517,513)
    1
    >>> PGCD(513,517)
    1
    """
    l,d=lPGCD(a,b)
    return d
def sontPremiersEntreEux(a,b):
    """
    >>> sontPremiersEntreEux(10,21) and sontPremiersEntreEux(100,37) and not(sontPremiersEntreEux(4,2))
    True
    """
    return PGCD(a,b)==1
def solDiophant(a,b,c):
    """
    Renvoie x et y de Z tels que a.x+b.y=c
    sous la forme x=x0+k.a' et y=y0+k.b'

    >>> solDiophant(2,5,16) #x0,y0,a',b' et les sols sont x=-32+5.k et y=16-2.k
    (-32, 16, 5, -2)
    >>> x0,y0,cx,cy=solDiophant(13,4,12)
    >>> 13*(x0+1234*cx)+4*(y0+1234*cy)==12
    True
    """
    d=PGCD(PGCD(a,b),c)
    aa,bb,cc=a//d,b//d,c//d
    x0,y0,dd=bezout(aa,bb)# donc a(x-x0)=-b(y-y0)
    assert cc%dd==0," Pas de solutions à l'équation"
    ccc=cc//dd
    return  x0*ccc,y0*ccc,bb,-aa

def bezout(a,b):
    """Renvoie (u,v,d) tel que a.u+b.v=d avec d=PGCD(a,b)
    >>> bezout(360,304)
    (11, -13, 8)
    >>> bezout(1254,493)
    (-149, 379, 1)
    >>> bezout(513,517)
    (129, -128, 1)
    """
    lq,d=lPGCD(a,b)
    u,v=1,-lq[-1]
    for k in range(len(lq)-1):
        u,v=v,u-v*lq[-k-2]
    return u,v,d


def estPremier1(n):
    """
    >>> estPremier1(13) and estPremier1(2) and not(estPremier1(6))and not(estPremier1(35))
    True
    """
    if n==1 : return Falsesympy
    if n==2 or n==3: return True
    if n%2==0: return False
    if n>1E6:return isprime(n) #Pour éviter les ralentissements
    d=3
    rn=int(sqrt(n)+1)
    while n%d!=0 and d<rn:
        d+=2
    return n%d!=0
def estPremier(n):
    """
    >>> estPremier(13) and estPremier(2) and not(estPremier(6))and not(estPremier(35))
    True
    """
    if n==1 : return False
    if n==2 or n==3: return True
    if n%2==0: return False
    if n<640000:
        d=3
        rn=int(sqrt(n)+1)
        while n%d!=0 and d<rn:
            d+=2
        return n%d!=0
    else:
        return isprime(n)


def nbPremierSuivant(n):
    """Renvoie le plus petit nombre premier strictement supérieur à n
    >>> nbPremierSuivant(1)==2 and nbPremierSuivant(3)==5 and nbPremierSuivant(20)==23
    True
    """
    p=n+1
    while not(estPremier(p)):
        p+=1
    return p
def nbPremierAleaParNbBits(nbBits=32):
    """
    >>> estPremier(nbPremierAleaParNbBits(10)) and nbPremierAleaParNbBits(10)>1024 and nbPremierAleaParNbBits(10)<2048
    True
    """
    n=2**nbBits+randint(2**(nbBits-1),2**nbBits)
    return nbPremierSuivant(n)
def nbPremierEtMoitieSuivant(n):
    """renvoie le couple q,p de nombres premiers avec q=(p-1)/2
    >>> nbPremierEtMoitieSuivant(100)
    (107, 53)
    """
    p=nbPremierSuivant(n)
    while not(estPremier((p-1)//2)):
        p=nbPremierSuivant(p+2)
    return p,(p-1)//2
def grandEntier(n):
    """Renvoie le produit de deux nombres premiers choisis au hasard dans [n..2N]"""
    return nbPremierSuivant(randint(n,2*n))*nbPremierSuivant(randint(n,2*n))

def estPremierMillerRabin(n):
    """
    https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test
    """
    if n < 2047:lbases=[ 2]
    elif n < 1373653:lbases=[ 2,  3]
    elif n < 9080191:lbases=[ 31,   73]
    elif n < 25326001:lbases=[ 2, 3,   5]
    elif n < 3215031751:lbases=[ 2, 3, 5,   7]
    elif n < 4759123141:lbases=[ 2, 7,   61]
    elif n < 1122004669633:lbases=[ 2, 13, 23,   1662803]
    elif n < 2152302898747:lbases=[ 2, 3, 5, 7,   11]
    elif n < 3474749660383:lbases=[ 2, 3, 5, 7, 11,   13]
    elif n < 341550071728321:lbases=[ 2, 3, 5, 7, 11, 13,   17]
    elif n < 3825123056546413051:lbases=[ 2, 3, 5, 7, 11, 13, 17, 19,   23]

    elif n < 18446744073709551616:lbases=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,   37]
    elif n < 318665857834031151167461: lbases=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31,   37]
    elif n < 3317044064679887385961981:lbases=[ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,   41]#25 chiffres :83bits
    else :return isprime(n)
    return estOkTestMillerRabin(n,lbases)



def estOkTestMillerRabin(n,lbases=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127]):
    res=True
    for a in lbases:
        if not(estPremierOuPseudoPremierDansLaBase(n,a)):
            return False
    return True

def testEstPremierMillerRabin(nbBits=50,nbtests=1000000):
    nmax=2**nbBits
    for k in range(nbtests):
        n=randint(5,nmax )
        if isprime(n)!=estPremierMillerRabin(n):
            print(f"Erreur avec {n}")
        if k%100000==1 : print(f"{k} sur {nbtests} tests de estPremierMillerRabin réalisés sur {nbBits=}")



def premierContreExempleTestMillerRabin(maxBase=5,depart=1999999,verbose=True):
    n=depart
    lbases=[k for k in range(2,maxBase+1) if estPremier(k)]
    while estOkTestMillerRabin(n,lbases)==estPremier(n):
        n+=1
        if n%1000000==0 and verbose: print(f"pas de contre exemple trouvé à Miller Rabine avec {lbases} en dessous de {n}")
    return n
def strExp(p):
    """renvoie l'exposant tout beau
    >>> strExp(9)
    '⁹'
    >>> strExp(-19)
    '-¹⁹'
    >>> strExp(0)
    '⁰'
    >>> strExp(1)
    ''
    """
    SE="⁰¹²³⁴⁵⁶⁷⁸⁹" #Cela serait malin de créer plutôt un dictionnaire
    SP,SM="⁺","⁻"
    pt=p
    if pt==0:return "⁰"
    if pt==1:return ""
    if pt<0:
        return "-"+strExp(-p)
    else:
        ch=""
    while pt>0:
##        p10p=int(log(pt,10))
##        v10=10**p10p
##        ch+=SE[pt//v10]
##        pt=pt%v10
          ch,pt =SE[pt%10]+ch ,pt//10
    return ch

def chFacteursPremiers(n):
    """renvoie une chaine de caractère donnant la décomposition en facteurs premiers de n
    >>> chFacteursPremiers(120)
    '2³×3×5'
    >>> chFacteursPremiers(3600)
    '2⁴×3²×5²'
    >>> chFacteursPremiers(1)+chFacteursPremiers(2)
    '12'
    >>> chFacteursPremiers(21)
    '3×7'
    """
    l=lFacteursPremiers(n)
    ch=""
    for d,p in l:
        ch+=f"{d}{strExp(p)}×"
    return ch[:-1]

def lFacteursPremiers(n):
    """renvoie une liste donnant la décomposition en facteurs premiers de n
    >>> lFacteursPremiers(18)
    [(2, 1), (3, 2)]
    >>> lFacteursPremiers(13)
    [(13, 1)]
    """
    assert isinstance(n,int) and n>0
    if n==1 : return [(1,1)]

    n1=n
    l,d=[],0

    while n1>1:
        dp=secondDiviseur(n1)
        if dp!=d:
            l+=[(dp,1)]
            d=dp
        else:
            l=l[:-1]+[( dp , l[-1][1] +1) ] #On incrémente la puissance
        n1=n1//dp
    return l
def indicatriceEuler(n):
    """
    >>> indicatriceEuler(5)==4 and indicatriceEuler(15)==8 and indicatriceEuler(125)==100
    True
    """
    lfp=lFacteursPremiers(n)
    res=1
    for p,k in lfp:
        res*=(p-1)*p**(k-1)
    return res
def lDecompoPGCDetPPCM(a,b):
    """Renvoie ce couple de décomposition en facteurs premiers
    en utilisant la décomposition en facteurs premier de a et b
    >> lDecompoPGCDetPPCM(60,700)
    [(2, 2),(5, 1)], [(2, 2), (5, 2), (7, 1)]
    """
    pass
#Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/
class ElementDeZnZ(object):
    "Elément de Z/nZ"
    def __init__(self,_a,_n=2):
        """
        >>> ElementDeZnZ(-1,10)
        ElementDeZnZ(9,10)
        >>> ElementDeZnZ(ElementDeZnZ(9,10))
        ElementDeZnZ(9,10)
        """
        if isinstance(_a,ElementDeZnZ):
            self.a,self.n= _a.a, _a.n
        else:
            self.a,self.n =_a%_n,_n
    @property
    def rep(self):
            return self.a
    @rep.setter
    def rep(self, rep):
        self.a = rep


    def __str__(self):
        """
        >>> print(ElementDeZnZ(-1,5))
        4(5)
        """
        return f"{self.a}({self.n})"
    def __repr__(self):
        """
        >>> ElementDeZnZ(-1,5)
        ElementDeZnZ(4,5)
        """
        return f"ElementDeZnZ({self.a},{self.n})"
    def __add__(self,other):
        """
        >>> ElementDeZnZ(2,10)+ElementDeZnZ(3,10)
        ElementDeZnZ(5,10)
        >>> ElementDeZnZ(2,10)+3
        ElementDeZnZ(5,10)
        """
        if isinstance(other,ElementDeZnZ):
            return  ElementDeZnZ(self.a+other.a,self.n) #https://developpement-informatique.com/article/222/les-operateurs-en-python
        else:
            return ElementDeZnZ(self.a+other,self.n)
    def __radd__(self,other):
        """
        >>> 2+ElementDeZnZ(3,10)
        ElementDeZnZ(5,10)
        """
        return self+other
    def __mul__(self,other):
        """
        >>> ElementDeZnZ(2,10)*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        >>> ElementDeZnZ(2,10)*3
        ElementDeZnZ(6,10)
        """
        if isinstance(other,ElementDeZnZ):
            return  ElementDeZnZ((self.a*other.a),self.n) #https://developpement-informatique.com/article/222/les-operateurs-en-python
        else:
            return ElementDeZnZ(self.a*other,self.n)
    def __rmul__(self,other):
        """
        >>> 2*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        """
        return self*other
    def __floordiv__(self,other):
        """
        Opération inverse de la multiplication : ElementDeZnZ(4,10)//ElementDeZnZ(5,10) doit renvoyer une erreur
        >>> ElementDeZnZ(9,10)//ElementDeZnZ(3,10)
        ElementDeZnZ(3,10)
        >>> ElementDeZnZ(1,10)//ElementDeZnZ(3,10)
        ElementDeZnZ(7,10)

        """
        if isinstance(other,ElementDeZnZ):
            b=other.a
        else:
            b=other
        u,v,d=bezout(b,self.n)
        ch=f"Il n'existe pas de dividende de {b} par {self}"
        assert self.a %d ==0,ch
        return ElementDeZnZ(u*(self.a//d),self.n)
    def __eq__(self,other):
        """
        >>> ElementDeZnZ(9,10)==ElementDeZnZ(-1,10)
        True
        >>> ElementDeZnZ(9,10)==ElementDeZnZ(1,10)
        False
        >>> ElementDeZnZ(9,10)==9
        True
        """
        if isinstance(other,ElementDeZnZ):
            return (self.a-other.a)%self.n==0
        else:
            return (self.a-other)%self.n==0
    def __neg__(self):
        """
        >>> -ElementDeZnZ(9,10)==ElementDeZnZ(1,10)
        True
        >>> -ElementDeZnZ(9,10)==2
        False
        >>> -ElementDeZnZ(9,10)==1
        True
        """
        return ElementDeZnZ(self.n-self.a,self.n)
    def __sub__(self,other):
        """
        >>> a4=ElementDeZnZ(-1,5);a1=ElementDeZnZ(1,5);a1+a4==0
        True
        >>> (-a4+a4==0) and (a4//4==1) and (4*a1+(-a1*4)==0)
        True
        """
        return self+(-other)
    def __rsub__(self,other):
        """
        >>> 4-ElementDeZnZ(3,5)
        ElementDeZnZ(1,5)
        """
        return (-self)+other

    def __pow__(self,q):
        """
        >>> a=ElementDeZnZ(3,10); a**2==-1 and a**1==3 and a**0==1 and a**3==7 and a**4==1
        True
        >>> (ElementDeZnZ(-3,47)**(-1))*ElementDeZnZ(-3,47)
        ElementDeZnZ(1,47)
        """
        if q<0:
            assert self.estInversible(),f" {self} n'est pas inversible et donc ne peut avoir de puissance négative"
            return self.inverse()**(-q)
        elif q==1: return self
        elif  q==0: return ElementDeZnZ(1,self.n)
        else:
            qq,rr = q//2,q%2 #q=2*qq+rr
            return ((self*self)**qq)*self**rr
    def toInt(self):
        """
        >>> ElementDeZnZ(3,10).toInt()
        3
        """
        return self.a
    def ordre(self):
        """
        Voir http://www.repcrypta.com/telechargements/fichecrypto_107.pdf
        >>> (ElementDeZnZ(2,7)).ordre()
        3
        >>> (ElementDeZnZ(-2,7)).ordre()
        6
        """
        assert self.estInversible()
        ld=sorted(eDiviseurs(self.n-1))
        for d in ld[1:-1]:
            if self**(d)==1:
                return d
        return self.n-1
    def elementPrimitif(self):
            """Renvoie le premier élément primitif (d'ordre n-1) de Z/nZ suivant self
            >>> ElementDeZnZ(2,17).elementPrimitif()
            ElementDeZnZ(3,17)
            >>> ElementDeZnZ(2,17).elementPrimitif()
            ElementDeZnZ(3,17)
            >>> ElementDeZnZ(15,17).elementPrimitif()
            ElementDeZnZ(3,17)
            >>> ElementDeZnZ(1,65537).elementPrimitif()
            ElementDeZnZ(3,65537)
            """
            if self==ElementDeZnZ(1,65537) : return ElementDeZnZ(3,65537)
            res=self+1
            while not(res.estInversible()) or res.ordre()!=self.n-1:
                res=res+1
            return res
    def estUnCarre(self):
        """
        cours 3 http://math.univ-lyon1.fr/~roblot/ens.html
        Pour p premier, Le groupe multiplicatif Fp est cyclique d’ordre p − 1 et donc a
        exactement (p − 1)/2 carres (p impair) : si g est un générateur alors g**i
        est un carrée si et seulement si i est pair.
        Pour tout a ∈ Fp×, on a a**(p−1) = 1 et donc a est un carré si et seulement si
        a**(p−1)/2 = 1 (sinon c’est −1).
        """
        if self==0 or self==1: return True
        assert estPremier(self.n)
        return self.LegendreJacobi()==1
    def LegendreJacobi(self):
        """
        cours 3 http://math.univ-lyon1.fr/~roblot/ens.html
        >>> ElementDeZnZ(9,17).LegendreJacobi()
        1
        >>> ElementDeZnZ(3,17).LegendreJacobi()
        -1
        """
        v=self**((self.n-1)//2)
        if v==1: return 1
        elif v==-1:return -1
        else: return 0

    def racineCarree(self):
        """Renvoie un r tell que r²==self avec r.a<=self.n/2
        >>> ElementDeZnZ(65535,65537).racineCarree()
        ElementDeZnZ(4112,65537)
        >>> ElementDeZnZ(9,17).racineCarree()
        ElementDeZnZ(3,17)
        >>> ElementDeZnZ(13,17).racineCarree()
        ElementDeZnZ(8,17)
        >>> ElementDeZnZ(0,17).racineCarree()
        ElementDeZnZ(0,17)
        >>> ElementDeZnZ(5,19).racineCarree()
        ElementDeZnZ(9,19)
        >>> ElementDeZnZ(10,13).racineCarree()
        ElementDeZnZ(6,13)
        """
        assert self.estUnCarre()
        if self==0 or self==1: return ElementDeZnZ(self)
        p=self.n
        if p%4==3: r= self**((p+1)//4)
        elif p%8== 5:
            s=self**((p-1)//4)
            if s==1:
                r= self**((p+3)//8)
            else:
                r=  (2*self)*(4*self)**((p-5)//8)#car 2**((p−1)/2= ≡ −1 (mod p)
        else:
            a,g=ElementDeZnZ(self),self.elementPrimitif()
            e1,e2=(p-1)//2,0  #a**e1.g**e2=1
            while e1%2==0:
                if a**(e1//2)*g**(e2//2)==1:
                    e1,e2=e1//2,e2//2
                else:
                    e1,e2=e1//2,(e2+p-1)//2
            #e1=2e1p+1 est impair et e2=2e2p pair donc
            e1p,e2p=(e1-1)//2,e2//2
            r= a**(e1p+1)*g**(e2p)
        if r.a>p//2: r=-r
        return r

    def estPrimitif(self):
        return self.ordre()==self.n-1
    def estInversible(self):
        """
        >>> ElementDeZnZ(3,5).estInversible()
        True
        >>> ElementDeZnZ(10,12).estInversible()
        False
        """
        return  PGCD(self.a,self.n)==1
    def inverse(self):
        """
        >>> ElementDeZnZ(3,5).inverse()==2
        True

        ElementDeZnZ(2,10).inverse() doit renvoyer une erreur
        """
        u,v,d=bezout(self.a,self.n)
        assert d==1,f"{self} n'est pas inversible !"
        #a et n premiers entre eux
        return ElementDeZnZ(u,self.n)     #a.u=1(n)
    def logDiscret(self,b):
        """Renvoie x tel que self.a**x==b(self.n)
        n doit être premier pour garantir l'existence
        >>> ElementDeZnZ(2,13).logDiscret(8)
        3
        >>> ElementDeZnZ(2,13).logDiscret(3)
        4
        """
        apk,k=ElementDeZnZ(1,self.n),0
        while apk!=b:
            apk*=self
            k+=1
        return k
    def valThChinois(self,other):
        """
        Renvoie c(pq) avec a(p) et b(q) tel que x≡a(p) et x≡b(q) <=>x≡c(p.q)$
        >>> ElementDeZnZ(2,7).valThChinois(ElementDeZnZ(3,10))
        ElementDeZnZ(23,70)
        """
        assert PGCD(self.n,other.n)==1,"p et q ne sont pas premiers entre eux"
        u,v,d=bezout(self.n,other.n)
        return ElementDeZnZ( other.a*self.n*u + self.a*other.n*v, self.n*other.n)
    def demoDiv(self):
        for k in range(1,self.n):
            a=ElementDeZnZ(k,self.n)
            try :
                ch=f"{a.a}×{a.inverse().a}=1 ({a.n})"
            except :
                ch=f"{a} n'a pas d'inverse"
            try :
                q=(self//a)
                ch+=f" et {a.a}×{q.a}={self} "
            except:
                ch+=f" et il n'y a pas de solution à {a.a}×X={self} "
            print(ch)

    def demo1():
        for k in range(10,12):
            p1,p2,p3 = nbPremierSuivant(4**k),nbPremierSuivant(5**k),nbPremierSuivant(6**k)
            a=ElementDeZnZ(p1,p3)
            print(f"{k:3} : {a.a}×{a.inverse().a}=1 ({a.n})")
            print(f"           et {a.a}{strExp(p2)}={a**p2}")
#ElementDeZnZ(1,17).elementPrimitif()
#ElementDeZnZ(2,13).logDiscret(8)
def demoVitesse():
        print("Démo Vitesse")
        print("Factorisation :")
        for p in range(23,26):
                n=grandEntier(2**p)
                print(f"{p}: {n}=={chFacteursPremiers(n)}")

        print("Logarithme discret :")
        for p in range(20,24):
            n=nbPremierSuivant(2**p)
            b=ElementDeZnZ(10**int(p*3/10),n)
            print(f"{p}: 2{strExp(ElementDeZnZ(2,n).logDiscret(b))}=={b}")

def estPremierOuPseudoPremierDansLaBase(n,a):
    if n%2==0 : return n==2 #cas où n est pair
    t,s=(n-1),0  #n-1=t * 2**s
    while t%2==0:
        t,s=t//2,s+1

    p,ap=t,ElementDeZnZ(a,n)**t
    if ap-1==0 or ap+1==0: return True
    while s>1:
        ap=ap*ap
        s=s-1
        if ap+1==0: return True
    return False

def estPremierOuPseudoPremierDansLesBases(n,la=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127]):
    res=True
    for x in la:
        if not(estPremierOuPseudoPremierDansLaBase(n,x)):
            return False
    return True

def lbasesDeTestsDePrimalite(nbits=32,verbose=False):
    """Renvoie la liste des bases à testés selon la valeur
    du nombre dont on veut tester la primalité.
    On voit ainsi que pour tester la primalité des nombres inférieurs à 2047 il suffit de tester avec la base 2
    pour tester ceux entre 2047 et 1373653-1 il suffit de tester les bases 2 et 3.
    lbasesDeTestsDePrimalite(21) renvoie [(2047, [2]), (1373653, [2, 3])]
    Donc il faut teste les bases 2 3 et 5 pour la primalité sur [1373653 et 2**21]
    >>> lbasesDeTestsDePrimalite(13)
    [(2047, [2, 3]), (8192, [2, 3])]
    """
    nFinal=2**nbits
    lres=[]
    n=3
    la=[2]
    while estPremierOuPseudoPremierDansLesBases(k,lk)!=isprime(k):
        n+=1
    lres.apend=[(n,la.copy())]
    la.append(nbPremierSuivant(la[-1]))
    while k<nFinal:
        onATrouve=False
        while estPremierOuPseudoPremierDansLesBases(k,lk)!=isprime(k):
            lk+=[nbPremierSuivant(lk[-1])]
            onATrouve=True
        if onATrouve:
            lb+=[(k,lk.copy())]
            if verbose : print((k,lk))
        k+=2
    return lb+[(nFinal,lk.copy())]
#lbasesDeTestsDePrimalite(32)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    testEstPremierMillerRabin()
    #demoVitesse()
    #ElementDeZnZ.demo1()
    #ElementDeZnZ(8,60).demoDiv()


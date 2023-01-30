from copy import copy
from random import randint
from math import sqrt, log
from sympy import isprime

global primeNumbers
primeNumbers = [      
    5,      7,      11,     13,     17,    19,     23,     29, 
    31,     37,     41,     43,     47,     53,     59,    61,     67,     71, 
    73,     79,     83,     89,     97,     101,    103,   107,    109,    113, 
    127,    131,    137,    139,    149,    151,    157,   163,    167,    173, 
    179,    181,    191,    193,    197,    199,    211,   223,    227,    229, 
    233,    239,    241,    251,    257,    263,    269,   271,    277,    281, 
    283,    293,    307,    311,    313,    317,    331,   337,    347,    349, 
    353,    359,    367,    373,    379,    383,    389,   397,    401,    409, 
    419,    421,    431,    433,    439,    443,    449,   457,    461,    463, 
    467,    479,    487,    491,    499,    503,    509,   521,    523,    541, 
    547,    557,    563,    569,    571,    577,    587,   593,    599,    601, 
    607,    613,    617,    619,    631,    641,    643,   647,    653,    659, 
    661,    673,    677,    683,    691,    701,    709,   719,    727,    733, 
    739,    743,    751,    757,    761,    769,    773,   787,    797,    809, 
    811,    821,    823,    827,    829,    839,    853,   857,    859,    863, 
    877,    881,    883,    887,    907,    911,    919,   929,    937,    941, 
    947,    953,    967,    971,    977,    983,    991,   997,   1009,   1013, 
    1019,   1021,   1031,   1033,   1039,   1049,   1051,  1061,   1063,   1069, 
    1087,   1091,   1093,   1097,   1103,   1109,   1117,  1123,   1129,   1151, 
    1153,   1163,   1171,   1181,   1187,   1193,   1201,  1213,   1217,   1223, 
    1229,   1231,   1237,   1249,   1259,   1277,   1279,  1283,   1289,   1291, 
    1297,   1301,   1303,   1307,   1319,   1321,   1327,  1361,   1367,   1373, 
    1381,   1399,   1409,   1423,   1427,   1429,   1433,  1439,   1447,   1451, 
    1453,   1459,   1471,   1481,   1483,   1487,   1489,  1493,   1499,   1511, 
    1523,   1531,   1543,   1549,   1553,   1559,   1567,  1571,   1579,   1583, 
    1597,   1601,   1607,   1609,   1613,   1619,   1621,  1627,   1637,   1657, 
    1663,   1667,   1669,   1693,   1697,   1699,   1709,  1721,   1723,   1733, 
    1741,   1747,   1753,   1759,   1777,   1783,   1787,  1789,   1801,   1811, 
    1823,   1831,   1847,   1861,   1867,   1871,   1873,  1877,   1879,   1889, 
    1901,   1907,   1913,   1931,   1933,   1949,   1951,  1973,   1979,   1987, 
    1993,   1997,   1999,   2003,   2011,   2017,   2027,  2029,   2039,   2053, 
    2063,   2069,   2081,   2083,   2087,   2089,   2099,  2111,   2113,   2129, 
    2131,   2137,   2141,   2143,   2153,   2161,   2179,  2203,   2207,   2213, 
    2221,   2237,   2239,   2243,   2251,   2267,   2269,  2273,   2281,   2287, 
    2293,   2297,   2309,   2311,   2333,   2339,   2341,  2347,   2351,   2357, 
    2371,   2377,   2381,   2383,   2389,   2393,   2399,  2411,   2417,   2423, 
    2437,   2441,   2447,   2459,   2467,   2473,   2477,  2503,   2521,   2531, 
    2539,   2543,   2549,   2551,   2557,   2579,   2591,  2593,   2609,   2617, 
    2621,   2633,   2647,   2657,   2659,   2663,   2671,  2677,   2683,   2687, 
    2689,   2693,   2699,   2707,   2711,   2713,   2719,  2729,   2731,   2741, 
    2749,   2753,   2767,   2777,   2789,   2791,   2797,  2801,   2803,   2819, 
    2833,   2837,   2843,   2851,   2857,   2861,   2879,  2887,   2897,   2903, 
    2909,   2917,   2927,   2939,   2953,   2957,   2963,  2969,   2971,   2999, 
    3001,   3011,   3019,   3023,   3037,   3041,   3049,  3061,   3067,   3079, 
    3083,   3089,   3109,   3119,   3121,   3137,   3163,  3167,   3169,   3181, 
    3187,   3191,   3203,   3209,   3217,   3221,   3229,  3251,   3253,   3257, 
    3259,   3271,   3299,   3301,   3307,   3313,   3319,  3323,   3329,   3331, 
    3343,   3347,   3359,   3361,   3371,   3373,   3389,  3391,   3407,   3413, 
    3433,   3449,   3457,   3461,   3463,   3467,   3469,  3491,   3499,   3511, 
    3517,   3527,   3529,   3533,   3539,   3541,   3547,  3557,   3559,   3571, 
    3581,   3583,   3593,   3607,   3613,   3617,   3623,  3631,   3637,   3643, 
    3659,   3671,   3673,   3677,   3691,   3697,   3701,  3709,   3719,   3727, 
    3733,   3739,   3761,   3767,   3769,   3779,   3793,  3797,   3803,   3821, 
    3823,   3833,   3847,   3851,   3853,   3863,   3877,  3881,   3889,   3907, 
    3911,   3917,   3919,   3923,   3929,   3931,   3943,  3947,   3967,   3989, 
    4001,   4003,   4007,   4013,   4019,   4021,   4027,  4049,   4051,   4057, 
    4073,   4079,   4091,   4093,   4099,   4111,   4127,  4129,   4133,   4139, 
    4153,   4157,   4159,   4177,   4201,   4211,   4217,  4219,   4229,   4231, 
    4241,   4243,   4253,   4259,   4261,   4271,   4273,  4283,   4289,   4297, 
    4327,   4337,   4339,   4349,   4357,   4363,   4373,  4391,   4397,   4409, 
    4421,   4423,   4441,   4447,   4451,   4457,   4463,  4481,   4483,   4493, 
    4507,   4513,   4517,   4519,   4523,   4547,   4549,  4561,   4567,   4583, 
    4591,   4597,   4603,   4621,   4637,   4639,   4643,  4649,   4651,   4657, 
    4663,   4673,   4679,   4691,   4703,   4721,   4723,  4729,   4733,   4751, 
    4759,   4783,   4787,   4789,   4793,   4799,   4801,  4813,   4817,   4831, 
    4861,   4871,   4877,   4889,   4903,   4909,   4919,  4931,   4933,   4937, 
    4943,   4951,   4957,   4967,   4969,   4973,   4987,  4993,   4999,   5003, 
    5009,   5011,   5021,   5023,   5039,   5051,   5059,  5077,   5081,   5087, 
    5099,   5101,   5107,   5113,   5119,   5147,   5153,  5167,   5171,   5179, 
    5189,   5197,   5209,   5227,   5231,   5233,   5237,  5261,   5273,   5279, 
    5281,   5297,   5303,   5309,   5323,   5333,   5347,  5351,   5381,   5387, 
    5393,   5399,   5407,   5413,   5417,   5419,   5431,  5437,   5441,   5443, 
    5449,   5471,   5477,   5479,   5483,   5501,   5503,  5507,   5519,   5521, 
    5527,   5531,   5557,   5563,   5569,   5573,   5581,  5591,   5623,   5639, 
    5641,   5647,   5651,   5653,   5657,   5659,   5669,  5683,   5689,   5693, 
    5701,   5711,   5717,   5737,   5741,   5743,   5749,  5779,   5783,   5791, 
    5801,   5807,   5813,   5821,   5827,   5839,   5843,  5849,   5851,   5857, 
    5861,   5867,   5869,   5879,   5881,   5897,   5903,  5923,   5927,   5939, 
    5953,   5981,   5987,   6007,   6011,   6029,   6037,  6043,   6047,   6053, 
    6067,   6073,   6079,   6089,   6091,   6101,   6113,  6121,   6131,   6133, 
    6143,   6151,   6163,   6173,   6197,   6199,   6203,  6211,   6217,   6221, 
    6229,   6247,   6257,   6263,   6269,   6271,   6277,  6287,   6299,   6301, 
    6311,   6317,   6323,   6329,   6337,   6343,   6353,  6359,   6361,   6367, 
    6373,   6379,   6389,   6397,   6421,   6427,   6449,  6451,   6469,   6473, 
    6481,   6491,   6521,   6529,   6547,   6551,   6553,  6563,   6569,   6571, 
    6577,   6581,   6599,   6607,   6619,   6637,   6653,  6659,   6661,   6673, 
    6679,   6689,   6691,   6701,   6703,   6709,   6719,  6733,   6737,   6761, 
    6763,   6779,   6781,   6791,   6793,   6803,   6823,  6827,   6829,   6833, 
    6841,   6857,   6863,   6869,   6871,   6883,   6899,  6907,   6911,   6917, 
    6947,   6949,   6959,   6961,   6967,   6971,   6977,  6983,   6991,   6997, 
    7001,   7013,   7019,   7027,   7039,   7043,   7057,  7069,   7079,   7103, 
    7109,   7121,   7127,   7129,   7151,   7159,   7177,  7187,   7193,   7207,
    7211,   7213,   7219,   7229,   7237,   7243,   7247,  7253,   7283,   7297, 
    7307,   7309,   7321,   7331,   7333,   7349,   7351,  7369,   7393,   7411, 
    7417,   7433,   7451,   7457,   7459,   7477,   7481,  7487,   7489,   7499, 
    7507,   7517,   7523,   7529,   7537,   7541,   7547,  7549,   7559,   7561, 
    7573,   7577,   7583,   7589,   7591,   7603,   7607,  7621,   7639,   7643, 
    7649,   7669,   7673,   7681,   7687,   7691,   7699,  7703,   7717,   7723, 
    7727,   7741,   7753,   7757,   7759,   7789,   7793,  7817,   7823,   7829, 
    7841,   7853,   7867,   7873,   7877,   7879,   7883,  7901,   7907,   7919]

def secondDiviseur(a):
    """Renvoie le premier diviseur de a supérieur à 1
    Ce diviseur est nécessairement premier
    >>> secondDiviseur(15845465)
    5
    >>> secondDiviseur(1)==1 and secondDiviseur(2)==2 and secondDiviseur(6)==2
    True
    >>> secondDiviseur(153)==3 and secondDiviseur(157)==157 and secondDiviseur(13)==13
    True
    """
    dividor = 1
    if a == 1:
        return a
    while True:
        if a % dividor == 0 and dividor > 1:
            break
        dividor += 1
    return dividor


def eDiviseurs(a):
    """renvoie la liste croissante des diviseurs positifs de a
    >>> eDiviseurs(60)
    {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 60, 30}
    >>> eDiviseurs(1)
    {1}
    >>> eDiviseurs(13)
    {1, 13}
    """
    aSet = set()
    for aDividor in range(1, a+1):
        if a % aDividor == 0:
            aSet.add(aDividor)
    return aSet


def lPGCD(a, b):
    """ Renvoie le couple : (liste des dividendes,le PGCD)
    >>> lPGCD(360,304)
    ([1, 5, 2], 8)
    >>> lPGCD(517,513)
    ([1, 128], 1)
    >>> lPGCD(513,517)
    ([0, 1, 128], 1)
    """
    lq = []
    on_n_a_pas_fini = True
    while (on_n_a_pas_fini):
        q, r = a//b, a % b
        if r == 0:
            on_n_a_pas_fini = False
        else:
            lq += [q]
            a, b = b, r
    return lq, b


def PGCD(a, b):
    """
    >>> PGCD(360,304)
    8
    >>> PGCD(517,513)
    1
    >>> PGCD(513,517)
    1
    """
    l, d = lPGCD(a, b)
    return d


def sontPremiers(a, b):
    """
    >>> sontPremiers(10,21) and sontPremiers(100,37) and not(sontPremiers(4,2))
    True
    """
    return PGCD(a, b) == 1


def solDiophant(a, b, c):
    """
    Renvoie x et y de Z tels que a.x+b.y=c
    sous la forme x=x0+k.rep' et y=y0+k.b'

    >>> solDiophant(2,5,16) #x0,y0,a',b' et les sols sont x=-32+5.k et y=16-2.k
    (-32, 16, 5, -2)
    >>> x0,y0,cx,cy=solDiophant(13,4,12)
    >>> 13*(x0+1234*cx)+4*(y0+1234*cy)==12
    True
    """
    d = PGCD(PGCD(a, b), c)
    aa, bb, cc = a//d, b//d, c//d
    x0, y0, dd = bezout(aa, bb)  # donc a(x-x0)=-b(y-y0)
    assert cc % dd == 0, " Pas de solutions à l'équation"
    ccc = cc//dd
    return x0*ccc, y0*ccc, bb, -aa


def bezout(a, b):
    """Renvoie (u,v,d) tel que a.u+b.v=d avec d=PGCD(a,b)
    >>> bezout(360,304)
    (11, -13, 8)
    >>> bezout(1254,493)
    (-149, 379, 1)
    >>> bezout(513,517)
    (129, -128, 1)
    """
    lq, d = lPGCD(a, b)
    u, v = 1, -lq[-1]
    for k in range(len(lq)-1):
        u, v = v, u-v*lq[-k-2]
    return u, v, d


def estPremier(n):
    """
    >>> estPremier(13) and estPremier(2) and not(estPremier(6))and not(estPremier(35))
    True
    """
    if n == 1:
        return False
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n in primeNumbers:
        return True
    if n > 1E6:
        return isprime(n)  # Pour éviter les ralentissements
    d = 3
    rn = int(sqrt(n)+1)
    while n % d != 0 and d < rn:
        d += 2
    return n % d != 0


def nbPremierSuivant(n):
    """Renvoie le plus petit nombre premier strictement supérieur à n
    >>> nbPremierSuivant(1)==2 and nbPremierSuivant(3)==5 and nbPremierSuivant(20)==23
    True
    """

    p = n+1
    while not(estPremier(p)):
        p += 1
    return p


def nbPremierEtMoitieSuivant(n):
    """renvoie le couple q,p de nombres premiers avec q=(p-1)/2
    >>> nbPremierEtMoitieSuivant(100)
    (107, 53)
    """
    p = nbPremierSuivant(n)
    while not(estPremier((p-1)//2)):
        p = nbPremierSuivant(p+2)
    return p, (p-1)//2


def grandEntier(n):
    """Renvoie le produit de deux nombres premiers choisis au hasard dans [n..2N]"""
    return nbPremierSuivant(randint(n, 2*n))*nbPremierSuivant(randint(n, 2*n))


def strExp(p):
    """renvoie l'exposant tout beau
    >>> strExp(9)
    '⁹'
    >>> strExp(-19)
    '⁻¹⁹'
    >>> strExp(0)
    '⁰'
    >>> strExp(1)
    ''
    """
    SE = "⁰¹²³⁴⁵⁶⁷⁸⁹"  # Cela serait malin de créer plutôt un dictionnaire
    SP, SM = "⁺", "⁻"
    pt = p
    if pt == 0:
        return "⁰"
    if pt == 1:
        return ""
    if pt < 0:
        ch = SM
        pt = -pt
    else:
        ch = ""
    while pt > 0:
        p10p = int(log(pt, 10))
        v10 = 10**p10p
        ch += SE[pt//v10]
        pt = pt % v10
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
    l = lFacteursPremiers(n)
    ch = ""
    for d, p in l:
        ch += f"{d}{strExp(p)}×"
    return ch[:-1]


def lFacteursPremiers(n):
    """renvoie une liste donnant la décomposition en facteurs premiers de n
    >>> lFacteursPremiers(18)
    [(2, 1), (3, 2)]
    >>> lFacteursPremiers(13)
    [(13, 1)]
    """
    assert isinstance(n, int) and n > 0
    if n == 1:
        return [(1, 1)]

    n1 = n
    l, d = [], 0

    while n1 > 1:
        dp = secondDiviseur(n1)
        if dp != d:
            l += [(dp, 1)]
            d = dp
        else:
            l = l[:-1]+[(dp, l[-1][1] + 1)]  # On incrémente la puissance
        n1 = n1//dp
    return l


def indicatriceEuler(n):
    """
    >>> indicatriceEuler(5)==4 and indicatriceEuler(15)==8 and indicatriceEuler(125)==100
    True
    """
    lfp = lFacteursPremiers(n)
    res = 1
    for p, k in lfp:
        res *= (p-1)*p**(k-1)
    return res


def lDecompoPGCDetPPCM(a, b):
    """Renvoie ce couple de décomposition en facteurs premiers
    en utilisant la décomposition en facteurs premier de a et b
    >> lDecompoPGCDetPPCM(60,700)
    [(2, 2),(5, 1)], [(2, 2), (5, 2), (7, 1)]
    """
    pass
# Les méthodes magiques : https://blog.finxter.com/python-dunder-methods-cheat-sheet/


class ElementDeZnZ(object):
    "Elément de Z/nZ"

    def __init__(self, val, n=256):
        """
        >>> ElementDeZnZ(-1,10)
        ElementDeZnZ(9,10)
        >>> ElementDeZnZ(ElementDeZnZ(9,10))
        ElementDeZnZ(9,10)
        """
        if isinstance(val, ElementDeZnZ):
            self.val = val.val
            self.n = val.n
        else:
            self.n = n
            self.val = val % n

    @property
    def a(self):
        return self.val

    @a.setter
    def a(self, _a):
        self.val = _a

    def __str__(self):
        """
        >>> print(ElementDeZnZ(-1,5))
        4[5]
        """
        return str(f"{self.val}[{self.n}]")

    def __repr__(self):
        """
        >>> ElementDeZnZ(-1,5)
        ElementDeZnZ(4,5)
        """
        return str(f"ElementDeZnZ({self.val},{self.n})")

    def __add__(self, other):
        """
        >>> ElementDeZnZ(2,10)+ElementDeZnZ(3,10)
        ElementDeZnZ(5,10)
        >>> ElementDeZnZ(2,10)+3
        ElementDeZnZ(5,10)
        """
        if isinstance(other, ElementDeZnZ):
            assert(self.n == other.n)
            return ElementDeZnZ(self.val + other.val, self.n)
        else:
            return ElementDeZnZ(self.val + other, self.n)            

    def __radd__(self, other):
        """
        >>> 2+ElementDeZnZ(3,10)
        ElementDeZnZ(5,10)
        """
        return self.__add__(other)

    def __mul__(self, other):
        """
        >>> ElementDeZnZ(2,10)*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        >>> ElementDeZnZ(2,10)*3
        ElementDeZnZ(6,10)
        """
        if isinstance(other, ElementDeZnZ):
            assert(self.n == other.n)
            return ElementDeZnZ(self.val * other.val, self.n)
        else:
            return ElementDeZnZ(self.val * other, self.n)

    def __rmul__(self, other):
        """
        >>> 2*ElementDeZnZ(3,10)
        ElementDeZnZ(6,10)
        """
        return self.__mul__(other)

    def __floordiv__(self, other):
        """
        Opération inverse de la multiplication : ElementDeZnZ(4,10)//ElementDeZnZ(5,10) doit renvoyer une erreur
        >>> ElementDeZnZ(9,10)//ElementDeZnZ(3,10)
        ElementDeZnZ(3,10)
        >>> ElementDeZnZ(1,10)//ElementDeZnZ(3,10)
        ElementDeZnZ(7,10)
        """
        if isinstance(other, ElementDeZnZ):
            b = other.val
        else:
            b = other
        u, v, d = bezout(b, self.n)
        ch = f"Il n'existe pas de dividende de {b} par {self}"
        assert self.val % d == 0, ch
        return ElementDeZnZ(u*(self.val//d), self.n)

    def __eq__(self, other):
        """
        >>> ElementDeZnZ(9,10)==ElementDeZnZ(-1,10)
        True
        >>> ElementDeZnZ(9,10)==ElementDeZnZ(1,10)
        False
        >>> ElementDeZnZ(9,10)==9
        True
        """
        if isinstance(other, ElementDeZnZ):
            return self.val == other.val and self.n == other.n
        else:
            return self.val == other % self.n

    def __neg__(self):
        """
        >>> -ElementDeZnZ(9,10)==ElementDeZnZ(1,10)
        True
        >>> -ElementDeZnZ(9,10)==2
        False
        >>> -ElementDeZnZ(9,10)==1
        True
        """
        return ElementDeZnZ(-self.val, self.n)

    def __sub__(self, other):
        """
        >>> a4=ElementDeZnZ(-1,5);a1=ElementDeZnZ(1,5);a1+a4==0
        True
        >>> (-a4+a4==0) and (a4//4==1) and (4*a1+(-a1*4)==0)
        True
        """
        if isinstance(other, ElementDeZnZ):
            assert(self.n == other.n)
            return ElementDeZnZ(self.val - other.val, self.n)
        else:
            return ElementDeZnZ(self.val - other, self.n)

    def __rsub__(self, other):
        """
        >>> 4-ElementDeZnZ(3,5)
        ElementDeZnZ(1,5)
        """
        if isinstance(other, ElementDeZnZ):
            assert(self.n != other.n)
            return ElementDeZnZ(other.val - self.val, self.n)
        else:
            return ElementDeZnZ(other - self.val, self.n)

    def __pow__(self, q):
        """
        >>> a=ElementDeZnZ(3,10); a**2==-1 and a**1==3 and a**0==1 and a**3==7 and a**4==1
        True
        """
        # return ElementDeZnZ(pow(self.val, q), self.n)
        def exporapide(a, n):
            if n == 0:
                return 1
            b = exporapide(a, n//2)
            if (n % 2) == 1:
                return (b**2 * a)
            else:
                return (b**2)
        exp = exporapide(self.val, q)
        return ElementDeZnZ(exp, self.n)

    def __int__(self):
        """
        >>> int(ElementDeZnZ(3,10))
        3
        """
        return self.val

    def ordre(self):
        """
        Voir http://www.repcrypta.com/telechargements/fichecrypto_107.pdf
        >>> (ElementDeZnZ(2,7)).ordre()
        3
        >>> (ElementDeZnZ(-2,7)).ordre()
        6
        """
        return self.logDiscret(1)

    def elementPrimitif(self):
        """Renvoie le premier élément primitif (d'ordre n-1) de Z/nZ suivant self
        >>> ElementDeZnZ(2,7).elementPrimitif()
        ElementDeZnZ(3,7)
        """
        res = self+1
        while res.ordre() != self.n-1:
            res = self+1
        return res

    def estPrimitif(self):
        return self.ordre() == self.n-1

    def estInversible(self):
        """
        >>> ElementDeZnZ(3,5).estInversible()
        True
        >>> ElementDeZnZ(10,12).estInversible()
        False
        """
        return PGCD(self.val, self.n) == 1

    def inverse(self):
        """
        >>> ElementDeZnZ(3,5).inverse()==2
        True

        ElementDeZnZ(2,10).inverse() doit renvoyer une erreur
        """
        u, v, d = bezout(self.val, self.n)
        assert d == 1, f"{self} n'est pas inversible !"
        # a et n premiers entre eux
        return ElementDeZnZ(u, self.n)  # a.u=1(n)

    def logDiscret(self, b):
        """Renvoie x tel que self.rep**x==b(self.n)
        n doit être premier pour garantir l'existence
        >>> ElementDeZnZ(2,13).logDiscret(8)
        3
        >>> ElementDeZnZ(2,13).logDiscret(3)
        4
        """
        assert(estPremier(self.n))
        x = 1
        while self.__pow__(x).val != b:
            x += 1
        return x

    def valThChinois(self, other):
        """
        Renvoie c(pq) avec a(p) et b(q) tel que x≡a(p) et x≡b(q) <=>x≡c(p.q)$
        >>> ElementDeZnZ(2,7).valThChinois(ElementDeZnZ(3,10))
        ElementDeZnZ(23,70)
        """
        assert PGCD(
            self.n, other.n) == 1, "p et q ne sont pas premiers entre eux"
        u, v, d = bezout(self.n, other.n)
        return ElementDeZnZ(other.val*self.n*u + self.val*other.n*v, self.n*other.n)
    
    def estUnCarre(self):
        return self.val == int(sqrt(self.val) + 0.5) ** 2

    def racineCarree(self):
        return ElementDeZnZ(sqrt(self.val), self.n)

    def demoDiv(self):
        for k in range(1, self.n):
            a = ElementDeZnZ(k, self.n)
            try:
                ch = f"{a.val}×{a.inverse().val}=1 ({a.n})"
            except:
                ch = f"{a} n'a pas d'inverse"
            try:
                q = (self//a)
                ch += f" et {a.val}×{q.val}={self} "
            except:
                ch += f" et il n'y a pas de solution à {a.val}×X={self} "
            print(ch)

    @staticmethod
    def demo1():
        for k in range(10, 12):
            p1, p2, p3 = nbPremierSuivant(
                4**k), nbPremierSuivant(5**k), nbPremierSuivant(6**k)
            a = ElementDeZnZ(p1, p3)
            print(f"{k:3} : {a.val}×{a.inverse().val}=1 ({a.n})")
            print(f"           et {a.val}{strExp(p2)}={a**p2}")


def demoVitesse():
    print("Démo Vitesse")
    print("Factorisation :")
    for p in range(23, 26):
        n = grandEntier(2**p)
        print(f"{p}: {n}=={chFacteursPremiers(n)}")

    print("Logarithme discret :")
    for p in range(20, 24):
        n = nbPremierSuivant(2**p)
        b = ElementDeZnZ(10**int(p*3/10), n)
        print(f"{p}: 2{strExp(ElementDeZnZ(2,n).logDiscret(b))}=={b}")


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(estPremier(2))

    # demoVitesse()
    # ElementDeZnZ.demo1()
    ElementDeZnZ(8, 60).demoDiv()
    print(ElementDeZnZ(3, 10)**2)
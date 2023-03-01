from Binaire603 import *
from arithmetiqueDansZ import *

class Polynome(object):
    def __init__(self, data=None, p=None) -> None:
        self.coef = []
        self.exp = []
        self.p = p
        if isinstance(data, self):
            self.coef = data.coef
            self.exp = data.exp
        else: #Binaire603
            for b in data:
                self.coef = b
            for b in data:
                self.exp = ElementDeZnZ(b, self.p)
    def __repr__(self) -> str:
        return f"Polynome(F{self.p})"

    def __str__(self) -> str:
        string = "[ "
        for coef, exp in zip(self.coef, self.exp):
            string += coef + strExp(exp) + " +"
        string += " ]."
        return string
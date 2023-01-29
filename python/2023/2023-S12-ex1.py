class ABR:
    def __init__(self, g0, v0, d0):
        self.gauche = g0
        self.cle = v0
        self.droit = d0

    def __repr__(self):
        if self is None:
            return ''
        else:
            return '(' + (self.gauche).__repr__() + ',' + str(self.cle) + ',' +(self.droit).__repr__() + ')'

n0 = ABR(None, 0, None)
n3 = ABR(None, 3, None)
n2 = ABR(None, 2, n3)
abr1 = ABR(n0, 1, n2)


def ajoute(cle,a):
    if a == None:
        return ABR(None,cle,None)
    elif a.cle>cle:
        sag = ajoute(cle,a.gauche)
        return ABR(sag,a.cle,a.droit)
    elif a.cle<cle:
        sad = ajoute(cle,a.droit)
        return ABR(a.gauche,a.cle,sad)
    else:
        return a

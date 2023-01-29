from random import randint 

def lancer(n):
    resultats = []
    for i in range(n):
        de = randint(1,6)
        resultats.append(de)
    return resultats

def paire_6(lancers):
    nb_6 = 0
    for de in lancers:
        if de == 6:
            nb_6 += 1
            if nb_6 == 2:
                return True
    return False

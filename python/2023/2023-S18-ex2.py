def est_un_ordre(tab):
    '''
    Renvoie True si tab est de longueur n et contient tous les entiers
    de 1 à n, False sinon
    '''
    for i in range(1,len(tab)):
        if i not in tab:  #(1)
            return False
    return True


def nombre_points_rupture(ordre):
    '''
    Renvoie le nombre de point de rupture de ordre qui représente un ordre
    de gènes de chromosome
    '''
    assert est_un_ordre(ordre) # ordre n'est pas un ordre de gènes
    n = len(ordre)
    nb = 0
    if ordre[0] != 1: # le premier n'est pas 1
        nb = nb + 1
    i = 0
    while i < n-1:
        if ordre[i]-ordre[i+1] not in [-1, 1]: # l'écart n'est pas 1 #(2)
            nb = nb + 1
        i = i + 1
    if ordre[n-1] != n: # le dernier n'est pas n #(3)
        nb = nb + 1
    return nb

def crible(n):
    """renvoie un tableau contenant tous les nombres premiers plus petit que N"""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(2, n): 
        if tab[i] == True: #(1)
            premiers.append(i)
            for multiple in range(2*i, n, i): #(2)
                tab[multiple] = False #(3)
    return premiers

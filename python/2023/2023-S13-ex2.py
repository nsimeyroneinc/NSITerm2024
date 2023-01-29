def rendu_monnaie(somme_due, somme_versee):
    pieces = [1, 2, 5, 10, 20, 50, 100, 200]
    rendu = [] #(1)
    a_rendre = somme_versee - somme_due #(2)
    i = len(pieces) - 1
    while a_rendre > 0 : #(3)
        if pieces[i] <= a_rendre :
            rendu.append(pieces[i]) #(4)
            a_rendre = a_rendre - pieces[i]
        else :
            i = i-1
    return rendu

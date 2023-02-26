def f(arbre:list,i:int)->int:
    if i >=len(arbre) or arbre[i] is None:
        return 0
    else:
        g=f(arbre,2*i)
        d=f(arbre,2*i+1)
        return 1+max(g,d)
    
arbre=[0,30,20,40,18,25,None,47]
arbre2=[0,9,6,15,3,7,None,18,2,None,None,None,None,None,16,None]
print(f(arbre2,1))

def estEquilibre(arbre: list, i : int) -> bool:
   if i >= len(arbre) or arbre[i] is None:
       return True
   else:
       balance = f(arbre, 2*i+1) - f(arbre, 2*i)
       reponse = balance in [-1, 0, 1]
       return reponse and estEquilibre(arbre,2*i) and estEquilibre(arbre, 2*i+1)
   
print(estEquilibre(arbre2,1))

def infixe(arbre: list) -> list:
    pile = []
    visites = []
    n = 1
    repetition = True
    while repetition :
        while n < len(arbre) and arbre[n] is not None :
            pile.append(n)
            n = 2*n
        if len(pile) == 0 :
            repetition = False
        else :
            n = pile.pop()
            visites.append(arbre[n])
            n = 2*n+1
    return visites

arbre3=[0,45,40,48,17,43,46,49,14,19]
print(infixe(arbre3))

def construitABR(i, ordre):

    while len(nouveau) < i+1:
        nouveau.append(None)
    print(nouveau)

    i_milieu = len(ordre)//2
    nouveau[i] = ordre[i_milieu]
    
    gauche = ordre[:i_milieu]
    if len(gauche) > 0:
        construitABR(2*i, gauche)
    
    droite = ordre[(i_milieu+1):]
    if len(droite) > 0:
        construitABR(2*i+1, droite)



ordre=infixe(arbre2)
nouveau=[0]
print(ordre)        
print(construitABR(1,ordre))
print(nouveau)
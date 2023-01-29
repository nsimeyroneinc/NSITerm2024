def recherche(elt,tab):
  ''' Renvoie l'indice de la première occurrence de elt dans tab si elt est dans tab et -1 sinon'''
  for i in range(len(tab)):
    if tab[i]==elt:
      return i
  return -1

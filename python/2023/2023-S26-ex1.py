def multiplication(n1,n2):
    produit=0
    for i in range(abs(n1)):
        produit += abs(n2)
    if (n1>0 and n2<0) or (n1<0 and n2>0): 
        return -produit
    else:
        return produit
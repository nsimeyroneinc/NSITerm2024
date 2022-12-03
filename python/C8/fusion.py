def fusion(L1, L2):
    L=[]
    n1 = len(L1)
    n2 = len(L2)
    i1 = 0
    i2 = 0
    while i1<n1 or i2<n2:
        if i1>=n1:
            L.append(L2[i2])
            i2 = i2+1
        elif i2>=n2:
            L.append(L1[i1])
            i1=i1+1
        else :
            e1 = L1[i1]
            e2 = L2[i2]
            if e1 > e2:
                L.append(e2)
                i2 = i2 + 1
            else :
                L.append(e1)
                i1 = i1 + 1
    return L

def moitie_droite(L):
    n = len(L)
    deb = n//2
    tab = []
    for i in range(deb,n):
        tab.append(L[i])
    return tab

def moitie_gauche(tab):
    n = len(tab)
    nvx_tab = []
    if n==0:
        return []
    mil = n//2
    if n%2 == 0:
        lim = mil
    else :
        lim =mil+1
    for i in range(lim):
        nvx_tab.append(tab[i])
    return nvx_tab
    
def tri_fusion(L):
    n = len(L)
    if n<=1 :
        return L
    print(L)
    mg = moitie_gauche(L)
    md = moitie_droite(L)
    L1 = tri_fusion(mg)
    L2 = tri_fusion(md)
    return fusion(L1, L2)


L=[3, 5, 2]
M = [4, 1, 11, 7]

T=fusion(L,M)
P=tri_fusion(T)
print(P)
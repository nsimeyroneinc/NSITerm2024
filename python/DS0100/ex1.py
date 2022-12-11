
def moitie_droite(L):
    n = len(L)
    deb = n//2
    tab = []
    for i in range(deb,n):
        tab.append(L[i])
    return tab



def moitie_gauche(L):
    n = len(L)
    fin = n//2
    tab = []
    for i in range(fin):
        tab.append(L[i])
    return tab

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
    
M = [4, 1, 11, 7]


L = [3, 5, 2, 7, 1, 9, 0]

def moitie_gauche2(L):
    half=len(L)//2
    return L[:half]


def moitie_gauche3(L):
    n=len(L)
    nvx_tab=  []
    if n==0:
        return []
    mil=n//2

    for i in range(mil):
        nvx_tab.append(L[i])
    return nvx_tab


print(moitie_gauche3(L))
#tri_fusion([9,5,3,1,7,6,10,3])

def tri_insertion(liste):
    for indice_courant in range(1, len(liste)):
        element_a_inserer = liste[indice_courant]
        i = indice_courant - 1
        while i >= 0 and liste[i] > element_a_inserer:
            liste[i+1] = liste[i]
            i=i-1
            print(f"Passage {indice_courant} : {liste}")
        liste[i + 1] = element_a_inserer
        print(f"Passage {indice_courant} : {liste}")
            

notes = [8, 7, 18, 14, 12, 9, 17, 3]
tri_insertion(notes)


def tri_insertion2(liste):
    for indice_courant in range(1, len(liste)):
        element_a_inserer = liste[indice_courant]
        i = indice_courant - 1
        while i >= 0 and liste[i] > liste[i+1]:
            liste[i],liste[i+1]=liste[i+1],liste[i]
            i=i-1
        liste[i + 1] = element_a_inserer
        print(f"Passage {indice_courant} : {liste}")

notes = [8, 7, 18, 14, 12, 9, 17, 3]

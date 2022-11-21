
def creer_pile_vide():
    return []
      
def est_vide(P):
    if P==[]:
        return True
    else:
        return False
  
    
def empiler(P,x):
    P.append(x)

def depiler(P):
    if est_vide(P) == True :
        raise IndexError("Vous avez essayé de dépiler une pile vide !")
    else :
        return P.pop()

def affiche(P):       # Hors-Programme : pour afficher 
    s = "|"              # convenablement la pile avec print(p)
    for k in P :
        s = s + str(k) + "|"
    print(s)

P=creer_pile_vide()
empiler(P,8)
empiler(P,5)
empiler(P,2)
empiler(P,4)


#Q=creer_pile_vide()
#while not est_vide(P):
#    empiler(Q,depiler(P))

affiche(P)


def hauteur_pile(P):
    Q=creer_pile_vide()
    n=0
    while not est_vide(P):
        n+=1
        x=depiler(P)
        empiler(Q,x)
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return n


def max_pile(P,i):
    Q=creer_pile_vide()
    indice=1
    indiceDuMax=1
    max=depiler(P)
    empiler(Q,max)
    while indice<i: #On a inégalité stricte car on par de l ' indice 2 pour la boucle
        x=depiler(P)
        indice+=1
        if x>max:
            max=x
            indiceDuMax=indice
        empiler(Q,x)
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return indiceDuMax



def max_pile_v(P,i):
    Q=creer_pile_vide()
    sommetpile=1
    x=depiler(P)
    max=x
    empiler(Q,x)
    n=1
    while sommetpile<i and not (est_vide(P)): #On a inégalité stricte car on par de l ' indice 2 pour la boucle
        sommetpile+=1
        x=depiler(P)
        empiler(Q,x)
        if x>max:
            n=sommetpile
            max=x
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return n

def max_pile_e(P,i):
    Q=creer_pile_vide()
    n=1
    position=1
    
    x=depiler(P)
    empiler(Q,x)
    elt_m=x
    while n<i:
        #rajout
        x=depiler(P)
        #fin rajout
        n=n+1
        if elt_m<x:
            elt_m=x
            position=n
        #rajout
        empiler(Q,x)
        #fin rajout
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return position


def max_pile_hugo(P,i):
    Q=creer_pile_vide()
    n=1
    position=1
    
    x=depiler(P)
    empiler(Q,x)
    elt_m=x
    while n<i:
        #rajout
        x=depiler(P)
        #fin rajout
        n=n+1
        if elt_m<x:
            elt_m=x
            position=n
        #rajout
        empiler(Q,x)
        #fin rajout
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return position

def max_pile_quentin(P,i):
    Q=creer_pile_vide()
    maxi=-1E99
    maxi_pos=0
    n1=0
    for _ in range(n):
        n1+=1
        x=depiler(P)
        empiler(Q,x)
        if x>maxi:
            maxi=x
            maxi_pos=n1
    while not est_vide(Q):
        empiler(P,depiler(Q))
    return n1


def max_pile_mael(P,i):
    Q=creer_pile_vide()
    n=0
    position=0
    elt_m=0
    while n<i:
        n=n+1
        x=depiler(P)
        empiler(Q,x)
        if elt_m<x:
            elt_m=x
            position=n
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return position


def max_pile_lucas(P,i):
    B=creer_pile_vide()
    B=P
    Q=creer_pile_vide()
    A=creer_pile_vide()
    if i == 0:
        return False
    if i==1:
        return 1
    x=depiler(P)
    m=1
    for j in range(i-1):
        d=depiler(P)
        if x>d:
            x=depiler(A)
            empiler(Q,x)
        else:
            m=j
            empiler(Q,x)
            x=depiler(A)
    while not est_vide(B):
        x=depiler(B)
        empiler(A,x)
    while not est_vide(A):
        x=depiler(A)
        empiler(P,x)
    return m

def max_pile_ruben(P,i):
    Q=creer_pile_vide()
    position_maxi=1
    x=depiler(P)
    maxi=x
    empiler(Q,x)
    position=1
    while position_maxi<i:
        position_maxi+=1
        x=depiler(P)
        empiler(Q,x)
        if x>maxi:
            position=position_maxi
            maxi=x
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)

    return position


def max_pile_clement(P,i):
    rang=1
    rang_max=1
    maxi=depiler(P)
    empiler(P,maxi)
    Q=creer_pile_vide()


def max_pile_LucaP(P,i):
    Q=creer_pile_vide()
    sommetdelapile=1
    x=depiler(P)
    elementmax=x
    empiler(Q,x)
    position=1
    while sommetdelapile<i and not est_vide(P):
        sommetdelapile+=1
        x=depiler(P)
        empiler(Q,x)
        if x>elementmax:
            position=sommetdelapile
            elementmax=x
    while not est_vide(Q):
        x=depiler(Q)
        empiler(P,x)
    return position



def max_pile_antoine(P,i):

    maxi=depiler(P)
    j_maxi=1

    Q=creer_pile_vide()
    for j in range(1,i):
        x=depiler(P)
        empiler(Q,x)
        if maxi<x:
            maxi=x
            j_maxi=j+1
    return j_maxi


def max_pile_pierick(P,i):
    Q=creer_pile_vide()
    r=1
    r_max=1
    max=depiler(P)
    empiler(Q,max)
    while r<=i:
        x=depiler(P)
        if x>max:
            max=r
            r_max=r
        empiler(Q,x)
        r+=1
    while not est_vide(Q):
        empiler(P,depiler(Q))
    return r_max

def max_pile_matteo(P,i):
    Q=creer_pile_vide()
    rang=1
    rang_m=1
    max=depiler(P)
    empiler(Q,max)
    while r<=i:
        x=depiler(P)
        if x>max:
            max=r
            r_max=r
        empiler(Q,x)
        r+=1
    while not est_vide(Q):
        empiler(P,depiler(Q))
    return r_max

def max_pile_alex(P,i):
   pass


def max_pile_lucas(P,i):
    Q=creer_pile_vide()
    max=depiler(P)
    empiler(Q,max)
    j_max=1
    for k in range(i-1):
        if not est_vide(P):
            x=depiler(P)
            if x>max:
                max=x
                j_max=k
        empiler(Q,x)
    while not est_vide(Q):
        empiler(P,depiler(Q))
    return j_max


P=creer_pile_vide()
empiler(P,18)
empiler(P,15)
empiler(P,2)
empiler(P,4)
empiler(P,1)



#Q=creer_pile_vide()
#while not est_vide(P):
#    empiler(Q,depiler(P))

affiche(P)
y=4
print('Enzo max : ',max_pile_e(P,y))
#print('cor max : ',max_pile(P,y))
#print('Quentin max : ',max_pile_e(P,y))
#print('Mael max : ',max_pile_mael(P,y))
#print('Lucas max : ',max_pile_lucas(P,y))
#print('Ruben max : ',max_pile_ruben(P,y))
#print('Lucas P max : ',max_pile_LucaP(P,y))

#print('Antoine max : ',max_pile_antoine(P,y))
#print('Pierrick max : ',max_pile_pierick(P,y))
print('Lucas C max : ',max_pile_lucas(P,y))

def retourner(P,j):
    Q1=creer_pile_vide()
    Q2=creer_pile_vide()
    k=1
    while k<=j:
        x=depiler(P)
        empiler(Q1,x)
        k+=1
    while not est_vide(Q1):
        el=depiler(Q1)
        empiler(Q2,el)
    while not est_vide(Q2):
        y=depiler(Q2)
        empiler(P,y)
    return P
 




def retourner_v(P,j):
    Q=creer_pile_vide()
    Z=creer_pile_vide()

    for i in range(j):
        if not est_vide(P):
            affiche(P)
            affiche(Q)
            affiche(Z)
            empiler(Q,depiler(P))
            empiler(Z,depiler(Q))

    while not est_vide(Z):
        empiler(P,depiler(Z))
    return P


def retourner_enzo(P,j):
    Q=creer_pile_vide()
    S=creer_pile_vide()
    n=0
    while n<j:
        x=depiler(P)
        empiler(Q,x)
        n=n+1
    while not est_vide(Q):
        x=depiler(Q)
        empiler(S,x)
    while not est_vide(S):
        x=depiler(S)
        empiler(P,x)
    return P
 
def retourner_titouan(P,j):
    Q=creer_pile_vide()
    R=creer_pile_vide()
    nb=0
    while nb<j and not est_vide(P):
        nb+=1
        empiler(Q,depiler(P))
    nb=0
    while nb<j and not est_vide(Q):
        nb+=1
        empiler(R,depiler(Q))
    nb=0
    while nb <j and not est_vide(R):
        nb+=1
        empiler(P,depiler(R))
    return P


def retourner_quentin(P,j):
    Q1=creer_pile_vide()
    Q2=creer_pile_vide()
    for _ in range(j):
        empiler(Q1,depiler(P))
    while not est_vide(Q1):
        empiler(Q2,depiler(Q1))
    while not est_vide(Q2):
        empiler(P,depiler(Q2))
    return P


def retourner_mael(P,j):
    Q=creer_pile_vide()
    S=creer_pile_vide()
    n=0
    while n<j:
        n+=1
        x=depiler(P)
        empiler(Q,x)

    while not est_vide(Q):
        x=depiler(Q)
        empiler(S,x)
    while not est_vide(S):
        x=depiler(S)
        empiler(P,x)
    return P

def retourner_lucas(P,j):
    A=creer_pile_vide()
    B=creer_pile_vide()
    for k in range(j):
        x=depiler(P)
        empiler(A,x)

    while not est_vide(A):
        x=depiler(A)
        empiler(B,x)
    while not est_vide(B):
        x=depiler(B)
        empiler(P,x)
    return P


def retourner_ruben(P,i):
    Q=creer_pile_vide()
    S=creer_pile_vide()
    n=0
    while n<i and not est_vide(P):
        n+=1
        x=depiler(P)
        empiler(Q,x)
    n=0
    while n<i and not est_vide(Q):
        x=depiler(Q)
        empiler(S,x)
    n=0
    while n<1 and not est_vide(S):
        x=depiler(S)
        empiler(P,x)
    return P

def retourner_clement(P,i):
    Q=creer_pile_vide()
    R=creer_pile_vide()
    rang=1
    while rang<=i:
        x=depiler(P)
        empiler(Q,x)
        rang+=1

    while not est_vide(Q):
        x=depiler(Q)
        empiler(R,x)
    
    while not est_vide(R):
        x=depiler(R)
        empiler(P,x)
    return P



def retourner_lucasP(P,j):

    Q=creer_pile_vide()
    R=creer_pile_vide()
    nb=0
    while nb<j and not est_vide(P):
        nb+=1
        empiler(Q,depiler(P))
    nb=0
    while nb<j and not est_vide(Q):
        nb+=1
        empiler(R,depiler(Q))
    nb=0
    while nb <j and not est_vide(R):
        nb+=1
        empiler(P,depiler(R))
    return P

def retourner_antoine(P,j):
    Q1=creer_pile_vide()
    Q2=creer_pile_vide()
    
    for i in range(j):
        x=depiler(P)
        empiler(Q1,x)

    while not est_vide(Q1):
        x=depiler(Q1)
        empiler(Q2,x)
    while not est_vide(Q2):
        x=depiler(Q2)
        empiler(P,x)
    return P


def retourner_alex(P,j):
    T=creer_pile_vide()
    T1=creer_pile_vide()

    for i in range(j):
        if not est_vide(P):
            empiler(T,depiler(P))
    while not est_vide(T):    
        empiler(T1,depiler(T))
    while not est_vide(T1):
        empiler(P,depiler(T1))


def retourner_lucasC(P,j):
    Q=creer_pile_vide()
    R=creer_pile_vide()
    for i in range(j):
        empiler(Q,depiler(P))
        empiler(R,depiler(Q))
        

    
    while not est_vide(R):
        x=depiler(R)
        empiler(P,x)
    return P


P=creer_pile_vide()
empiler(P,8)
empiler(P,5)
empiler(P,2)
empiler(P,4)


print('Lucas C :')
affiche(P)
retourner_lucasC(P,3)
affiche(P)

#print('Alex :')
#affiche(P)
#retourner_alex(P,3)
#affiche(P)

#print('Antoine :')
#affiche(P)
#retourner_antoine(P,3)
#affiche(P)

#print('LucasP :')
#affiche(P)
#retourner_lucasP(P,3)
#affiche(P)

#print('Clement : ')
#print(retourner_clement(P,3))

#print('Ruben : ')
#print(retourner_ruben(P,3))

#print('Lucas : ')
#print(retourner_lucas(P,4))

#print('Mael : ')
#print(retourner_mael(P,3))


#print('Quentin : ')
#print(retourner_quentin(P,3))

#print('Titouan :')
#affiche(P)
#retourner_titouan(P,3)
#affiche(P)


def tri_crepe(P):
    k=hauteur_pile(P)
    while k >0:
        i=max_pile(P,k)
        retourner(P,i)
        retourner(P,k)
        k-=1
    return P



P1=creer_pile_vide()
empiler(P1,5)
empiler(P1,9)
empiler(P1,3)
empiler(P1,6)





def tri_crepe_v(P):
    haut=hauteur_pile(P)
    while haut!=0:
        max=max_pile(P,haut)
        retourner(P,max)
        retourner(P,haut)
        haut-=1
    return P


def tri_crepe_enzo(P):
    h=hauteur_pile(P)
    m=max_pile(P,h)
    while not h==m:
        retourner(P,m)
        retourner(P,h)
        m=max_pile(P,h)
        
    return P

def tri_crepe_titouan(P):
    h=hauteur_pile(P)
    while h!=0:
        maximum=max_pile(P,h)
        retourner(P,maximum)
        retourner(P,h)
        h-=1
    return P

def tri_crepe_quentin(P):
    h=hauteur_pile(P)
    while h>1:
        x=max_pile(P,h)
        if x<h:
            retourner(P,x)
            retourner(P,h)
        h-=1
    return P

def tri_crepe_mael(P):
    h=hauteur_pile(P)
    c_max=max_pile(P,h)
    while not h==m:
        retourner(P,m)
        retourner(P,h)
        m=max_pile(P,h)
        
    return P

def tri_crepe_lucas(P):
    Q=creer_pile_vide()
    for i in range(hauteur_pile(P)):
        while not est_vide(P):
            y=depiler(P)
            if x>=y:
                empiler(Q,y)
            else:
                
                empiler(Q,x)        
    while not est_vide(Q):
        empiler(P,depiler(Q))

    return P


def tri_crepe_ruben(P):
    t=hauteur_pile(P)
    
    while t!=0:
        maxi=max_pile(P,t)
        retourner(P,maxi)
        retourner(P,t)
        t-=1
        
    return P

def tri_crepe_clement(P):
    h=hauteur_pile(P)
    rang_maxi=max_pile(P,h-i)
    retourner(P,rang_maxi)
    retourner(P,h-i)
    return P


def tri_crepe_Pierrick(P):
    h=hauteur_pile(P)
    for i in range(0,h-1):
        rang_max=max_pile(P,h-i)
        retourner(P,rang_max)
        retourner(P,h-i)
        
    return P


def tri_crepe_lucasC(P):
    for i in range(hauteur_pile(P)):
        retourner(P,max_pile(P,hauteur_pile(P)-i))
        retourner(P,hauteur_pile(P))
    return P

P=creer_pile_vide()
empiler(P,8)
empiler(P,5)
empiler(P,12)
empiler(P,14)
empiler(P,7)
empiler(P,54)
empiler(P,127)
empiler(P,71)


P1=creer_pile_vide()
empiler(P1,5)
empiler(P1,9)
empiler(P1,3)
empiler(P1,6)


affiche(P)
print('tri Lucas C ',tri_crepe_lucasC(P))

affiche(P1)

print('tri Lucas C ',tri_crepe_lucasC(P1))
#print('tri clement ',tri_crepe_clement(P))
#print('tri ruben ',tri_crepe_ruben(P))

#affiche(P)
#print('tri enzo ',tri_crepe_enzo(P))

#print('tri titouan ',tri_crepe_titouan(P))
#print('tri lucas ',tri_crepe_lucas(P))



#affiche(P1)
#print('tri enzo ',tri_crepe_enzo(P1))
#print('tri titouan ',tri_crepe_titouan(P1))


#print('tri quentin ',tri_crepe_quentin(P1))
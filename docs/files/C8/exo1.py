def maxi(liste):
    if len(liste)==1:
        return liste[0]
    i_centre=(len(liste))//2
    l1=liste[:i_centre]
    l2=liste[i_centre:]
    m1=maxi(l1)
    m2=maxi(l2)
    if m1>m2:
        return m1
    else: 
        return m2


        
        

L=[152,19,120,33,11,15,9,14,57]

print(maxi(L))

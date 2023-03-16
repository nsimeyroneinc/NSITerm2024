from math import sqrt
class Segment:
    def __init__(self,point1,point2):
        self.p1=point1
        self.p2=point2
        self.longueur= sqrt((point1[0]-point2[0])**2+(point1[1]-point2[1])**2)
        
        
def liste_segments(liste_points):
    n = len(liste_points)
    segments = []
    for i in range(n-1):
        for j in range(i+1, n):
            # On construit le segment à partir des points i et j.
            seg = Segment(liste_points[i],liste_points[j])
            segments.append(seg) # On l'ajoute à la liste
    return segments    

def plus_court_segment(liste_segments):
    if len(liste_segments)==1:
        return liste_segments[0]
    else:
        milieu=len(liste_segments)//2
        c1=plus_court_segment(liste_segments[milieu:])
        c2=plus_court_segment(liste_segments[:milieu])
        if c1.longueur>c2.longueur:
            return c2
        else:
            return c1
        
point_A=(3,4)
point_B=(2,3)
point_C=(-3,-1)

nuage_points=[point_A,point_B,point_C]

liste_points=[point_A,point_B,point_C]
liste_segments(liste_points)

rep=plus_court_segment(liste_segments(liste_points))

print((rep.p1[0],rep.p1[1]),(rep.p2[0],rep.p2[1]))
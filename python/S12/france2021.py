class Noeud():
    def __init__(self, v):
        self.ag = None
        self.ad = None
        self.v = v
            
    def insere(self, v):
        n = self
        est_insere = False
        while not est_insere :
            if v == n.v:
                est_insere = True             
            elif v < n.v:                  
                if n.ag != None:           
                    n = n.ag                  
                else:                         
                    n.ag = Noeud(v)             
                    est_insere = True         
            else:
                if n.ad != None:           
                    n = n.ad                  
                else:                         
                    n.ad = Noeud(v)           
                    est_insere = True       
                        
    def insere_tout(self, vals):
        for v in vals:
            self.insere(v) 

racine = Noeud(18)
racine.insere_tout([12, 13, 15, 16, 19, 21, 32, 23])
print(racine)
class Triunghi:
    def __init__(self, idt, p1, p2, p3):
        self.id = idt
        self.punct1 = p1
        self.punct2 = p2
        self.punct3 = p3
    
    def getId(self):
        """
        Returneaza id-ul triunghiului
        Date iesire: id - int
        """
        return self.id

    def getPuncte(self):
        """
        Returneaza lista de varfuri
        Date iesire: lista de puncte
        """
        return [self.punct1, self.punct2, self.punct3]
    
    def setPuncte(self, puncte):
        """
        Seteaza punctele cu o lista data
        """
        self.punct1 = puncte[0]
        self.punct2 = puncte[1]
        self.punct3 = puncte[2]
    
    def punctInTriunghi(self, punct):
        """
        Verifica daca un punct dat este in triunghi
        """
        if punct.equalPoints(self.punct1) or punct.equalPoints(self.punct2) or punct.equalPoints(self.punct3):
            return True
        return False
    
    def getPerimetru(self):
        """
        Returneaza perimetrul triunghiului
        """
        latura1 = self.punct1.distanceToPoint(self.punct2)
        latura2 = self.punct1.distanceToPoint(self.punct3)
        latura3 = self.punct2.distanceToPoint(self.punct3)
        return latura1 + latura2 + latura3
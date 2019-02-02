class Service:
    def __init__(self, repo):
        self.repository = repo
    
    def adaugarePunct(self, punct):
        """
        Adauga un punct in baza de date
        Date intrare: punct - de tip Punct
        """
        puncte = self.repository.getPuncte()
        puncte.append(punct)
        self.repository.setPuncte(puncte)
        return True
    
    def adaugareTriunghi(self, triunghi):
        """
        Adauga un triunghi in baza de date
        Date intrare: triunghi - de tip Triunghi
        """
        triunghiuri = self.repository.getTriunghiuri()
        triunghiuri.append(triunghi)
        self.repository.setTriunghiuri(triunghiuri)
    
    def getPerimetre(self):
        """
        Returneaza lista cu toate perimetrele triunghiurilor
        Date iesire: result - lista de perimetre (int)
        """
        triunghiuri = self.repository.getTriunghiuri()
        result = {}
        for triunghi in triunghiuri:
            result[triunghi] = triunghi.getPerimetru()
        return result

    def getTriunghiuriVarfIntreg(self):
        """
        Returneaza toate triunghiurile cu un varf ce are coordonate puncte intregi
        Date iesire: result - lista de triunghiuri
        """
        triunghiuri = self.repository.getTriunghiuri()
        result = []
        for triunghi in triunghiuri:
            puncte = triunghi.getPuncte()
            ok = False
            for punct in puncte:
                if punct.isInteger() == True:
                    ok = True
            if ok == True:
                result.append(triunghi)
        return result
    
    def getPuncteSingure(self):
        """
        Returneaza toate punctele ce nu apartin niciunui triunghi
        Date iesire: result - lista de puncte
        """
        triunghiuri = self.repository.getTriunghiuri()
        puncte = self.repository.getPuncte()
        result = []
        for punct in puncte:
            ok = True
            for triunghi in triunghiuri:
                if triunghi.punctInTriunghi(punct):
                    ok = False
                    break
            if ok == True:
                result.append(punct)
        return result
    
    def existingPoint(self, point):
        """
        Verifica daca un punct dat exista deja
        """
        puncte = self.repository.getPuncte()
        for punct in puncte:
            if punct.equalPoints(point):
                return True
        return False
    
    def getUniqueId(self):
        """
        Returneaza un id inexistent in baza de date
        """
        idt = 0
        triunghiuri = self.repository.getTriunghiuri()
        ok = False
        while ok == False:
            ok = True
            for triunghi in triunghiuri:
                if triunghi.getId() == idt:
                    ok = False
            if ok == False:
                idt += 1
        return idt
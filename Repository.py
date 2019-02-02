from Punct import Punct
from Triunghi import Triunghi
import copy
class Repository:
    def __init__(self, puncte, triunghiuri):
        self.puncteDB = puncte
        self.triunghiuriDB = triunghiuri
        self.puncte = self.importPuncte(self.puncteDB)
        self.triunghiuri = self.importTriunghiuri(self.triunghiuriDB)
    
    def savePuncte(self):
        """
        Salveaza starea curenta a punctelor
        """
        file = open(self.puncteDB, "w")
        for punct in self.puncte:
            line = str(punct.getX()) + " " + str(punct.getY())
            line += "\n"
            file.write(line)
    
    def saveTriunghiuri(self):
        """
        Salveaza starea curenta a triunghiuri
        """
        file = open(self.triunghiuriDB, "w")
        for triunghi in self.triunghiuri:
            puncte = triunghi.getPuncte()
            line = str(triunghi.getId()) + " " + str(puncte[0].getX()) + " " + str(puncte[0].getY()) + " " + str(puncte[1].getX()) + " " + str(puncte[1].getY()) + " " + str(puncte[2].getX()) + " " + str(puncte[2].getY())
            line += "\n"
            file.write(line)
    
    def importPuncte(self, puncteDB):
        """
        Importeaza toate punctele
        """
        try:
            file = open(puncteDB, "r")
        except:
            file = open(puncteDB, "w")
            file.write("")
            return []
        lista = []
        for line in file:
            line = line.strip("\n").split(" ")
            try:
                punct = Punct(float(line[0]), float(line[1]))
                lista.append(punct)
            except:
                pass
        return lista
    
    def importTriunghiuri(self, triunghiuriDB):
        """
        Importeaza toate triunghiurile
        """
        try:
            file = open(triunghiuriDB, "r")
        except:
            file = open(triunghiuriDB, "w")
            file.write("")
            return []
        lista = []
        for line in file:
            line = line.strip("\n").split(" ")
            try:
                punct1 = Punct(float(line[1]), float(line[2]))
                punct2 = Punct(float(line[3]), float(line[4]))
                punct3 = Punct(float(line[5]), float(line[6]))
                triunghi = Triunghi(int(line[0]), punct1, punct2, punct3)
                lista.append(triunghi)
            except:
                pass
        return lista
    
    def getPuncte(self):
        """
        Returneaza toate punctele
        """
        return copy.deepcopy(self.puncte)
    
    def getTriunghiuri(self):
        """
        Returneaza toate triunghiurile
        """
        return copy.deepcopy(self.triunghiuri)
    
    def setPuncte(self, puncte):
        """
        Seteaza lista de puncte cu una data
        Date intrare: puncte - lista de puncte
        """
        self.puncte = puncte
        self.savePuncte()
    
    def setTriunghiuri(self, triunghiuri):
        """
        Seteaza lista de triunghiuri cu una data
        Date intrare: triunghiuri - lista de triunghiuri
        """
        self.triunghiuri = triunghiuri
        self.saveTriunghiuri()
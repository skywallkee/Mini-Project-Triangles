from Repository import Repository
from Service import Service
from Punct import Punct
from Triunghi import Triunghi
class Test:
    def __init__(self):
        repo = Repository("testPuncte.txt", "testTriunghiuri.txt")
        serv = Service(repo)
        self.service = serv
        self.repo = repo
    
    def testAdaugarePunct(self):
        puncte = self.repo.getPuncte()
        lungime = len(puncte)
        punct = Punct(0.5, 1.2)
        self.service.adaugarePunct(punct)
        puncte = self.repo.getPuncte()
        assert(len(puncte) == lungime + 1)
    
    def testAdaugareTriunghi(self):
        triunghiuri = self.repo.getTriunghiuri()
        lungime = len(triunghiuri)
        idt = self.service.getUniqueId()
        punct1 = Punct(0.5, 1.2)
        punct2 = Punct(1.2, 2.2)
        punct3 = Punct(27, 3.6)
        triunghi = Triunghi(idt, punct1, punct2, punct3)
        self.service.adaugareTriunghi(triunghi)
        triunghiuri = self.repo.getTriunghiuri()
        assert(len(triunghiuri) == lungime + 1)

    def testPerimetruTriunghi(self):
        perimetre = self.service.getPerimetre()
        triunghiuri = self.repo.getTriunghiuri()
        assert(len(perimetre) == len(triunghiuri))

    def testTriunghiuriCuCoordonate(self):
        lista = self.service.getTriunghiuriVarfIntreg()
        assert(len(lista) == 0)
    
    def testPuncteCeNuApartin(self):
        singure = self.service.getPuncteSingure()
        assert(len(singure) == 0)

    def runTests(self):
        self.testAdaugarePunct()
        print("Test adaugare punct trecut")
        self.testAdaugareTriunghi()
        print("Test adaugare triunghi trecut")
        self.testPerimetruTriunghi()
        print("Test perimetre trecut")
        self.testTriunghiuriCuCoordonate()
        print("Test coordonate trecut")
        self.testPuncteCeNuApartin()
        print("Test puncte ce nu apartin niciunui triunghi trecut")
        input("Apasati ENTER pentru a continua.")
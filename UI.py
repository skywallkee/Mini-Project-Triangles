from Punct import Punct
from Triunghi import Triunghi

class UI:
    def __init__(self, serv):
        self.service = serv
        self.menu = {
            "0": "Iesire",
            "1": "Adauga punct",
            "2": "Adauga triunghi",
            "3": "Afiseaza perimetrul triunghiurilor",
            "4": "Afiseaza triunghiuri cu un varf ce are coordonate intregi",
            "5": "Afiseaza puncte ce nu apartin niciunui triunghi"
        }
    
    def clear(self):
        print("\n"*100)

    def display(self):
        self.clear()
        for option in range(0, len(self.menu)):
            option = str(option)
            print(option + ". " + self.menu[option])

    def validOption(self, option):
        if option in self.menu or option == "-1":
            return True
        return False

    def getOption(self):
        option = "Invalid"
        while not self.validOption(option):
            option = input("Alegeti optiunea dorita: ")
        return option
    
    def validPoint(self, p):
        try:
            p = float(p)
        except:
            return False
        return True

    def requestPunct(self):
        x = "invalid"
        while self.validPoint(x) == False:
            x = input("Dati coordonata X: ")
        x = float(x)
        y = "invalid"
        while self.validPoint(y) == False:
            y = input("Dati coordonata Y: ")
        y = float(y)
        punct = Punct(x, y)
        return punct

    def validPunct(self, punct):
        punct = punct.split(" ")
        if self.validPoint(punct[0]) == True and self.validPoint(punct[1]) == True:
            punct = Punct(float(punct[0]), float(punct[1]))
            if self.service.existingPoint(punct) == True:
                return True
        return False

    def requestTriunghi(self):
        p1 = "invalid"
        p2 = "invalid"
        p3 = "invalid"
        while self.validPunct(p1) == False:
            print("Format: X Y")
            p1 = input("Dati punctul 1: ")
            if self.validPunct(p1):
                try:
                    p1 = p1.split(" ")
                    p1 = Punct(p1[0], p1[1])
                    break
                except:
                    p1 = "invalid"
        while self.validPunct(p2) == False:
            print("Format: X Y")
            p2 = input("Dati punctul 2: ")
            if self.validPunct(p2):
                try:
                    p2 = p2.split(" ")
                    p2 = Punct(p2[0], p2[1])
                    if p2.equalPoints(p1):
                        p2 = "invalid"
                    else:
                        break
                except:
                    p1 = "invalid"
        while self.validPunct(p3) == False:
            print("Format: X Y")
            p3 = input("Dati punctul 3: ")
            if self.validPunct(p3):
                try:
                    p3 = p3.split(" ")
                    p3 = Punct(p3[0], p3[1])
                    if p3.equalPoints(p2) or p3.equalPoints(p1):
                        p3 = "invalid"
                    else:
                        break
                except:
                    p1 = "invalid"
        idt = self.service.getUniqueId()
        triunghi = Triunghi(idt, p1, p2, p3)
        return triunghi


    def doOption(self, option):
        if option == "1":
            punct = self.requestPunct()
            if self.service.adaugarePunct(punct) == True:
                print("Adaugare de punct realizata cu succes!")
            else:
                print("Nu s-a putut adauga punctul.")
        elif option == "2":
            triunghi = self.requestTriunghi()
            if self.service.adaugareTriunghi(triunghi) == True:
                print("Adaugare triunghi realizata cu succes!")
            else:
                print("Nu s-a putut adauga triunghiul.")
        elif option == "3":
            perimetre = self.service.getPerimetre()
            print("Perimetrele triunghiurilor sunt: ")
            for triunghi in perimetre:
                print(triunghi.getId(), ":", perimetre[triunghi])
        elif option == "4":
            triunghiuri = self.service.getTriunghiuriVarfIntreg()
            print("Triunghiuri cu varf ce are coordonate intregi: ")
            for triunghi in triunghiuri:
                puncte = triunghi.getPuncte()
                print(triunghi.getId(), puncte[0], puncte[1], puncte[2])
        elif option == "5":
            puncte = self.service.getPuncteSingure()
            print("Punctele ce nu apartin niciunui triunghi sunt: ")
            for punct in puncte:
                print(punct.getX(), punct.getY())
        input("Pentru a continua apasati ENTER.")
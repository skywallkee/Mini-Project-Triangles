import math

class Punct:
    def __init__(self, x, y):
        # Constructor
        self.x = x
        self.y = y

    def getX(self):
        """
        Returneaza x-ul punctului
        Date iesire: x - flaot
        """
        return float(self.x)
    
    def getY(self):
        """
        Returneaza y-ul punctului
        Date iesire: y - float
        """
        return float(self.y)
    
    def setX(self, x):
        """
        Seteaza x-ul punctului cu o alta valoare
        Date intrare: x - float
        """
        self.x = float(x)

    def setY(self, y):
        """
        Seteaza y-ul punctului cu o alta valoare
        Date intrare: y - float
        """
        self.y = float(y)
    
    def distanceToPoint(self, point):
        """
        Returneaza distanta de la punctul curent la un alt punct
        Date intrare: point - de tip Punct
        Date iesire: distanta - de tip Float
        """
        x1 = self.getX()
        y1 = self.getY()
        x2 = point.getX()
        y2 = point.getY()
        return math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
    
    def isInteger(self):
        if self.getX() == int(self.getX()) and self.getY() == int(self.getY()):
            return True
        return False
    
    def equalPoints(self, point):
        if self.getX() == point.getX() and self.getY() == point.getY():
            return True
        return False
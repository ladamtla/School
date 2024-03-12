class Pont:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Teglalap:
    def __init__(self, csucs1: Pont, csucs2: Pont):
        self.csucs1 = csucs1
        self.csucs2 = csucs2
        self.szel = abs(csucs2.x - csucs1.x)
        self.mag = abs(csucs2.y - csucs1.y)

    def terulet(self):
        return self.szel * self.mag

    def kerulet(self):
        return 2 * (self.szel + self.mag)

    def __str__(self):
        return f"Téglalap csúcsai: ({self.csucs1.x}, {self.csucs1.y}) és ({self.csucs2.x}, {self.csucs2.y}), szélessége: {self.szel}, magassága: {self.mag}"

c1 = Pont(0,0)
c2 = Pont(5, 5)
tl = Teglalap(c1, c2)

print(tl)
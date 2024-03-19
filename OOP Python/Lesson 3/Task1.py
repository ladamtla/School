class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x
    def get_y(self):
        return self.__y

    def __eq__(self, other):
        if self.__x == other.__x and self.__y == other.__y:
            return True
        else:
            return False

    def __del__(self):
        print('Pont törölve')



    def __str__(self):
        return "(" + str(self.__x) + "," + str(self.__y) + ")"

class Rectangle:
    def __init__(self, point1: Point, point2: Point):
        self.__point1 = point1
        self.__point2 = point2
        self.__width = abs(point2.get_x() - point1.get_x())
        self.__height = abs(point2.get_y() - point1.get_y())

    def __str__(self):
        return f"Csúcs1: {self.__point1.__str__()} Csúcs2: {self.__point2.__str__()} Szélessége: {self.__width} Magassága: {self.__height}"

    def __eq__(self, other):
        if self.__point1 == other.__point1 and self.__point2 == other.__point2:
            return True
        else:
            return False

    def __del__(self):
        print('Téglalap törölve')

    @property
    def perimeter(self):
        return self.__width*2+self.__height*2

    @property
    def area(self):
        return self.__width*self.__height



p1 = Point(0,0)
p2 = Point(5, 5)
p3 = Point(10, 10)
tl1 = Rectangle(p1, p2)
tl2 = Rectangle(p1, p3)

print(f"Pont1: {p1}")
print(f"Pont2: {p2}")
print(f"Pont3: {p3}")
print(f"Pont1 ugyanaz, mint Pont2? {p1==p2}")
print(f"Téglalap1: {tl1}, Területe: {tl1.perimeter}, Kerülete: {tl1.area}")
print(f"Téglalap2: {tl2}, Területe: {tl2.perimeter}, Kerülete: {tl2.area}")
print(f"Téglalap1 ugyanaz, mint Téglalap2? {tl1==tl2}")
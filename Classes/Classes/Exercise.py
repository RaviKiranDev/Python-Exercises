
#1. Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.
import math
class Circle:
    def __init__(self, radius):
        self.radius=radius

    def AreaOfCircle(self):
        area = float(math.pi*(self.radius **2))
        return area

if __name__ == '__main__':
    r=Circle(10)
    print(r.AreaOfCircle())







#2. Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

import math
class Rectangle:
    def __init__(self, length, width):
        self.length=length
        self.width=width

    def AreaOfRectangle(self):
        area = float(self.length * self.width)
        return area

if __name__ == '__main__':
    r=Rectangle(10, 12)
    print(r.AreaOfRectangle())

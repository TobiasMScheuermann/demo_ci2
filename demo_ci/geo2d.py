from math import sqrt


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        # Using Heron's formula
        s = (self.a + self.b + self.c) / 2
        return sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


if __name__ == "__main__":
    rect = Rectangle(5, 3)
    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())

    tri = Triangle(3, 4, 5)
    print("Triangle area:", tri.area())
    print("Triangle perimeter:", tri.perimeter())

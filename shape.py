from abc import abstractmethod


class Shape:
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a ** 2 * 3.14


rect = Rectangle(int(input("A: ")), int(input("B: ")))
circle = Circle(int(input("Radius: ")))

print(f"Area rect: {rect.area()}")
print(f"Area circle: {circle.area()}")
from math import pi

class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        super().__init__(name)
        self.length = length
        self.width = width

    # member method
    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, name, radius) -> None:
        super().__init__(name)
        self.radius = radius

    def area(self):
        return pi * self.radius * self.radius

# Create instances of the shapes
rectangle = Rectangle('Rectangle', 10, 10)
circle = Circle('Circle', 1)

# Print the areas of the shapes
print(f'{rectangle.name} area: {rectangle.area()}')
print(f'{circle.name} area: {circle.area()}')

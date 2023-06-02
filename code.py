class Rectangle():
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area
    
    def get_perimeter(self):
        perimeter = 2 * (self.width + self.length)
        return perimeter
    
    def vertical_orientation(self):
        if self.width > self.length:
            return True
        else:
            return False

length = float(input('Enter the Length of a Rectangle: '))
width = float(input('Enter the Width of a Rectangle: '))

rectangle = Rectangle(length, width)

print("Area:", rectangle.get_area())
print("Perimeter:", rectangle.get_perimeter())
print("Is vertically oriented?", rectangle.vertical_orientation())

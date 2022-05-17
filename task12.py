from math import sqrt


class Circle:
    def __init__(self):
        self.p1 = float(input('circle radius'))
    def perimeter(self):
        pi = 3.14159265359
        return float(2 * pi * self.p1)

    def area(self):
        pi = 3.14159265359
        return float(pi * (self.p1 ** 2))

class Rectangle:
    def __init__(self):
        self.p1 = float(input('sideA'))
        self.p2 = float(input('sideB'))
    def perimeter(self):
        return (self.p1 + self.p2) * 2
    def area(self):
        return (self.p1 * self.p2)


class Triangle:
    def __init__(self):
        self.p1 = float(input('sideA'))
        self.p2 = float(input('sideB'))
        self.p3 = float(input('sideC'))
    def perimeter(self):
        return float(self.p1 + self.p2 + self.p3)
    def area(self):
        s = ((self.p1 + self.p2 + self.p3)/2)
        return float((s*(s - self.p1) * (s - self.p2) * (s - self.p3)) ** 0.5)

class Trapezium:
    def __init__(self):
        self.p1 = float(input('sideA'))
        self.p2 = float(input('sideB'))
        self.p3 = float(input('sideC'))
    def perimeter(self):
        return (self.p2 + self.p3 + 2 * sqrt (sqrt (self.p1) + sqrt (self.p2 - self.p3)/4 ))
    def area(self):
        return float(((self.p2 + self.p3)/2) * self.p1)



print('Выберите тип фигуры')
print('1 Круг')
print('2 Прямоугольник')
print('3 Треугольник')
print('4 Трапеция')
a = int(input(''))
if a == 1:
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj = Circle()
    if b == 2:
        obj = Rectangle()
    if b == 3:
        obj = Triangle()
    if b == 4:
        obj = Trapezium()
    print(obj.area())

if a == 1:
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj = Circle()
    if b == 2:
        obj = Rectangle()
    if b == 3:
        obj = Triangle()
    if b == 4:
        obj = Trapezium()
    print(obj.perimeter())



if a == 3:
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj = Circle()
    if b == 2:
        obj = Rectangle()
    if b == 3:
        obj = Triangle()
    if b == 4:
        obj = Trapezium()
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj1 = Circle()
    if b == 2:
        obj1 = Rectangle()
    if b == 3:
        obj1 = Triangle()
    if b == 4:
        obj1 = Trapezium()
    if obj.perimeter() > obj1.perimeter():
        print('первая фигура > вторая фигура')
    else:
        print('вторая фигура > первая фигура')

if a == 4:
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj = Circle()
    if b == 2:
        obj = Rectangle()
    if b == 3:
        obj = Triangle()
    if b == 4:
        obj = Trapezium()
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj1 = Circle()
    if b == 2:
        obj1 = Rectangle()
    if b == 3:
        obj1 = Triangle()
    if b == 4:
        obj1 = Trapezium()
    print('сума фигуры 1 + сума фигуры 2')
    print(obj.area() + obj1.area())


if a == 5:
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj = Circle()
    if b == 2:
        obj = Rectangle()
    if b == 3:
        obj = Triangle()
    if b == 4:
        obj = Trapezium()
    print('Выберите тип фигуры')
    print('1 Круг')
    print('2 Прямоугольник')
    print('3 Треугольник')
    print('4 Трапеция')
    b = int(input(''))
    if b == 1:
        obj1 = Circle()
    if b == 2:
        obj1 = Rectangle()
    if b == 3:
        obj1 = Triangle()
    if b == 4:
        obj1 = Trapezium()
    print('Разница фигур')
    s = float(obj.area() - obj1.area())
    if s > 0:
        print(obj.area() - obj1.area())
    if s < 0:
        print(obj1.area() - obj.area())
    s = float(obj.area() - obj1.area())
    if s > 0:
        print(obj.area() - obj1.area())
    if s < 0:
        print(obj1.area() - obj.area())









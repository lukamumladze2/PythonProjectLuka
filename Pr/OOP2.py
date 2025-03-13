class Shape:
    def __init__(self, color):
        self.color = color

    def say_hi(self):
        print(f'I am a shape with {self.color} color')

class Quadrangle(Shape):
    def say_hi(self):
        print(f'I am a quadrangle with {self.color} color')

class Triangle(Shape):
    def __init__(self, a, b, c, color):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c
    def say_hi(self):
        print(f'I am a triangle with {self.color} color')

class Square(Quadrangle):
    def __init__(self, a, color):
        self.a = a
        Shape.__init__(self, color)


s1 = Shape('red')
s1.say_hi()
q1 = Quadrangle('blue')
q1.say_hi()
t1 = Triangle("yellow")
t1.say_hi()
# class Rectangle:
#     """ეს კლასი არის მართკუთხედებისთვის"""
#
#     def __init__(self, width, length, color):
#         self.width = width
#         self.length = length
#         self.color = color
#
#     def perimeter(self):
#         perimeter = self.width * 2 + self.length * 2
#         return perimeter
#
# rectangle1 = Rectangle(1, 2, "red")
# rectangle2 = Rectangle(12, 12, "blue")
# # print(type(rectangle1))
# # print(rectangle1.color) # width, length
#
# print(rectangle1.perimeter())
# print(rectangle2.perimeter())
from binascii import a2b_qp

# class Rectangle:
#    ''' Docstring text here'''
#
#    def __init__(self, width, length):
#        self.width = width
#        self.length = length
#
#    def perimeter(self):
#        return 2 * (self.width + self.length)
#
#    def area(self):
#        return self.width * self.length
#
#    def length_cubed(self):
#        return self.length ** 3
#
# obj1 = Rectangle(4, 5)
#
# print(obj1.area())
# print(obj1.length_cubed())



# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
# location1 = Point(2,6)
# print(location1)
#
#
# class Student:
#    def __init__(self, firstname, lastname):
#        self.firstname = firstname
#        self.lastname = lastname
#
#    def get_name(self):
#        return self.firstname
#
#    def set_name(self, text):
#        self.firstname = text
#
#    def get_lastname(self):
#        return self.lastname
#
#    def set_lastname(self, text):
#        self.lastname = text
#
# st1 = Student("Giorgi", "Abashidze")
#
# st1.set_lastname("asfdfsdg")
# print(st1.get_lastname())
#
#
# class Rectangle:
#
#     def __init__(self, width, length, color):
#         self.width = width
#         self.length = length
#         self.color = color
#
#     def perimeter(self):
#         return 2 * (self.width + self.length)
#
#     def area(self):
#         return self.width * self.length
#
#
# obj1 = Rectangle(15, 16, "red")
#
# print(obj1.perimeter())
# print(obj1.area())

# class Car:
#
#     def __init__(self, color, model, makeYear, fuelType):
#         self.color = color
#         self.model = model
#         self.makeYear = makeYear
#         self.fuelType = fuelType
#
#
#     def __str__(self):
#         return f"your car is {self.color} {self.model} made in {self.makeYear} which uses {self.fuelType}"
#
#
# car1 = Car("red", "Mercedes", 2015, "Gas" )
# car2 = Car("blue", "BMW", 2013, "Gas" )
# car2 = Car("orange", "Audi", 2009, "Diesel" )


# class Celsius:
#
#     def __init__(self, temperature):
#         self.__temperature = temperature
#
#     def get_temp(self):
#         return self.__temperature
#
#     def set_temp(self, text):
#         self.__temperature = text
#
#     def del_temp(self):
#         del self.__temperature
#
#     temperature = property(get_temp, set_temp, del_temp)
#
#
# obj1 = Celsius(16)
# obj2 = Celsius(32)
# print(obj1.temperature)
# obj1.temperature = 18
# print(obj1.temperature)


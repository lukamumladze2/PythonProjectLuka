# #1
# class Fraction:
#
#     def __init__(self, top, bottom):
#         self.top, self.bottom = top, bottom
#
#     def __str__(self):
#         return f"თქვენი წილადია {self.top}/{self.bottom}"
#
#     def addition(self):
#         if wiladi1.bottom == wiladi2.bottom:
#             return f"{wiladi1.top + wiladi2.top}/{wiladi1.bottom}"
#         else:
#             return "წილადის შეკრება შეუძლებელია რადგან მათი მნისშვნელები ერთმანეთს არ უდრის"
#
#     def inverse(self):
#         return f"{self.bottom}/{self.top}"
#
#
# wiladi1 = Fraction(1, 4)
# wiladi2 = Fraction(2, 4)
# print(wiladi1)
#
# result = wiladi1.addition()
# print(f"თქვენი წილადების ჯამია {result}")
# print(f"თქვენი შებრუნებული წილადია {wiladi1.inverse()}")
#
#
# #2
# import math
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def length(self):
#         return math.sqrt((0- self.x)^2 + (0 - self.y)^2)
#
# point1 = Point(3, 5)
# point2 = Point(6, 9)
#
# print(f"პირველი წერტილის სიგრძე ცენტრიდან: {point1.length()}")
# print(f"მეორე წერტილისის სიგრძე ცენტრიდან: {point2.length()}")
#
#
# #3
# import math
#
# class Point:
#
#     def __init__(self, x, y):
#         self.x, self.y = x, y
#
#     def __str__(self):
#         return f"({self.x},{self.y})"
#
#     def length(self):
#         return math.sqrt((point_b.x - point_a.x)**2 + (point_b.y - point_a.y)**2)
#
# x1 = int(input("შემოიყვანეთ a წერტილის კოორდინატები:\nx: "))
# y1 = int(input("y: "))
# point_a = Point(x1, y1)
#
# x2 = int(input("შემოიყვანეთ b წერტილის კოორდინატები:\nx: "))
# y2 = int(input("y: "))
# point_b = Point(x2, y2)
#
# result = point_a
#
# print(f"მანძილი a წერტილიდან b წერტილამდე არის: {result.length()}")
#1
from math import *
x = float(input('insert a number '))

rounded = round(x, 1)
ceil = ceil(x)
floor = floor(x)
trunc = trunc(x)

print(f"rounded number is {rounded}")
print(f"ceil number is {ceil}")
print(f"floor number is {floor}")
print(f"trunc number is {trunc}")

#2
from math import pow

x = pow(3, 8)
y = pow(2, 9)
z = pow(4, 6)

print(f"3⁸ is {x}")
print(f"2⁹ is {y}")
print(f"4⁶ is {z}")

#3
from math import sqrt

x = sqrt(225625)
y = sqrt(4225)

print(f"√225625 is {x}")
print(f"√4225 is {y}")

#4
from random import random

x = random()
x = round(x, 3)
print(x)

#5
from random import uniform

x = uniform(100, 120)
x = round(x, 1)
print(x)

#6
from random import randint

for i in range(10):
    print(randint(1, 100))
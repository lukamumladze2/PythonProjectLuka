#1
for i in range(400, 100, -1):
    if i % 9 == 0:
        print(i)

#2
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0,]
print(numbers[-1])

#3
def cube_list(numbers):
    cubed = []
    for i in numbers:
        cubed.append(i**3)
    return cubed

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(cube_list(numbers))

#4



#5
def favourite_fruit(fruits, fav_fruit):
    if fav_fruit in fruits:
        return fruits.index(fav_fruit)
    else:
        return "your favorite fruit is not in the list."

fruits = ['apple', 'banana', 'orange', 'grapes']

fav_fruit = input("what is your favorite fruit? ")


print(favourite_fruit(fruits, fav_fruit))


#bonus
#1
def full_list(odd_numbers, even_numbers):
    full_list = odd_numbers + even_numbers
    full_list.sort()
    return full_list

odd_numbers = [1, 3, 5, 7, 9]
even_numbers = [2, 4, 6, 8, 10]

print(full_list(odd_numbers, even_numbers))

#2
# "def" keyword გამოიყენება ფუნქციის შესაქმნელად

#3
# რიცხვის ასახარისხებლად ვიყენებთ pow-ს math მოდულიდან

from math import pow
a = pow(4, 5)
print(a)



#1
cubes_tuple = tuple(x**3 for x in range(5, 100, 5))

print(cubes_tuple)

print(len(cubes_tuple))

#2
cubes_tuple = tuple(x**3 for x in range(5, 100, 5))

cubes_iterator = iter(cubes_tuple)

while True:
    try:
        print(next(cubes_iterator))
    except StopIteration:
        break
#3
cubes_set = {x**3 for x in range(5, 101, 5)}

print(cubes_set)

cubes_sum = sum(cubes_set)
cubes_len = len(cubes_set)

cubes_average = cubes_sum / cubes_len

print(cubes_average)

#4
cubes_set = {x**3 for x in range(5, 101, 5)}

cubes_iterator = iter(cubes_set)

while True:
    try:
        print(next(cubes_iterator))
    except StopIteration:
        break

cubes_sum = sum(cubes_set)
cubes_len = len(cubes_set)

cubes_average = cubes_sum / cubes_len

print(cubes_average)

#5
def my_generator():
    for i in range(1, 5):
        yield i

my_iterator = my_generator()

while True:
    try:
        print(next(my_iterator))
    except StopIteration:
        break
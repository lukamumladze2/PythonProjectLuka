#2
from operator import invert

person = {"name": "Walter White", "age": 50, "city": "Albuquerque", "occupation": "Chemistry teacher"}
print(person)

#3
person = {"name": "Walter White", "age": 50, "city": "Albuquerque", "occupation": "Chemistry teacher"}
person.update({"hobby": "eating and sleep"})
print(person)

#4
def merge_dictionaries(dic1, dic2):
    merged_dict = dic1.copy()
    merged_dict.update(dic2)
    return merged_dict

dic1 = {1: 2, 3: 4, 5: 6}
dic2 = {7: 8, 9: 10, 11: 12}

print(merge_dictionaries(dic1, dic2))

#5

#6
nums = [1, 2, 3, 4, 5]

cubed_dict = {}

for i in nums:
    cubed_dict[i] = i ** 3

print(cubed_dict)

#8
def invert_dictionary(input_dict):
    invert_list = list(input_dict.items())
    invert_list.reverse()
    inverted_dict = dict(invert_list)
    return inverted_dict

input_dict = {1: 2, 3: 4, 5: 6}
print(invert_dictionary(input_dict))




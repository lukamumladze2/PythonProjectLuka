#1
def str_length(string_list):
    length = []
    for string in string_list:
        length.append(len(string))
    return length

string_list = ["gamarjoba","saxli","manqana"]
print(str_length(string_list))

#2
def unique(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    unique1 = set1 - set2
    unique2 = set2 - set1
    unique_elements = unique1.union(unique2)
    list(unique_elements)
    return unique_elements

list1 = [2, 4, 5, 7, 8]
list2 = [4, 5, 7, 9, 10]
print(unique(list1, list2))

#3
def person_info(person):
    print(f"{person[0]}: {person[1]}")

data = [("John", 52), ("Dean", 26), ("Sam", 22)]

for name, age in data:
    person = (name, age)
    person_info(person)

#4
def is_enough(products):
    results = []
    for product_name, quantity in products.items():
        if quantity > 5:
            results.append((product_name ,"enough"))
        else:
            results.append((product_name, "not enough"))
    return tuple(results)

products = {"apple": 4, "banana": 6, "strawberry": 7, "carrot": 2, "cucumber": 3}
print(is_enough(products))

#5
def words_a(word_list):
    a_words = {}
    for word in word_list:
        if word[0] == "a":
            a_words[word] = len(word)
    return a_words

word_list = ["apple", "arrow", "house", "car", "account"]
print(words_a(word_list))

#Bonus
#6
"""
pop, discard, remove
"""
#7
"""
თაფლი უფრო დაცულია და მისი შეცვლა არ შეგვიძლია
"""
#8
"""
union, intersection, difference, symmetric difference
"""
#9
"""
"""
#10
"""
items
"""
#11
"""
*args
"""
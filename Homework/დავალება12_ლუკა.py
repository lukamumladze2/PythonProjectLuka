# # 1
# dict1 = {0: 10, 1: 20}
#
# dict1.update({2: 3, 4: 5})
#
# print(f"ახალი ლექსიკონია {dict1}")
#
# del dict1[4]
#
# print(f"ლექსიკონი წაშლის შემდეგ {dict1}")
#
# # 2
# dic1 = {1: 10, 2: 20}
# dic2 = {3: 30, 4: 40}
# dic3 = {5: 50, 6: 60}
#
# dic1.update(dic2)
# dic1.update(dic2)
#
# print(dic1)
#
# # 3
# d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
#
# key_check = int(input("ჩაწერეთ რომელი გასახების შემოწმება გსურთ: "))
#
# if key_check in d:
#     print(f"გასაღები {key_check} არის ლექსიკონში.")
# else:
#     print(f"გასაღები {key_check} არ არის ლექსიკონში.")
#
# # 4
# d = {'x': 10, 'y': 20, 'z': 30}
#
# for key in d:
#     print(f"{key} -> {d[key]}")

# # 5
# cubes_dict = {}
#
# for i in range(1, 11):
#     cubes_dict[i] = pow(i, 3)
#
# print(cubes_dict)

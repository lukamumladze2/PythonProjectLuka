# #1
# numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# print('ჯამი', sum(numbs))
# print('მაქსიმალური', max(numbs))
# print('მინიმალური', min(numbs))
# print('საშუალო', sum(numbs)//len(numbs))
#
# #2
# numbs = [1, 2, 205, 3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 102]
# numbs.sort()
# print(numbs)
#
# #3
# list = []
#
# for i in range(10):
#     a = input('შემოიყვანეთ მონაცემი: ')
#     list.append(a)
#
# print('list', list)
#
# #4
# list = []
#
# if len(list) == 0:
#     print('სია ცარიელია')
# else:
#     print('სია არ არის ცარიელი')
#
# #5
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
#
# even_numbers = []
#
# for i in list:
#     if i % 2 == 0:
#         even_numbers.append(i)
#
# print(even_numbers)
#
# #6
# list = [1, 5, 0, 1, 3, 4, 5, 5, 9, 2, 4, 6, 3, 7, 8]
#
# output_list = []
#
# for i in list:
#     if list.count(i) == 1:
#         output_list.append(i)
#
# output_list.sort()
# print(output_list)

#ბონუს დავალება
# num = []
#
# a = input('შემოიყვანეთ რიცხვი:' )
# num.append(a)
#
# print(len(num[0]))
#
# num = str(num[0])
#
# reversed_num = ""
#
# while num:
#     reversed_num += num[-1]
#     num = num[:-1]
#
# print(reversed_num)
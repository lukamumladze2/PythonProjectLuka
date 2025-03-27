# list = [4, 5, 6, 7, 3, 5, 3, 1]
# iter_list = iter(list)
# try:
#     for i in range(9):
#         print(next(iter_list))
#
# except StopIteration:
#     rint("StopIteration error")p

# def content_to_another_file(input_file, output_file):
#     try:
#         with open(input_file, "r", encoding="utf-8") as infile:
#             lines = infile.readlines()
#         joined_content = " ".join([line.strip() for line in lines])
#
#         with open(output_file, "w", encoding="utf-8") as outfile:
#             outfile.write(joined_content)
#         return "Copying content to another file was successful!"
#     except FileNotFoundError as error_message:
#         return error_message
#     except Exception as e:
#         return e
#
# in_file = "food.txt"
# out_file = "food2.txt"
# print(content_to_another_file(in_file, out_file))

# joined_content = " ".join([line.strip() for line in lines])

# def multiples_of_five():
#     num = 5
#     while True:
#         yield num
#         num += 5
#
# iterator = multiples_of_five()
#
# count = 0
# while count < 10:
#     print(next(iterator))
#     count += 1

# list = [i ** 3 for i in range(1, 100) if i % 5 == 0]
# print(list)
# print(f"maximum number {max(list)}")

def number_generator():
    yield [1, 2, 3, 4, 5]
iterator = iter(number_generator())
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
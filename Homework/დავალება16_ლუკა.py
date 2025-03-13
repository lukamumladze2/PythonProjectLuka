#1
while True:
    try:
        num1 = float(input("შემოიყვანეთ პირველი რიცხვი: "))
        num2 = float(input("შემოიყვანეთ მეორე რიცხვი: "))
        if num2 == 0:
            print("Error: 0-ზე გაყოფა არ შეიძლება")
        else:
            result = num1 / num2
            print("პასუხი:", result)
            break
    except ValueError:
        print("Error: არასწორი მონაცემი, სცადეთ თავიდან")
from ast import Index

#2
def divide_numbers(num1, num2):
  try:
    if num2 == 0:
      return "0-ზე გაყოფა არ შეიძლება"
    else:
      return num1 / num2
  except TypeError:
    return "არასწორი მონაცემი, შეიყვანეთ მხოლოდ რიცხვები"

print(divide_numbers(10, 2))

#3
list = [1, 2, 3, 4]

try:
    print(list[5])
except IndexError:
    print('index is out of range')

#4
try:
    file = open("myresult.txt", "r")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("The file myresult.txt does not exist.")



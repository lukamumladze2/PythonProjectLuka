
#1
number = 2
while number <= 1000:
    is_prime = True
    i = 2
    while i <= number // 2:
        if number % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(number)
    number += 1

#2

#3
number = int(input("შეიყვანეთ მთელი რიცხვი: "))
count = 0
number = abs(number)

if number == 0:
    count = 1

while number > 0:
    number //= 10
    count += 1

print(f"ციფრთა რაოდენობა: {count}")

#4
number = int(input("შეიყვანეთ მთელი რიცხვი: "))
total = 0
number = abs(number)

while number > 0:
    total += number % 10
    number //= 10

print(f"ციფრების ჯამი: {total}")

#5
number = int(input("შეიყვანეთ მთელი რიცხვი: "))
number = abs(number)

while number >= 10:
    number //= 10

print(f"პირველი ციფრი: {number}")

#ბონუს დავალება
num = []

for i in range(1):
    a = input('შემოიყვანეთ რიცხვი:' )
    num.append(a)

print(len(num[0]))

num = str(num[0])

reversed_num = ""

while num:
    reversed_num += num[-1]
    num = num[:-1]

print(reversed_num)
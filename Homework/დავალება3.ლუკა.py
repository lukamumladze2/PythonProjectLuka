
#1
length = 8
width = 5
perimeter = (length*2) + (width*2)
print(perimeter)

#2
a = int(input("შეიყვანეთ რიცხვი: "))

if a <= 1:
    print("არაა მარტივი რიცხვი")
else:
    b = 2
    c = 1

    while b * b <= a:
        if a % b == 0:
            c = 0
            break
        b += 1

    if c == 1:
        print("მარტივი რიცხვია")
    else:
        print("არაა მარტივი რიცხვი")

#3
a = 0
b = 0

while a < 20:
    b += a * 2 + 2
    a += 1

print(b)


#4
a = 1
while a < 101:
    if a % 5 == 0:
        break
    print(a)
    a += 1

#5
for a in range(1, 31):
    if a % 2 == 1:
        continue
    print(a)

#6
a = int(input('შემოიყვანეთ პირველი რიცხვი '))
b = int(input('შემოიყვანეთ მეორე რიცხვი '))
if b > a:
    print(b, 'არის მაქსიმუმი')
else:
    print(a, 'არის მაქსიმუმი')
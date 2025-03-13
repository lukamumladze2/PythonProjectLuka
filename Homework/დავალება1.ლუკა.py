# დავალება 3

#1
x = int(input('Put in number '))
if x > 0:
    print('Number is positive')

#2
x = int(input('ჩაწერეთ რიცხვი '))
if x % 10 == 0:
    print('რიცხვი არის 10-ჯერადი ')
else:
    print('რიცხვი არ ბოლოცდება 0-ით')

#3
x = int(input('ჩაწერეთ პირველი რიცხვი '))
y = int(input('ჩაწერეთ მეორე რიცხვი '))

if x > 10 and y > 10:
    print((x+y)/2)
else:
    print(x*y)

#4
x = int(input('Put in number '))
if x > 0:
    print('Number is positive')
elif x < 0:
    print('Number is negative')
else:
    print('Number is equal to zero')
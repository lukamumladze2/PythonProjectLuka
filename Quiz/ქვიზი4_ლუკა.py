with open("titanic.txt", "r") as f:
    lines = f.readlines()

headers = lines[0].strip().split(",")
gender_index = headers.index("Sex")
survived_index = headers.index("Survived")
ticket_index = headers.index("Pclass")
fare_index = headers.index("Fare")

female_count = 0

for line in lines:
    i = line.strip().split(",")
    if i[gender_index] == "female":
        female_count += 1

f_percentage = female_count / (len(lines) - 1) * 100

male_count = 0

for line in lines:
    i = line.strip().split(",")
    if i[gender_index] == "male":
        male_count += 1

m_percentage = male_count / (len(lines) - 1) * 100

female_survivors = 0

for line in lines:
    i = line.strip().split(",")
    if i[gender_index] == "female" and i[survived_index] == "1":
        female_survivors += 1

dead_females = female_count - female_survivors

male_survivors = 0

for line in lines:
    i = line.strip().split(",")
    if i[gender_index] == "male" and i[survived_index] == "1":
        male_survivors += 1

dead_males = male_count - male_survivors

first_class_ticket = 0
second_class_ticket = 0
third_class_ticket = 0

for line in lines:
    i = line.strip().split(",")
    if i[ticket_index] == "1":
        first_class_ticket += 1
    elif i[ticket_index] == "2":
        second_class_ticket += 1
    else:
        third_class_ticket += 1

first_class_ticket_percentage = first_class_ticket / (len(lines) - 1) * 100
second_class_ticket_percentage = second_class_ticket / (len(lines) - 1) * 100
third_class_ticket_percentage = third_class_ticket / (len(lines) - 1) * 100

total_fare = 0
total_tickets = first_class_ticket + second_class_ticket + third_class_ticket

for line in lines[1:]:
    i = line.strip().split(",")
    fare = float(i[fare_index])
    total_fare += fare

average_fare = total_fare / total_tickets
fare_per_ticket = average_fare / total_tickets

first_class_fare = first_class_ticket * fare_per_ticket
second_class_fare = second_class_ticket * fare_per_ticket
third_class_fare = third_class_ticket * fare_per_ticket

dict = {
    "passengers_amount":
    {
        "females" : female_count,
        "males" : male_count,
        "females_%" : f_percentage,
        "males_%" : m_percentage,
    },

    "passengers_survived":
    {
        "females" : female_survivors,
        "males" : male_survivors,
        "dead_females" : dead_females,
        "dead_males" : dead_males,
    },

    "ticket_class":
    {
         "first class ticket" : first_class_ticket,
         "second class ticket" : second_class_ticket,
         "third class ticket" : third_class_ticket,
         "first class ticket_%" : first_class_ticket_percentage,
         "second class ticket_%" : second_class_ticket_percentage,
         "third class ticket_%" : third_class_ticket_percentage,
    },

    "average_fare":
    {
        "first class fare" : first_class_fare,
        "second class fare" : second_class_fare,
        "third class fare" : third_class_fare,
    }
}
print(dict)



#2
class Ticket:
    def __init__(self, film_name, ticket_price, ticket_amount, language="Geo"):
        self.film_name = film_name
        self.ticket_price = ticket_price
        self.ticket_amount = ticket_amount
        self.language = language

    def __str__(self):
        return f"film name: {self.film_name}, ticket price: {self.ticket_price}, ticket amount: {self.ticket_amount}, language: {self.language}"


class User:
    def __init__(self, username, balance):
        self.username = username
        self.balance = balance

    def __str__(self):
        return f"user name: {self.username}, money on balance: {self.balance}"

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def purchase(self, ticket, amount):
        if ticket.ticket_price * amount > self.balance:
            return "you dont have enough money"
        elif ticket.ticket_amount < amount:
            return "we dont have enough tickets"
        else:
            self.balance -= ticket.ticket_price * amount
            ticket.ticket_amount -= amount
            return "you have successfully bought tickets"

cinema = Ticket("Titanic", 16, 50, "English")
user = User("Luka", 50)
user.deposit(70)
print(user.purchase(cinema, 5))



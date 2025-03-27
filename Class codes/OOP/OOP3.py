class Bank_Account:
    def __init__(self, account_name, balance=0):
        self.__account_name = account_name
        self.__balance = balance

    def get_acc_name(self):
        return self.__account_name

    def set_acc_name(self, text):
        self.__account_name = text

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance + amount

    def get_balance(self):
        return self.__balance


name = input("შეიტანეთ კლიენტის სახელი და გვარი: ")
account = Bank_Account(name)

balance = int(input("რა თანხა გაქვთ ამჟამად ანგარიშზე? "))
account.deposit(balance)

operation_choose = int(input("აირჩიეთ შესაბამისი კოდი რომელი ოპერაციის შესრულებაც გსურთ: "
                             "თანხის შეტანა: 1, თანხის გამოტანა: 2: "))

if operation_choose == 1:
    money_deposit = int(input("რა თანხის შეტანა გსურთ: "))
    account.deposit(money_deposit)
    print(f"ახალი ბალანსი: {account.get_balance()}")
elif operation_choose == 2:
    money_withdraw = int(input("რა თანხის გამოტანა გსურთ: "))
    account.withdraw(money_withdraw)
    print(f"თანხის შეტანა შესრულებულია. ანჟამად თქვენ გაქვს {account.get_balance()} ლარი")

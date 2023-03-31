class User():
    def __init__(self,name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def show_details(self):
        print("Personal details are below")
        print("")
        print("Name ", self.name)
        print("Age ", self.age)
        print("Gender ", self.gender)


class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 100

    def deposit(self):
        self.amount = int(input("enter amount: "))
        self.balance += self.amount
        print("Account balamce is updated ", self.balance)

    def withdraw(self, amount):
        self.amount = amount
        if self.balance < self.amount:
            print("Insufficient balance: " , self.balance)
        else:
            self.balance -= amount
            print("Total amount now is ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Account balance is : ", self.balance)



josh = Bank("Josh", 21, "Male")
josh.view_balance()

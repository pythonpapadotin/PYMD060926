class BankAccount:
    # class attributes
    bank_name = "ABC Bank"
    total_accounts = 0

    # The function inside a class without any decorator like
    # classmethod or staticmethod will be a object method.
    # The first argument of object method will always point to the object.
    # self is the argument which everybody agreed to use it as the first argument
    # of the object method to make the code more read friendly in nature.
    # The first argument in a class method should always point to the class.
    # Similarly, cls is universally accepted class reference argument.
    def __init__(satya, name, balance):
        satya.name = name
        satya.balance = balance
        BankAccount.total_accounts += 1

    def deposit(mohit, amount):
        if BankAccount.is_valid_amount(amount):
            mohit.balance += amount

    # Class method
    @classmethod
    def change_bank_name(meenakshi, new_name):
        meenakshi.bank_name = new_name

    # Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # Magic method
    # They will be invoked in a special manner
    # Without __str__ override:- <__main__.BankAccount object at 0x100eccf40>
    # With below __str__ : Uday: ₹6000
    def __str__(self):
        return f"{self.name}: ₹{self.balance}"

    # to invoke this, just call len(obj)
    def __len__(self):
        return self.balance


# Creating objects
uday = BankAccount("Uday", 5000)
saurav = BankAccount("Saurav", 10000)

# Object method
uday.deposit(1000)

# Class method
# BankAccount.change_bank_name("XYZ Bank")
#
# print(BankAccount.bank_name)

# Static method
# print(BankAccount.is_valid_amount(500))  # True
# print(BankAccount.is_valid_amount(-10))  # False

# print(uday.is_valid_amount(5390))  # True

# Magic method: __str__ is called automatically by print()
# to get the object's string representation.
# x = str(uday)

print(uday)  # print function takes the str() value of whatever is passed to it.

# y = len(uday)

# print(x)

# print('y is', y)
#
# print(BankAccount.bank_name)
# print(BankAccount.total_accounts)

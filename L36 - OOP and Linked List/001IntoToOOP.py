# class Customer:
#     pass


# c = Customer()


class Customer:
    def __init__(self, name, age, gender, balance):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance

    def describe(self):
        info = f"{self.name} {self.age} {self.gender} {self.balance}"
        print(info)


c1 = Customer("Ramanujan", 32, "Male", 1749)
# print(c1.name, c1.age, c1.gender, c1.balance)
# print(c1.name)
# print(c1.age)
# print(c1.gender)
# print(c1.balance)
c1.describe()

c2 = Customer("Aryabhata", 74, "Male", 0)
# print(c2.name, c2.age, c2.gender, c2.balance)
c2.describe()

c3 = Customer("Bose", 51, "Male", 100)
# print(c3.name, c3.age, c3.gender, c3.balance)
c3.describe()

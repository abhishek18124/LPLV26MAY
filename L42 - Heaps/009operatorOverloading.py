class customer:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def __lt__(self, other):
        # self is reference to object on which this method is invoked, in our eg. it is a reference to c1
        # other is reference to the object which was passed as an arg during the fn call, in our eg. it is a reference to c2
        return self.age < other.age


c1 = customer("kohli", 38, 100)
c2 = customer("rohit", 35, 60)

if c1 < c2:  # c1.__lt__(c2)
    print(f"{c1.name} is younger than {c2.name}")
else:
    print(f"{c2.name} is younger than {c1.name}")

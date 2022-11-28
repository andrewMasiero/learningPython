class Person():
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent / 100))

    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)

    def giveRaise(self, percent, bonus=10):
        self.person.giveRaise(percent + bonus)

    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)


if __name__ == "__main__":
    # self-test code
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(10)
    print(sue)

    tom = Manager('Tome Jones', 50000)
    tom.giveRaise(10)
    print(tom.lastName())
    print(tom)

    print('--All three--')
    for obj in (bob, sue, tom):
        obj.giveRaise(10)
        print(obj)

    for i in range(0, 2):
        print()

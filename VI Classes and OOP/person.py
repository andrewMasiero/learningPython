"""
Record and process information about people.
Run this file directly to test its classes.
"""

from classtools import AttrDisplay  # use generic display tool


class Person(AttrDisplay):  # mix in a repr at this level
    """
    Create and process person records
    """

    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]

    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent / 100))


class Manager(Person):
    """
    A customized Person with special requirements
    """

    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)  # job name is implied

    def giveRaise(self, percent, bonus=10):
        Person.giveRaise(self, percent + bonus)


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

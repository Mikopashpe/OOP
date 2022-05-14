'''
В данном разделе создается класс, удовлетворяющий практически всем уловиям и составляющим создания классов ООП
'''

class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastname(self):
        return self.name.split()[-1]
    def giveraise(self, percent):
        self.pay = int(self.pay *(1+ percent))
    def __repr__(self):
        return f"Person: {self.name}, {self.pay}"


class Manager(Person):
    def __init__(self, name, pay):
        Person.__init__(self, name, 'mgr', pay)
    def giveraise(self, percent, bonus = .10):
        Person.giveraise(self, percent+ bonus)
    

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addmember(self, person):
        self.members.append(person)
    def giveraise(self, percent):
        for person in self.members:
            person.giveraise(percent)
    def showall(self):
        for person in self.members:
            print(person)


if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Johns', job = 'dev', pay = 10000)
    tom = Manager('Tom Jones', 50000)
    development = Department(bob, sue)
    development.addmember(tom)
    development.giveraise(.10)
    development.showall()



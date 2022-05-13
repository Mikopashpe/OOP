'''
 В данном разделе приведены примеры простого класса и более развитого, содержащего атрибуты и методы для наследования экземплярами класса
'''

class rec:
    pass

# Записи на основе экземпляров класса
pers1 = rec()
pers1.name = 'Bob'
pers1.job = ['dev', 'mgr']
pers1.age = 40.5

pers2 = rec()
pers2.name = 'Sue'
pers2.job = ['dev', 'cto']

print(pers1.name, pers2.job)

# Создание более развитого класса, включающего в себя данные и логику
class Person:
    def __init__(self, name, job, age = None):
        self.name = name
        self.job = job
        self.age = age
    def info(self):
        return (self.name, self.job)

# Вызовы конструктора
rec1 = Person('Bob', ['dev', 'mgr'], 40.5)
rec2 = Person('Sue', ['dev', 'cto'])

# Вызов атрибута
print(rec1.job)

# Вызов метода
print(rec2.info())


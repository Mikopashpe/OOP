'''
В данном разделе идет ознакомление с созданием классов, суперклассов, подклассов и наследованием атрибутов класса.
'''
# Создание класса First и его методов: setdata и display
class First:
    def setdata(self, value):
        self.data = value
    def display(self):
        print(self.data)

# Создание экземпляров класса First
x = First()
y = First()

# Вызов атрибутов класса у экземпляров класса
x.setdata('King Arthur')
y.setdata(3.14159)
x.display()
y.display()

# Создание подкласса Second. С этого момента класс First становится суперклассом.
class Second(First):
# Меняем метод display в рамках данного дочернего класса
    def display(self):
        print('My self is', self.data)

# При создании данного экземпляра подкласса ему доступны атрибуты суперкласса
z = Second()
z.setdata(44)
z.display()

# Создаем подкласс Third родительского класса Second. Методы, описанные в данном классе будут недоступны родительскому классу
class Third(Second):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return Third(self.data+other)
    def __str__(self):
        return 'Thirdclass: %s' % self.data
    def mul(self, other):
        self.data *= other

# Создание экземплятов класса и вывод операций перегрузки
a = Third('abc')
a.display()
print(a)
b = a +'xyz'
b.display()
print(b)
a.mul(3)
print(a)

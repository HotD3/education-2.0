class Person:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def hello(self):
        print(f'{self.name} says: Hello, i am {self.age} years old')
#if __name__ == '__main__':
Artur = Person('Artur', 27, 'male')
Dasha = Person("Dasha", 27, 'female')
print(Artur)
print(Dasha)
Artur.hello()
Dasha.hello()
print(Dasha.sex)
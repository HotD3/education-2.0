class Person:       #создание нового класса
    def __init__(self, name, surname, birth, how_old):  #создание метода __init__ c полями name, surname etc.
        self.name = name
        self.surname = surname
        self.birth = birth
        self.how_old = how_old
    def my_func(self):   #создание метода, с помощью которого будет выводиться сообзение с приветствием
        print(f"{self.name}, where you from? - i am from {self.birth}")
    def nationality_check(self):  #метод, который определяет, соответствует ли поле birth заданному
        if self.birth == 'Ukraine':
            print('He is Ukrainian') #выводит сообщение, если соответсвует
        else:
            print('Not ukrainian')  #выводит сообщение, если не соответствует
    def year_of_birth(self):  #метод для определения года рождения
        import datetime   #импорт библиотеки 
        current_year = datetime.datetime.now().year  #создание переменной current_year, которая будет показывать текущий год
        print(f"Year of birth is {current_year - self.how_old}")  #вывод сообщения с годом рождения. Текущий год отнимается от года рождения
Artur = Person('Artur', 'Buhil', 'Ukraine', 27)  #создание экземпляра Artur, принадлежащего классу Person
Artur.my_func()
Artur.nationality_check()
Dasha = Person('Dasha', 'Bohdan', 'Ukraina', 27) #создание экземпляра Dasha, принадлежащего классу Person
Dasha.my_func()
Dasha.nationality_check()
Artur.year_of_birth()
    
# p1 = Person()
# p1.name = "Artur"
# p1.surname = "Buhil"
# p1.birth = "Ukraine"

# p2 = Person()
# p2.name = "Dasha"
# p2.surname = "Bohdan"
# p2.birth = "Ukraine"

# print(p1.name)
# print(f"{p1.name} {p1.surname}")
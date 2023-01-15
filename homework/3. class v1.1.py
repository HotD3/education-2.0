class Nikolay():
    def __init__(self, name):
        self.name = name
    def check_name(self):
        n = self.name
        check_n = n.split()
        num_check = len(check_n)
        new_name = self.name.replace(" ", '')
        if self.name.replace(' ', '') == 'Nikolay':
            print(f"Your name correct,{self.name}")
        elif self.name == 'Nikola':
            print(f'Your name correct,{self.name}')
        elif self.name == 'Kolya':
            print(f'Your name correct,{self.name}')
        # elif num_check ==1:
        #     #    print('Length is correct')
            pass
        else:
            # new_name = self.name.replace(" ", '')
            print(f"Your name {self.name} replaced to {new_name}")
            print(f"I am not {new_name}, i am Nikolay")
            self.name = 'Nikolay'
__version__ = '1.1'
name4 = Nikolay('Artur')
name4.check_name()
name1 = Nikolay('Nikola')
name1.check_name()
name2 = Nikolay('Nikolay')
name2.check_name()
name3 = Nikolay("Artur Alexandrovich")
name3.check_name()
name5 = Nikolay("Ni ko la")
name5.check_name()
''' функция проверяет соответствие имен. Если введенное имя соответствует - выводится сообщение Your name correct. Если имя не совпадает -
удаляются пробелы во введеном имени и выводится сообщение, что имя заменено.'''


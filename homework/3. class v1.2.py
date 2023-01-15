'''Создается переменная new_name,  которая убирает пробелы во введенном имени. Если пробелы были и имя совпало - выводится  
сообщение You cant fool me, i know that... Если имя совпало и пробелов не было - Your name correct. В других случая выводится сообщение
You were {name}, but now your name Nikolay'''
class Nikolay():
    def __init__(self, name):
        self.name = name
    def check_name(self):
        # n = self.name
        # check_n = n.split() #разбитие строки на список слов
        # num_check = len(check_n)
        new_name = self.name.replace(" ", '') #создание новой строки , которая состоит из искомой self.name но без пробелов
        if self.name.replace(' ', '') == 'Nikolay':
            print(f"You cant fool me, i know that {self.name} is {new_name}")
        elif new_name == 'Nikolay':
            print(f"Your name correct,{new_name}")
        elif new_name == 'Nikola':
            print(f'Your name correct,{new_name}')
        elif new_name == 'Kolya':
            print(f'Your name correct,{new_name}')
        else:
            print(f"You were {new_name}, but now your name Nikolay")
__version__ = '1.2'
name4 = Nikolay('Artur')
name4.check_name()
name1 = Nikolay('Nikola')
name1.check_name()
name2 = Nikolay('Niko lay')
name2.check_name()
name3 = Nikolay("Artur Alexandrovich")
name3.check_name()
name5 = Nikolay("NikolayIvanovich")
name5.check_name()
name6 = Nikolay('Koly a')
name6.check_name()
name7 = Nikolay('Koly_a')
name7.check_name()
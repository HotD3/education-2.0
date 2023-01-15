class Nikolay():
    def __init__(self, name):
        self.name = name
    def check_name(self):
        n = self.name
        check_n = n.split()
        num_check = len(check_n)
        if (self.name == ('Nikolay') and (self.name == ('Kolya') and self.name == ('Nik') and num_check == 1)):
            print("Your name correct")
        # elif num_check ==1:
        #    print('Length is correct')
        else:
            new_name = self.name.replace(" ", '')
            print(f"Your name {self.name} replaced to {new_name}")
            print(f"I am not {self.name}, i am Nikolay")
            # self.name = 'Nikolay'
__version__ = '1.0'
# name4 = Nikolay('Artur')
# name4.check_name()
name1 = Nikolay('Nik')
name1.check_name()
# name2 = Nikolay('Nikolay')
# name2.check_name()
# name3 = Nikolay("Artur Alexandrovich")
# name3.check_name()
'''Функция check_name создает переменную n, которая принимает одно из значений self.name. После этого создается новая переменная
check_n (с помощью метода split() строка разбивается на список строк). Далее создается переменная num_check, которая принимает значение,
эквивалентное количеству строк в check_n. Далее идет проверка соответствия значения self.name и name . Если оно совпадает - выводится 
сообщение об успешном действии, если нет - убираются пробелы в значении переменной name и выводится сообщение о том, что '''
class Nikolay_v2:
    def __init__(self,name):
        self.name = name
    def check(self):
        name = {'Nikolay' , 'Kolya', 'Nikola'}
        new_name = self.name.replace(" ", '')
        if new_name in name:
           print (f'Yes, ur {new_name} is correct')
        else:
            print(f'No, you name is {new_name}')
p1 = Nikolay_v2("Ni ko la")
p1.check()
__version__ = '1.3'
'''Создание функции. Во время выполнения функции предлагает ввести значение переменной new_name. После этого
удаляются пробелы . Далее идет проверка , принадлежит ли принадлежит new_name списку name. Если да - выводится сообщение Yes, ur name is correct
если нет - No, your name not correct. При ведении Stop цилк завершается'''
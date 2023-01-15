class Nikolay_v2:
    count = 0
    def check(self):
        Nikolay_v2.count +=1
        from test import name
        while True:
           Nikolay_v2.count +=1
           new_name = input("Enter your name: ")
           new_name = new_name.replace(" ", '')
           if new_name in name:
              print (f'Yes, ur name {new_name} is correct')
           elif new_name == "Stop":
              break
           else:
               print(f'No, you name is {new_name} not correct')
        
Nikolay_v2().check()
print(Nikolay_v2.count-2)
__version__ = '1.6'
'''Создание функции,которая импортирует кортеж name из test.py и запускает цикл. Во время выполнения цикла предлагает ввести значение переменной new_name. После этого
удаляются пробелы . Далее идет проверка , принадлежит ли принадлежит new_name списку name. Если да - выводится сообщение Yes, ur name is correct
если нет - No, your name not correct. При ведении Stop цилк завершается. Добавлен счетик итераций цикла While'''
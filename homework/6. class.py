class Person():
    
             
        # name = input("Enter name")
        # surname = input("Enter surname")
        # birth = input("Enter place of birth")
        # age = input("Enter ur age")
    def info(self):
        import datetime
        year = datetime.datetime.now().year
        
        # while True:
        n = input("Enter name: ")
        str_n = str(n)
        s = input(("Enter surname: "))
        str_s = str(s)
        b = input("Enter place of birth: ")
        str_b = str(b)
        a = int(input("Enter year of birth:  "))
        year = datetime.datetime.now().year
        age = year - a
        print(f"{str_n} was born in {str_b} {age} years ago")
             

#         A
# p1 = Person()
# p1.info()
Person().info()
__version__ = '1.4'
'''Ввод данных с клавиатуры и вывод сообщения с именем , страной рождения и возрастом. Возраст работает не корректно, тк считает только 
год и получаетмся погрешность. Нужно посчитать количество дней и поделить на 365, чтобы узнать возраст'''
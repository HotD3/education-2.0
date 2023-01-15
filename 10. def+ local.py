x = 15           #указание значения параметра
def new_x(x):          #создание функции с параметром Х
    print ("x=", x)           #вывод значения параметра Х
    x=int(input('Enter X:'))   #создание локалькой переменной Х
    print('Local x=', x)
new_x(x)          #вызов
print('X still', x)
print(new_x(x))
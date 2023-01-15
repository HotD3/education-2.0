def minmax(a,b):              # Создание функции с параметрами a/b
    if a > b:
        print(a, 'bolshe', b)
    elif a == b:
        print(a, '=', b)
    else:
        print(a, 'menshe', b)
minmax(3,6)                  #вызов функции с указанием значений параметров
x=int(input('Vvedite x:')) 
y=int(input("vvedite y:"))
minmax(x,y)              #вызов функции с присвонием переменных в качестве аргументов (a=x,b=y)
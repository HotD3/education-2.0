def outer():       #создание функции
    x = 5       #присвоение значения переменной внутри функции
    print('Local x = ',x)   #вывод значения функции
    def inner():    #создание новой функции внутри уже созданной
        nonlocal x   #обьявление переменной х не локальной
        x = 15
    inner()  #вызов функции
    print('New x = ', x) #вывод нового значения Х
outer()
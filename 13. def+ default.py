def funcc(message, times = 1):   #создание функции с двумя аргументами. Аргумент times по умолчанию имеет значение 1.
    print(message*times)          #вывод текста на экран, где один аргумент умножается на другой( по умолчанию message * 1)
    
funcc('Hello')  #вызов функции с присвоением значения аргументу message значения hello. Присваивать значение аргументу times не обязательно,т.к. по умолчанию = 1
funcc('World', 5)  #вызов функции с присвоением значений обоих аргументов. message = World, times = 5 . Итог World*5=WorldWorldWorldWorldWorld 
funcc(5,5) #вызов функции с присвоением значения иобоим аргументам. message = 5, times = 5. 5*5=25
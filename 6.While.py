number = 23
running = True
while running:
    number1 = int(input('Enter number1:')) #Ввод number1 находится внутри цикла while, чтобы продолжать вводить число до тех пока не угадаем.
    if number==number1:
        print ('Vi ygadali 4islo')
        running = False #завершение цикла , если угадали число. В противном случае программа будет предлагать ввести новое значение number1
    elif number > number1:
        print(('Number1 bolshe 4em number'))
    else:
        print('Number1 menshe 4em number')
else:                      #Вывод блока else, если цикл окончен и running - False
    print('Цикл окончен')
print('Konec')
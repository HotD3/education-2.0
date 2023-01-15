def total(initial=5, *numbers, extra_number):  #создание функции с параментрами initial, numbers and extra_number. 
    count = initial                #создание переменной count и присвоение ей значения параментра initial . ь.е. 5
    for number in numbers:          #проход по всем элементам кортежа numbers.
      count += number               #значение переменной count равно count + значение каждого элемента кортежа numbers 
    count += extra_number              #значение переменной count равно count + значение парамента extra_number
    print(count)                             #вывод значения count на экран
total(10, 1, 2, 3, extra_number=50)             #вызов функции total cо значением параментров initial = 10, numbers = [1,2,3], extra_number = 50
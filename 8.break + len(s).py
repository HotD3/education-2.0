while True:                             # то тех пор, пока цикл True будут выполняться команды
    s=input(('Enter something: '))          #ввод значения аргумента s
    #if s=='Exit':                  #условие, пр ивыполнении которого цикл прерывается. Если значение агумента равно Exit. чувстивткльно к регистру
    if len(s) >= 10:               # условие, пр ивыполнении которого цикл прерывается. Если длина значения аргумента больше 10
        break                     # команда прерывания цикла
    print('Length of the string is :', len(s))         # вывод текста и длиной строки
    if len(s) < 3:
        print('Length is not enough!')  #если строка короче , чем опрелделен ов условии - выовд жтого сообщения
        continue   #продолжение выполнения цикла
print('Konec cikla')

def total(a=5, *numbers, **phonebook):   #создание функции с параметром а=5 и 
    print('a', a)
#проход по всем элементам кортежа
    for single_item in numbers:
      print('single_item', single_item)
#проход по всем элементам словаря
    for first_part, second_part in phonebook.items():
      print(first_part,second_part)
print(total(8,1,2,3,Jack=1123,John=2231,Inge=1560))
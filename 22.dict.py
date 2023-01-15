phonebook = {'Artur'  :  '0501622508',                #Создание словаря
              'Dasha'  :  '0668225567',
              'Mama'   :  '0506130443'}
print('Arturs number is', phonebook['Artur'])         #вывод на экран значения ключа "Artur"
phonebook['Papa'] = '0501622509'  #добавление ключа-значения в словарь
phonebook['Spammer'] = '8800777332' #добавление ключа-значения в словарь
for name, number in phonebook.items():   #использование цикла for и метода items и возвращение списка кортжей, который  содержит пару элементов
    print('Contact {0} has mobile number {1}'.format(name, number)) #вывод   на экран всех элементов словаря
print('Almost in phonebook', len(phonebook), 'contacts')  #вывод на экран общего количества элементов словаря
#phonebook['Papa'] = '0501622509'
print(phonebook['Papa'])      #вывод на экран значения ключа 'Papa'
if 'Spammer' in phonebook:         #Проверяем, существует ли ключ 'Spammer' в словаре phonebook
    del phonebook['Spammer']       #выполнение операции удаления ключа-значения 
    print('Contact has been deleted')  #если выполняется заданное условие - выводится сообщение об успешном удалении
else:
    print('This contact does not exist this phonebook')  #если условие не выполняется - выводится сообщение о том, что такого контакта нет


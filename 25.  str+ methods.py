name = 'Artur'
if name.startswith('Ar'):  #использование метода startswith для проверки , начинается ли строка с заданного значения
    print('Yes')
if 'A' in name:  #проверка, содержится ли А в строке( чувствительно к регистру)
    print('Yes, a exists in the name')
if name.find('rt') != -1:   #использовнаие метода find для определения позиции в строке. Если строка не обнаружена - возвращается значение -1
    print('Yes, it exists this string')
delimiter = '+++' #создание переменной delimiter со значением +++
new_list = ['LS1', 'LS2', 'LS3'] #создание списка 
print(delimiter.join(new_list)) #использование метода join для объединения элементов строки
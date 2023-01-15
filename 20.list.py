shoplist = ['apple', 'mango', 'carrot', 'bananas']  # создание списка с названием shoplist
print ('I must buy',len(shoplist), 'types of fruits') #вывод количества элементов в списке
print ('Fruits:', end=' ') #создание пробела + после слова Fruits
for item in shoplist:# 
    print(item, end=' ')#
print('\nI need to buy some rice') #
shoplist.append('rice')#добавление элемента в список
print ('My new shoplist:', shoplist)#вывод обновленного списка
print('I need to sort my shoplist')#вывод сообщения о необходимости сортировки списка
shoplist.sort()#сортирвока списка по умолчанию по алфавиту
print(('Sorted shoplist looks like:', shoplist))#вывод отсортированного списка
print('First of all i need to buy an', shoplist[0])#вывод сообщения и элемента списка с порядкровым номером 0
olditem = shoplist[0]#создание переменной olditem и присовение ей значения элемента списка 0
del shoplist[0]#удаление элемента списка
print(('New shoplist:', shoplist))#вывод нового значения списка
print('i bought', olditem)#вывод сообщения и значения переменной olditem

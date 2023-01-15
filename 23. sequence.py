shoplist = ['Meat' , 'Sausages', 'Juice', 'Water']  #создание списка
print('Almost i need to buy:', len(shoplist), 'goods') #вывод количества элементов в списке
print ('Drinks which i need to buy:', shoplist[2:]) #вывод элементов списка начиная с третьего
print('First of all i need to buy some', shoplist[0]) #вывод первого элемента списка
del shoplist[0] #удаление первого элемента списка
print('Shoplist:', shoplist[:]) # вывод всех элемпентов списка
shoplist.append('test') #добавление нового элемента в список
print(shoplist) #вывод списка
for product in shoplist:   
    print([product])#возвращение всех элементов в списке
print(('Almost i need to buy:', len(shoplist), 'goods'))        #в данном случае это список, так как он заключен в (), по этому все элементы выводятся в виде элементов списка
print('Every 2nd element:', shoplist[::2]) #вывод элементов списка с шагом два( 1,3,5,7 и тд)
print('Reverse shoplist:', shoplist[::-1]) #вывод элементов с шагом -1, т.е (4,3,2,1)
print(shoplist[::-2])  #вывод элементов с шагом -2 (4,2)
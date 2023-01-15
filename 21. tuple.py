shoplist = ('Rice', 'water', 'sugar', 'potato', 'meet', 'juice')  #создание кортежа shoplist
print('Almost u need to buy', len(shoplist), 'products') #вывод сообщения с длиной кортежа
new_shoplist = ('Chrisps', 'sweets', 'fruits', shoplist)#слздание нового кортеджа new_shoplist, который включает в себя старый кортеж shoplist
print('Updated shoplist is: ',new_shoplist) #вывод нового кортежа на экран
print('Count of products in shoping list is:', len(new_shoplist))   #длина нового кортежа
print('The products added before shoping:', new_shoplist[3])  #вывод элементов нового кортежа, которые относятся к старому кортежу shoplist
print('Products added in the supermarket:', new_shoplist[0:3])  #вывод элементов нового кортежа без учета старого
print('Almost i bought', len(new_shoplist)-1 +len(shoplist), 'products')#вывод общего значения элементов нового кортежа
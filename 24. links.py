shoplist = ['Eggs', 'Milk', 'Meat', 'Coffee']
print(shoplist)
shoplist1 = shoplist  #'мы создаем ссылку на список shoplist. Если мы вносим изменения в shoplist, они будут отражаться в shoplist1
print(shoplist1)
del shoplist[0]
print(shoplist)
shoplist1 = shoplist[:] #создание копии списка путем полной вырезки
del shoplist1[2]
print(shoplist)
print(shoplist1)
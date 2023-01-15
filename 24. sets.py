shoplist = ['Eggs', 'Milk', 'Meat', 'Coffee']
print(shoplist)
shoplist1 = shoplist
print(shoplist1)
del shoplist[0]
print(shoplist)
shoplist1 = shoplist[:] #создание копии списка путем полной вырезки
del shoplist1[2]
print(shoplist)
print(shoplist1)
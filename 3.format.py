print('{0:.1}'.format(1/3))
print('{0:+^7}'.format('Hello')) #вывод аргумента {0} c центрированием(^) и добавлением "+", чтобы общее поличесво символов было 7, в данном случае hello (5)+ 2 символа по бокам. если добавлять 1 символ - он появится после аргумента
print('His name is {name}, hi is {nation}'.format(name='Artur',nation='Ukrainian')) # name/ nation являются аргументами . в методе format мы задаем их значения, порядок задания значений аргументов может быть произвольным.
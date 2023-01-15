
#Создайте класс Soda (для определения типа газированной воды), принимающий 1 аргумент при инициализации 
# (отвечающий за добавку к выбираемому лимонаду). 
#В этом классе реализуйте метод show_my_drink(), выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки,
#  а иначе отобразится следующая фраза: «Обычная газировка».
class soda():
    def __init__(self, name, syrup):
        #self.name = name
        self.syrup = syrup
    def show_my_drink(self):
        if self.syrup == 'No syrup':
            print(f"Your {name} without any syrup")
        else:
            print(f"Your {name} with {self.syrup} syrop")
name = 'Lemonade'
chocolate = soda(name, 'Chocolate')
chocolate.show_my_drink()
no_syrup = soda(name, "No syrup")
no_syrup.show_my_drink()
# Николаю требуется проверить, возможно ли из представленных отрезков условной длины сформировать треугольник. 
# Для этого он решил создать класс TriangleChecker, принимающий только положительные числа. 
# С помощью метода is_triangle() возвращаются следующие значения (в зависимости от ситуации):
# – Ура, можно построить треугольник!;
# – С отрицательными числами ничего не выйдет!;
# – Нужно вводить только числа!;
# – Жаль, но из этого треугольник не сделать.

class TringleChecker:
    def __init__(self,a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def is_triangle(self):
        if ((self.a + self.b - self.c) >  0) and ((self.a + self.c - self.b) >0) and ((self.b + self.c - self.a)>0):
            print ('Triangle exists')
        else:
            print('This triangle can not exist. Learn math bitch!')
tr = TringleChecker(1, 2, 3)
tr.is_triangle()
            

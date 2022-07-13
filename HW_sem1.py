# 1- Напишите программу, которая принимает на вход цифру, 
#обозначающую день недели, и проверяет, является ли этот день выходным.
#*Пример:*
#- 6 -> да
#- 7 -> да
#- 1 -> нет
week_days = {1:"Пн",2:"Вт",3:"Ср",4:"Чт",5:"Пт",6:"Сб",7:"Вс"}
lst = list(range(1,8))
check_number = True
while check_number:
    days_number = input('Введите день недели:')
    if days_number.isdigit():
        days_number = int(days_number)
        if days_number in lst:
            check_number = False
        else:
            print('Такой день недели не существует')
    else:
        print('Вы ввели не число!')
if days_number ==6 or days_number == 7:
    print(f'{days_number} {week_days[days_number]}-> Выходной')
else:
     print(f'{days_number} {week_days[days_number]}-> Рабочий')   
#2- Напишите программу для проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.     
print('\nX/Y/Z   ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z')
for x in range(0,2):
    for y in range(0,2):
        for z in range(0,2):
            expression1 = not(x or y or z)
            expression2 = not(x) and not(y) and not(z)
            print(f'{x}/{y}/{z}      {expression1 == expression2}')
#3- Напишите программу, которая принимает на вход координаты точки (X и Y),
#  причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
#  эта точка (или на какой оси она находится).
#*Пример:*
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3  
while True:
    try:
        X = int(input('Введите координату X: '))
        Y = int(input('Введите координату Y: '))
    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
    else:
        break
result=0
if (X > 0 and Y>0):
    result =1
elif (X<0 and Y>0):
    result =2
elif (X<0 and Y<0):
    result =3
elif (X>0 and Y<0):
    result =4
if result>0:
    print(f"Точка [{X}:{Y}] находится в {result} четверти")                 
else:
    print(f"Точка [{X}:{Y}] находится в на пересечении четвертей")

# 4 - Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
lst = list(range(1,5))
Quaters = {1:"X>0 и Y>0",2:"X>0 и Y<0",3:"X<0 и Y<0",4:"X>0 и Y<0"}
Flag = True
while Flag:
    quater = input('Введите номер четверти: ')
    if quater.isdigit():
        quater = int(quater)
        if quater in lst:
            Flag = False
        else:
            print('такой четверти не существует')
    else:
        print('вы ввели не число') 
print(f'{quater} находится в {Quaters[quater]}')

#5- Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.
#*Пример:*
#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
import math
while True:
    try:
        X1 = int(input('Введите координату X1: '))
        Y1 = int(input('Введите координату Y1: '))
        X2 = int(input('Введите координату X2: '))
        Y2 = int(input('Введите координату Y2: '))
    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
    else:
        break
      
Katet1 = (X1-X2)
Katet2 = (Y1-Y2)
Result = math.sqrt(Katet1*Katet1 + Katet2*Katet2)
print(f'расстояние между точками равно {round(Result,2)}')
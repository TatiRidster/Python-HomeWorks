#1 - Задайте список из нескольких чисел. Напишите программу, которая 
# найдёт сумму элементов списка, стоящих на нечётной позиции.
#*Пример:*
#- [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
from ast import Num
from random import randint


def sum_odd_numbers(lst):
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0:
            sum += lst[i]
    print(f"Сумма равна: {sum}")

lst = [2, 3, 5, 9, 3]
sum_odd_numbers(lst)
lst = list(map(int, input("Введите числа через пробел:\n").split()))
sum_odd_numbers(lst)
#2 - Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#*Пример:*
#- [2, 3, 4, 5, 6] => [12, 15, 16];
#- [2, 3, 5, 6] => [12, 15]

def mult_of_pairs_lst(lst):
    new_lst =[]
    if len(lst) % 2 != 0:
        l = len(lst)//2 + 1 
    else: 
        l = len(lst)//2
    new_lst = [lst[i]*lst[len(lst)-i-1] for i in range(l)]
    print(f'sum of pairs of elements {new_lst}')

# lst = [2, 3, 4, 5, 6]
# mult_of_pairs_lst(lst)
# lst = list(map(int, input("Введите числа через пробел:\n").split()))
# mult_of_pairs_lst(lst)
lst = [randint(1, 11) for _ in range(6)]
print(f'random list  {lst}')
mult_of_pairs_lst(lst)
#3 - Задайте список из вещественных чисел. Напишите программу, 
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#*Пример:*
#- [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564
input_list = [randint(1,100)+randint(10,999)/100 for _ in range(randint(1,10))]
print(input_list)

def max_min_diff(list_of_numbers: list) -> int:
    max = list_of_numbers[0]-int(list_of_numbers[0])
    min = list_of_numbers[0]-int(list_of_numbers[0])
    
    for i in list_of_numbers:
        num = i-int(i)
        if num>max:
            max = num
        if num<min:
            min=num
        diff=max-min        
    return max,min,diff
max,min,diff = max_min_diff(input_list)
print(f"max:{max:.3f} - min: {min:.3f} = difference {diff:.3f}")
#4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#*Пример:*
#- 45 -> 101101
#- 3 -> 11
#- 2 -> 10

def decimal_to_binary():
    while True:
        try:
            n = int(input('Input integer number: '))
        except ValueError:
            print("Это не правильный ввод. Это не целое число! Попробуйте еще раз.")
        else:
            break
    conv = ""
    while n != 0:
        conv = str(n%2) + conv
        n //=2
    return conv

print(f"Binary number: {decimal_to_binary()}")
#5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для
#  отрицательных индексов.
#*Пример:*
#- для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
#  [Негафибоначчи](https://clck.ru/sH87m)

def Fibonacchi():
    while True:
        try:
            n = int(input('Input integer number: '))
        except ValueError:
            print("Это не правильный ввод. Это не целое число! Попробуйте еще раз.")
        else:
            break
    fib_positive =[0,1]    
    fib_negative =[0,1] 
    for i in range(2, n):
        fib_positive.append(fib_positive[-1]+fib_positive[-2])   
    for j in range(2,n):
        fib_negative.append(fib_negative[-2]-fib_negative[-1])
    return print(f"Fibonacchi {fib_negative[::-1]+fib_positive[1:]}")

Fibonacchi()
#1- Вычислить число c заданной точностью d. Число Пи не просто обрезать с math.pi,
#а вычислить, используя формулы: Нилаканта, ряды Тейлора, серию Ньютона или серию Чудновских.
#Пример:
#- при d = 0.001, π = 3.141.    10^(-10)≤ d ≤10^-1
from decimal import *
from math import factorial
 
def chudnovsky(d):
    pi = Decimal(0)
    k = 0
    while k < d:
        pi += (Decimal(-1)**k) * (Decimal(factorial(6 * k)) / ((factorial(k)**3) * (factorial(3 * k))) * (13591409 + 545140134 * k) / (640320**(3 * k)))
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi**(-1)
    return pi
# Установка новой точности из библиотеки decimal. Функция decimal.getcontext() 
# возвращает текущий контекст для активного потока. 
# текущий контекст можно изменять, присваивая атрибутам класса decimal.Context() другие
# значения на месте
d=8
getcontext().prec = d
print(chudnovsky(d))
#2- Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности. Посмотрели, что такое множество? 
# Вот здесь его не используйте.
#используем списки list
lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")
#3- Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.
#Пример: при N = 12 -> [2, 3]


def number_factors():
    while True:
        try:
            n = int(input('Input integer number: '))
        except ValueError:
            print("Это не правильный ввод. Это не целое число! Попробуйте еще раз.")
        else:
            break
    i = 2 # первое простое число
    lst = []
    new_lst =[]
    while i <= n:
        if n % i == 0:
            lst.append(i)
            n //= i
            i = 2
        else:
            i += 1
        [new_lst.append(i) for i in lst if i not in new_lst]
    return new_lst
    
factors_lst =[]
factors_lst =number_factors()
print(f"Простые множители числа приведены в списке: {factors_lst}")
#4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
#В файле содержится, например:
#Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
#https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
#Это на случай возникновения непонятных символов в файле.
#with open('text.txt',encoding = 'utf-8') as file:
#print(file.read())  ord('\u0394') - это даст число 916
#chr(916)
def check_digit_in_string(str_to_lookup: str) ->str:
    result_string =''
    char_count=0
    digit_flag =0
    length = len(str_to_lookup)
    for i in range(0,length):
        empty_char =str_to_lookup[i]
        if empty_char==' ':
            if digit_flag ==0:
                if len(result_string) !=0:
                    result_string+=' '
                result_string += str_to_lookup[i-char_count:i]  
            char_count = 0
            digit_flag = 0
        elif is_int(str_to_lookup[i]):
            digit_flag = 1
        else:
            char_count +=1
    return result_string

def is_int(str):
    try: 
        int(str)
        return True
    except ValueError:
        return False
#Блок работы с файликом нужен для тренировки        
str ='Мама сшила м0не штаны и7з бере9зовой кор45ы 893'
with open('text.txt','w',encoding = 'utf-8') as file:
    file.write(str)
    file.close()
with open('text.txt','r',encoding = 'utf-8') as file:
    str_new = file.read()
    file.close()
print(f' строка без цифр : {check_digit_in_string(str_new)}')
with open('text.txt','r',encoding = 'utf-8') as file:
    lines = file.readlines()
del lines[0]

with open('text.txt','w',encoding = 'utf-8') as file:
    file.write(check_digit_in_string(str_new))
    file.close()
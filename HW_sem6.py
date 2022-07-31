#1- Определить, присутствует ли в заданном списке строк, некоторое число
from functools import reduce
import math
def is_num(lst,number):
    return list(filter(lambda element: str(number) in element, lst))
lst = ['В','те2ории,','теори4я','и','1','прак1тика','нераз5делимы.','Н1а','практ8ике','эт3о','не','та0к.']
number=1   
print(is_num(lst,number))
#2- Найти сумму чисел списка стоящих на нечетной позиции
def is_int(input_number:str):
    try:
        input_number = int(input_number)
        return input_number
    except ValueError:
        return False

num = is_int(input('Введите число: '))
result = list(map(int, str(num)))
sum_of_elem = reduce(lambda a,b:a+b, result[1::2])
print(sum_of_elem)
#теоремы:
#делает список от 1 до введенного числа 
# nums = list(range(1, int(is_int(input('Введите число: '))+1)))
# #фильтрует список и выдает список только нечетных элементов списка начиная с нулевого элемента
# filtered_nums=(list(filter(lambda elem: nums.index(elem)%2, nums)))
#выдает сумму чисел списка стоящих на нечетной позиции
# from functools import reduce
# reduce(lambda a,b:a+b, nums[1::2])
#за нечетность отвечает[1::2], весь список [0::1],[0:2:1] до 2 элемента не включая его с шагом 1

# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
p1  = list(map(int, input('Введите координаты первой точки через пробел: ').split()))
p2  = list(map(int, input('Введите координаты второй точки через пробел: ').split()))
  
res = reduce(lambda a, b: (a + b)**(1/2),(map(lambda p: (p[1] - p[0])**2,zip(p1, p2))))
print(res)
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
lst_second = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
num = "йцу"
def second_coming(lst:list, num):
    return [i for i, element in enumerate(lst) if num in element] [1] if len(lst) >= 2 else 0
print(second_coming(lst_second,num))
# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
def mult_list(nums):
    return [nums[i] * nums[-i-1] for i in range(math.ceil(len(nums)/2))]
lst =[3,9,5,7,8]
print(f'результат произведения пар {mult_list(lst)}')
# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.
n=5
def get_sequence(n):
    list1= [3**i for i in range(0, n+1) if (i % 2) == 0]
    list2= [(-3)**i for i in range(0, n+1) if (i % 2) !=0]
    list3=list1+list2
    return list3
print(get_sequence(n))
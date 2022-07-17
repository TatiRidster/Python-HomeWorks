# 1 - Напишите программу, которая принимает на вход вещественное 
# число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11
def test_number(text):
    is_minus = False
    int_test = True    
    while int_test:
            number_test = input(f'{text}')
            if number_test[0] =="-":
                is_minus = True
                number_test =number_test.replace("-","")
            if number_test.isdigit():
                number_test=int(number_test)
                if is_minus:
                    number_test*=-1
                int_test = False
            elif number_test.isdecimal():
                number_test=float(number_test)
                if is_minus:
                    number_test*=-1
                int_test = False       
            else:
                print("Это не правильный ввод. Это строка, попробуйте еще раз.")
    return number_test
#мне эта проверка(выше, разбирали на семинаре) не нравится, ибо на вещественные числа
#она не работает
#моя проверка проверяет хорошо вещественные числа, но выдает лог выражение (true или false)
#сделать универсальный отличный вариант не получается
import re
def is_float(str):
    realnum = re.compile("^[-+]?[0-9]*\.?[0-9]+(e[-+]?[0-9]+)?$")
    if realnum.match(str):
        return True
    else:
        return False
a = input('Введите число: ')
number_float = str(is_float(a))

if is_float(a) == True:
    a=str(a)
else:
    print("число введено неверно")
result=0
for i in a:
    if i.isdigit():
        result =result +int(i)
        
print(f'Cумма введенного {a} равна {result}')

# 2 - Напишите программу, которая принимает на вход число N и 
# выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
N=int(input('Введите число: '))
lst=[1]
for i in range(1,N):
    lst.append(lst[i-1]*(i+1))
print(lst)    
# 3 - Задайте список из n чисел последовательности (1+1/n)**n и выведите
#  на экран их сумму.
# *Пример:*
# - Для n = 6: {1: 2.0, 2: 2.25, 3: 2.37037037037037, 4: 2.44140625, 5: 2.4883199999999994, 6: 2.5216263717421135}
while True:
    try:
        number = int(input('Введите число: '))
        if number ==0:
            print('Введенное число должно быть больше нуля')
    except ValueError:
        print("Это не правильный ввод. Это не число вообще! Это строка, попробуйте еще раз.")
    else:
        break
    
dictionary={}
for i in range(1,number+1):
    dictionary[i]=(1+1/i)**i
print(dictionary)

result=0
for i in dictionary:
    result += float(dictionary[i])
print(f'Cумма элементов равна {result:.2f}') 
    
# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) -
#  для задания случайности
#нашла интересный нерабочий вариант с битами, сделала рабочим
import struct
import time

def lastbit(f):
    return struct.pack('!f', f)[-1] & 1

def getrandbits(k):
    #"Return k random bits using a relative drift of two clocks."
    # though it might work even if they use the same clock
    
    result = 0
    for _ in range(k):
        time.sleep(0)
        result <<= 1
        result |= lastbit(time.perf_counter())
    return result
def randint(a, b):
    "Return random integer in range [a, b], including both end points."
    return a + randbelow(b - a + 1)

def randbelow(n):
    "Return a random int in the range [0,n).  Raises ValueError if n<=0."
    
    if n <= 0:
       raise ValueError
    k = n.bit_length()  # don't use (n-1) here because n can be 1
    r = getrandbits(k)          # 0 <= r < 2**k
    while r >= n: # avoid skew
        r = getrandbits(k)
    return r
print(*[randint(10, 100) for _ in range(10)])        
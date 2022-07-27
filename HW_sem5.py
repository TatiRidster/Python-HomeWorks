#1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
#'абвгдейка - это передача' = >" - это передача"

text = 'абвгдейка - это передача про абвазбуку и мысленные констабврукции детей'

def del_words(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

new_text = del_words(text)
print(new_text)
#3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
#['python', 'c#']
#[1,2]
#Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
#[(1,'PYTHON'), (2,'C#')]
#Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
#[сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
#[(1,'PYTHON'), (102,'C#')]
#Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице, в третьем столбце: https://www.charset.org/utf-8
#Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
#Cложите получившиеся числа и верните из функции в качестве ответа вместе с 
# преобразованным списком
from functools import reduce
def create_prog_list():
    with open('prog_lang.txt', encoding = 'utf-8') as file:
        program_languages = file.read().split('\n')
    num_list = list(range(1, len(program_languages)+1))
    tuples_list= zip(num_list, [word.upper() for word in program_languages])
    return list(tuples_list)

def filter_list(tuples_list):
    result_list = []
    result =0
    for number,program_languages in tuples_list[::]:
        points = reduce(lambda a,b: a+b, [ord(char) for char in program_languages])
        if points%number ==0:
            result +=points
            result_list.append((points,program_languages))
    del tuples_list
    return result, result_list


tuples_list = create_prog_list()
# print(tuples_list)
sort_list = filter_list(tuples_list)
print(f'Сумма и преобразованный список  {sort_list}')

#4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах
with open('RLE_decoded.txt', 'r') as file:
    data = file.read()

def rle_encode(data): 
    encoding = '' 
    prev_char = '' 
    count = 1 
    if not data: return '' 
    for char in data: 
        if char != prev_char:  
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else:  
        encoding += str(count) + prev_char 
        return encoding

str_encode = rle_encode(data)
print(str_encode)
with open('RLE_encoded.txt', 'w') as file:
    file.write(rle_encode(data))
    file.close()

def rle_decode(data): 
    decode = '' 
    count = '' 
    for char in data: 
        if char.isdigit(): 
            count += char 
        else:  
            decode += char * int(count) 
            count = '' 
    return decode
with open('RLE_encoded.txt', 'r') as file:
    decoded_str = file.read()
    file.close()    
decoded_val = rle_decode(decoded_str)
print(decoded_val)
with open('RLE_decoded.txt', 'w') as file:
    file.write(rle_decode(decoded_str))
    file.close()
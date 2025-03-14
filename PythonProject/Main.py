'''Минимальный элемент'''
#numbers = [9,2,3,1,10,5,6,7,8]
#first_el = numbers[0]
#for i in numbers:
#    if i < first_el:
#        first_el = i
#print(first_el)

#numbers = [9,2,3,1,10,5,6,7,8]
#print(min(numbers))


'''МАКСИМАЛЬНЫЙ ЭЛЕМЕНТ'''
# numbers = [5,2,3,1,4]
# first_el = numbers [0]
# for i in numbers:
#     if i > first_el:
#         first_el = i
# #print(first_el)
''''''
from itertools import count
from xmlrpc.client import boolean

'''Есть строка - МИР
Нужно вывести это слово -Наоборот'''
''''''
'''Решение'''
#world = 'МИР'
#print(world[:: -1])
#

'''Калькулятор ч-з функции '''
#def add(a, b):
#    return  a + b
#def calculator (a,b , operation):
#   if operation == '+':
#    return  a + b
#   elif operation == '-':
#       return a - b
#   else:
#    return f'Ничего'

#res = calculator(
#    int(input('Первое число: ')),
#    int(input('Первое число: ')),
#    input('Введите,что делать? (+, -)')
#)

#print(res)


'''ЛЯМБДА '''

# lambda n: n % 2 == 0
# print(res(2))
#res = lam

'''Сортировка списка по четности.Напишите прог.кот.запрашивает список чисел упользователя
 а затем сортирует четные числа в порядке убывания,
 нечетные - в порядке возрастания.Условие пишем прог.на основе функции '''

# numbers = [8,3,5,2,10]
# def sort_two(numbers):
#    left = sorted([k for k in numbers if k %2 ==0],reverse=True)
#    right = sorted([ k for  k in numbers if k%2 ==1])
#
#    result = left + right
#
#    return result
# print(sort_two(numbers= list(map(int,input("Введите число через пробел: ").split()))))

'''Получение данных от пользователя '''
#input("Введите свой возраст")
#a="GULZINA"
#b=len(a)
#print(b)

# def add (a, b):
#      c = a + b
#      return c
# my_func = add (5, 2)
# print((my_func))

'''Есть строка -"МИР"
 Нужно вывести это слово -Наоборот
 Условие на основе функции.'''
#
# def reverse_el(world):
#     res = ''
#     for el in world:
#         res =el + res
#     return res
# res = reverse_el('МИР')
# print(res)

'''Нужно их отсортировать.
 Условие:Решить на основе функции.'''
#
# def my_sorted (numbers):
#     while numbers != sorted(numbers):
#         for number in range(len(numbers) -1):
#             if numbers[number] > numbers[number + 1 ]:
#                 numbers [ number], numbers[number + 1] =numbers[number + 1],numbers[number]
#                 return numbers
# print((my_sorted([5,2,1,3,4] )))
#
#
#
''' Задачи Литкода '''
#
# def mergeAlternately(self, word1: str, word2: str) -> str:
#     result = ""
#
#     for w1, w2 in zip(word1, word2):
#         result += w1 + w2
#
#     result += word1[len(word2):] + word2[len(word1):]
#     return result
#
''' Дан набор чисел преобразовать на нечетные Гулкайыр '''
# def number (Sam):
#     ser = []
#     for i in Sam:
#         if i %2 ==0:
#             i+=1
#             ser.append(i)
#
#     return ser
# print(number([67,787.23,20,80]))
#
# def number(list):
#     res =[]
#     for i in list:
#         if # есть продолжение???

''' Напишите функцию которая открывает любой адрес в браузере.'''

# import webbrowser
#
# def open_url(lru):
#     webbrowser.open(lru) # До конца решить!
#
# my = input(' Введите адрес:')
#
# if my == 'youtube':
#     open_url('https://www.youtube.com')
#
# elif my == 'instagram':
#     open_url('https://www.instagram.com')
#
# elif my == 'google':
#     open_url('https://www.google.com')
#
# else:
#     print(' Что то адрес не понятный ')

''' ПИТОН  -РАБОТА С ФАЙЛАМИ '''

''' Здесь мы открываем файл '''
# file = open('files/text.txt', 'w')

''' Здесь мы что- то делаем с файлом.'''
# file.write(' Hi \n')

'''Здесь мы закрываем файл.'''
# file.close()
#
# file = open('text.txt', 'w')
#
# file.write(' Hi \n')
#
# file.close()

''' Append - Добавление в файл '''

# file = open('text.txt', 'a')
#
# file.write(' Hi Gulzina \n')
#
# file.close()

'''Read - Чтение '''
# file = open('text.txt', 'r')
#
# file_read =file.read()
#
# print(file_read)
#
# file.close()
#

'''Напишите фунуцию кот.принимает то что впис.в опред.файл и вписывает туда то что ввели '''
#
# def open_file_write_in_file(text):
#     file = open('text.txt','w')
#     file.write(text)
#     file.close()
#
# open_file_write_in_file('Привет ты теперь с файлами будешь дружить')

'''Нап.ф-цию кот.принимает путь до файла и читает ее,отдает результат в виде чтения в терминале.'''

# def open_file_ang_read_file(path_to_file):
#     file = open(path_to_file,'r')
#     result_read = file.read()
#     file.close()
#
#     return  result_read
#
# print(open_file_ang_read_file('text.txt'))

''' Напиш.фун-ю кот.принимает путь до файла и принимает то,что мы туда вписываем,
и возвращает  то что писали ( т.е пишет сначала,
и прочтет то что вписали.'''
#

# def open_file_write_and_start (path_to_file, data):
#     file = open(path_to_file, 'w')
#     file.write(data)
#     file.close()
#
#     file = open(path_to_file, 'r')
#     result = file.read()
#     file.close()
#
#     return result
#
# my_func =open_file_write_and_start('text.txt' ,'Фвйлы файлы')
# print(my_func)
#
#
# def open_file_write_and_start (path_to_file, data): # Работает!
#     file = open(path_to_file, 'w')
#     file.write (data)
#     file.close()
#
#     file =open(path_to_file, 'a')
#     file.write('Файлы, фвйлы')
#     file.close()
#
#
#     file = open(path_to_file, 'r')
#     result = file.read()
#     file.close()
#
#     return result
#
# my_func =open_file_write_and_start('text.txt' ,'Теперь только файлы')
# print(my_func)

''' РАБОТА с " with " '''
# with open('files/text.txt', 'w') as file:
#     file.write('То что вписали')
#
# with open('files/text.txt', 'a') as file:
#      file.write('То что вписали')
#
# with open('files/text.txt', 'r') as file:
#     file.read()


# def working_with_files(path_to_file, data): # Работает код!
#     with open(path_to_file, 'w') as file:
#         file.write('data')
#
#     with open(path_to_file, 'a') as file:
#         file.write('То что вписали в конец')
#
#     with open( path_to_file, 'r') as file:
#          file.read()
#
# my_func = working_with_files('text.txt',' То что вписали')
# print(my_func)
#
'''ИСКЛЮЧЕНИЯ!!! '''

# try:
#     num = int(input('Число:'))
#     print(num)
# except ValueError:
#     print('Ожидалось что вы ведете число')

# try:
#     a = 5
#     b = 0
#     print(a/ b)
# except ZeroDivisionError:
#     print('Вы делите на ноль.')
#
# ValueError
# try:
#     num = int(input('Введите число:'))
#     print(num)
# except ValueError:
#     print(('Был введен не то что ожидалось(целое число'))

#FileNotFoundError

# try:
#     with open('file/text.txt', 'w') as file:
#         file.write('awe')
# except FileNotFoundError:
#     print('Такой директорий не существует')

'''Ожидаем 2 числа от пользователя чтобы эти  два числа
# разделить на друг-друга,
# если он ввел корректно ( то есть обе числа- не ноль)→
# все обработает корректно.
# Если нет,то вылавливает конкретное(соот.исключения)
#  и просим ввести данные снова (пока не ввеедет корректные данные)'''

# def func( a,b):
#      result =  a /b
#      return f'Результат:{result}'
#
# while True:
#     try:
#         my_func = func(
#             int(input('Первое число: ')),
#             int(input('Второе число: ')),
#         )
#         print(my_func)
#         break
#     except ZeroDivisionError:
#         print('Вы делите на ноль.')
#     except ValueError:
#          print('Просим ввести заново') # Правильно снова и снова выходит!

# try:# До конца выйди! Файл не найден.
#     file = open('work_with_files/files/text.txt', 'w')
#     file.write('awe')
# except FileNotFoundError:
#     print('Файл не найден')
# finally:
#      file.close()#

'''  Что за задача не знаю уточнить!!!  '''
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     if second_number == 'q':
#         break
#     answer = int(first_number) / int(second_number)
#     print(answer)

''' Задача на Исключения '''

# print("Дайте мне два числа, и я их разделю.")
# print("Введите «q», чтобы выйти..")
# while True:
#     first_number = input("Введите первое число: ")
#     second_number = input("Введите второе число (или 'q' для выхода): ")
#     if second_number == 'q':
#         break
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("Нельза делить на 0!")
#     else:
#         print(answer)

''' Повторение данных '''

'''Создайте словарь самостоятельно
Сортируйте ключей словаре по возрастанию знaчений '''
#
# my_idea = {'name':'gulzina',' first name':'Appazova','rost':168}
# for i in my_idea.values():
#     print(i)
#
# my_idea = {'3':168,'2':20,'1':10}
# print(sorted(my_idea.keys()))

# my_idea = {'3':20,'2':168,'1':10}
# ser =sorted(my_idea,key= my_idea.get,reverse = True)[:5]
# print(ser)

'''  Фрукты'''
'''Пользователь  вводит число K - кол-во фруктов.
Затем он вводит К фруктов в формате название фрукта и его кол-во.
Добавьте все фрукты в словарь,где название фрукта-это ключ, а кол-во -значение.'''

'''Примечание циклом while можно тоже до решить'''

#
# k= int(input('яблоко 3, апельсин 3,мандарин 10:'))
# fruits = {}
#
# for _ in range(k):
#     name= input('яблоко,апельсин,мандарин:')
#     fruits[name] = quantity
# print(fruits)
#
# user1 = 'java'
# user2= 'Python'
# user3 ='js'
# if user1 == 'Python':
#     print(user1)
# elif user2 == 'Python':
#     print(user2)
# elif user3 == 'Python':
#     print(user3)
# else:
#     print('net')
#
'''Найти сумму всех чисел четных с пом.цикла while'''
# number = [ 2,1,4,2,5]
# for el in number:
#     if el %2 == 0:
#
#         print(el)

# numbers = [2, 1, 4, 2, 5]
#
# # Инициализируем переменные
# sum_even = 0
# index = 0
#
# # Цикл while для перебора элементов списка
# while index < len(numbers):
#     if numbers[index] % 2 == 0:  # проверяем, четное ли число
#         sum_even += numbers[index]  # добавляем к сумме
#     index += 1  # переходим к следующему элементу
#
# # Выводим результат
# print(f"Сумма четных чисел в списке: {sum_even}")

''' Импорт, декораторы '''

def dec (func):
    def wrapper():
        print('До выполнения print hello')
        func()
        print('После выполнения print hello')

    return wrapper()
@ dec
def print_hello():
    print('hello')

print_hello

''' ООП '''


















'''
Игра "Угадай число" с подсказками.
Создайте игру, где компьютер загадывает случайное число от 1 до 100.
Пользователь должен угадать число, получая подсказки:
"Число больше" или "Число меньше".
После 7 попыток ига заканчивается.'''

# import random
#
# random_ =random.randint(1 ,100)
#
# k = 7
# while k>= 0:
#     user = int(input('Введите число(1, 100): '))
#
#     if user < random_:
#         print("Число больше.Осталось {k-1} попыток.")
#     elif user > random_:
#         print("Число меньше.Осталось {k-1} попыток.")
#
#     else:
#         print('Вы нашли',"Действительно:",random_)
#         break
#   k -=1
#   if k ==0:
#         break

'''Задачи '''
''' № 1 Выведите все элементы, которые меньше 5 '''
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for el in a:
#     if el <5:
#         print(el)

''' № 2 Нужно вернуть список, который состоит из элементов, общих для этих двух списков '''

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]
# result = []
# for i in a:
#     if i in b:
#         result.append(i)
# print(result)

'''№ 4 Отсортируйте словарь по значению в порядке возрастания .'''
# result ={3:30, 2:20,1:10}
# print(sorted(result.values()))


'''№ 5 Найдите три ключа с самыми высокими значениями в словаре !!!!!'''
# my_dict = {'a':500, 'b':5874,'c':560,'d':400, 'e':5874, 'f': 20} !!!!
# result = sorted(my_dict.items(), key=lambda item: item[1], reverse=True)[:5]
# print(result)

''''№ 6 Напишите проверку на то, является ли строка палиндромом. 
Палиндром — это слово или фраза, 
которые одинаково читаются слева направо и справа налево.!!!!'''

# word = 'adda'
# word = word [::]
# print(word)
''' Первый вариант палиндром'''
#def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]
#
# input_string= input("Введите строку:")
#
# if is_palindrome (input_string):
#     print("Строка является палиндромом")
# else:
#     print("Строка не является палиндромом.")

'''Второй вариант палиндром '''
# a = 'mukum'
# b = a [::-1]
# if b==a:
#      print('yes')
# else:
#     print('no')

''''№ 7 Выведите первый и после.элемент списка'''
# numbers = [ 32,44,11,True,'odd',False]
# print(numbers[0], numbers[-1])
# print(f'первый:{numbers[0]}, последний:{ numbers[-1]}')

'''№ 8 при заданном целом числе и посчитайте п+пп+ппп'''
# ввод 4
# вывод 1
# 22
# 333
# 444

# b = int(input('Введите число:'))
# for i in range(1, b+1):
#     print(str(i) *i)

''' № 9 Нап.прог.кот выводит числа  четные числа из заданного списка 
и останвливает если встречается число 237 '''

# numbers = [52,12,332,11,237,90,54]
# for i in numbers:
#         if i ==237:
#             break
#         elif i % 2 ==0:
#            print(i)

'''№ 10 Напиш.прог.кот.принимает 2 списка и 
выводит все элементы первого кот.нет во втором.'''

# numbers1 = [ 52,11,21,90,78,66]
# numbers2 = [76,55,14,21,90,78,33]
# res =[]
# for num in  numbers1:
#     if num not in numbers2:
#         res.append(num)
# print(res)

''' № 11 Сложите цифры всех целых чисел в в списке.'''
# element = [ 9.2, 'st', 5,12,9.21,2]

# sum__int_elements =0
# for i in element:
#      if type(i) == int:
#          sum__int_elements +=i
# print((sum__int_elements))

'''№ 12 Посчитать сколько раз символ встречается в строке'''

# word = ' apple'
# c = 0
# my_letter = input('Введите букву:')
# for i in word:
#     if i == my_letter:
#         c += 1
# print(f'Буква "{my_letter}" {c} Шт')

''' Второй вариант'''
# word = 'aziza'
# c = 0
# my_letter = input('Введите символ:')
# for i in word:
#     if i == my_letter:
#         c += 1
# print(f'Буква {my_letter} встречается {c} раз')

'''№13 Поменять переменные местами'''
# a = 'Переменная "a"'
# b = 'Переменная " b"'
# a,b = b,a
# print(a)
# print(b)

'''№ 14 С помощью аноним.функции извлеките из списка числа делимые на 15 '''

# numbers = [ 90,12,50,25,61]
# res = lambda numbers: [num for num in numbers if num % 15 == 0]
# print(res(numbers))

'''№ 15 Вы принимаете от пользователя последовательность
чисел,разделенных запятой.
Составтьте список и кортеж  с этими числами'''

# a = list(map(int,input('Введите число').split(',')))
# b= tuple(map(int,input('Введите число').split(',')))
# print(a)
# print(b)

'''№ 16 Выведите первый и последний элемент из списка'''

# numbers =[32,44,11,True, 'odd',False]
# print(numbers[0], numbers[-1])

''' № 17  При заданном n + nn+nnn'''

# n = int(input('Введите число'))
# for i in range (1,n + 1):
#      print(str(i) *i)

''' № 18 Нужно вернуть список  кот.состоит из элементов общих
 для этих двух списков '''

# a = [1,2,3,4,5,6,7,8,13,21,34,55,89]
# b = [1,2,3,4,5,6,7,8,9,10,11,12,13]
# res = []
# for elem in a:
#     if elem in b:
#         res.append(elem)
# print(res)

'''Напишите прог.кот принимает 2 списка и выводит
все элементы первого кот.нет во втором'''

numbers1 =list(map(int,input("Введите первое из списка:").split()))
numbers2 = list(map(int,input("Введите первое из списка:").split()))
c = []
for i in numbers1:
    if i in numbers2:
        continue
    else:
        c.append(i)
print(c)
''' Второй вариант'''

numbers =[43,54,12,63,237,90,21]
numbers2 = [43,54,63,237,100,200]
result = []
for elem in numbers:
    if elem not  in numbers2:
        result.append(elem)
print(result)

''' № 19 Напишите программу кот.выводит четные числа из заданного
списка и останавливается  если встречается число 237'''
# numbers =[43,54,12,63,237,90,21]
# res =[]
# for elem in numbers:
#     if elem == 237:
#         break
#     if elem % 2 == 0:
#         print(elem)






































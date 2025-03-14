from math import factorial
from queue import PriorityQueue

#
# Задача № Тебе 100 лет
# name =input("Введите свое имя:")
# age = int(input("Введите свой возраст:"))
# year = 2024 - age + 100
# print (name + "Тебе будет 100 лет", + str (year)) # Как пробел сделать?
#
# Задача № 2
# age = 18
# if age > 17:
#     print("Ты можешь смотреть кино")
# elif age < 17 and age >12:
#     print(" Ты можешь смотреть телевизор ")
# else:
#     ("Тебе разрешено только мультфильм")
#
# Задача № 3
#
# a = 3
# if a == 5:
#     print(" Сравнение равен к 3")
# else:
#     print("Сравнение не равен к 3")
#
# Задача № 4 Четное нечетное число
#
# num =int(input("Введите число:"))
# mod = num % 2
# if mod > 0:
#     print("Это нечетное число")
# else:
# #     print("Это четное число")
#
#
# Задача № 5
# Перебирание меньше 5 числа
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for num in a:
#     if num < 5:
#         print(num)
#
# Задача №6 Элементы для общего списка
#
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# set_a = set(a)
# set_b = set(b)
# common_elements = list(set_a & set_b)
# print(common_elements)
#
#
#message = "Hello Python world!"
# print(message)
#
# message = "Hello Python world!"
# print(message)
# message = "Hello Python Crash Course world!"
# print(message)
#
# name = "ada lovelace"
# print(name.title())
# name = "Ada Lovelace"
# print(name.upper())
# print(name.lower())
# first_name = "ada"
# last_name ="lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(f"Hello, {full_name.title()}!")
# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# message = f"Hello, {full_name.title()}!"
#print(message)

# first_name = "ada"
# last_name = "lovelace"
# full_name = f"{first_name} {last_name}"
# print(full_name)
#
#first_name = "ada"
#last_name = "lovelace"
# name =f"Hello,{first_name} {last_name}!"
#print(first_name,last_name)
# full_name = "{} {}".format(first_name, last_name)
# full_name = "{} {}".format(first_name, last_name)
#
#
# print("\tPython")
# print("Languages:\nPython\nC\nJavaScript")
#
# favorite_language = " python  "
#
# favorite_language = favorite_language.rstrip()
# print(favorite_language)
#
# favorite_language = 'python'
# favorite_language.lstrip()
# print(favorite_language)

# message = "One of Python's strengths is its diverse community."
# print(message)
#
# message = 'One of Python's strengths is its diverse community.'
# print(message)

# def greet():
#     print("Привет, мир!")
#
# greet()

# universe_age = 14_000_000_000
# print(universe_age)

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
#print(bicycles[0].title())
# print(bicycles[1])
# print(bicycles[3])
#print(bicycles[-1])

# motorcycles = ['honda', 'yamaha', 'suzuki']
# motorcycles.append('ducati')
#
# print(motorcycles)
#
# motorcycles = []
# motorcycles.append('honda')
# motorcycles.append('yamaha')
# motorcycles.append('suzuki')
# print(motorcycles)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# print(motorcycles)
# popped_motorcycle = motorcycles.pop()
# print(motorcycles)
# print(popped_motorcycle)

# motorcycles = ['honda', 'yamaha', 'suzuki']
# last_owned = motorcycles.pop()
# print(f"The last motorcycle I owned was a {last_owned.title()}.")

# motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
# print(motorcycles)
# too_expensive = 'ducati'
# motorcycles.remove(too_expensive)
# print(motorcycles)
# print(f"\nA {too_expensive.title()} is too expensive for me.")

# def greet_user():
#     print("Hello!")
# greet_user()

# def mergeAlternately(self,word1:str,word2:str) → str:
#     result = ""
#     for w1, w2 in zip(word1, word2):
#         result += w1 + w2
# result += word1[len(word2):] + word2[len(word1):]
# return result


# def canPlaceFlowers(self, flowerbed: list[int], n: int) →bool:
#      count_new_flowers = 0
#      for i in range(len(flowerbed)):
#     if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
#         flowerbed[i] = 1
#         count_new_flowers += 1
#
#     if count_new_flowers >= n:
#      rerurn True
# else:
#        rerurn False
#
# def merge_strings(word1, word2):
#     result = []
#     min_len = min(len(word1), len(word2))
#
#     for i in range(min_len):
#         result.append(word1[i])
#         result.append(word2[i])
#
#         result.append(word1[min_len:])
#         result.append(word2[min_len:])
#
#         return ''.join(result)
#
# word1 = "abc"
# word2 = "pqr"
# print(merge_strings(word1, word2))


# def gcdOfStrings(self, str1: str, str2: str) -> str:
#     if str1 + str2 != str2 + str1:
#         return ""
# def gcd(a, b):
#         while b:
#          a, b = b, a % b
#         return a
#
#
#         gcd_len = gcd(len(str1), len(str2))
#         return str1[:gcd_len]
#
# gcdOfStrings ("ab","rs","pqrs")
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
# word1 = "abc"
# word2 = "pqr"


# def was_package_received_yesterday(tz_from, tz_to, start, duration):
#        assert_equals(was_package_received_yesterday(1, 5, 6, 3), False, "East to zone 12 should return False (to is greater than from)")
#        assert_equals(was_package_received_yesterday(-11, -8, 3, 12), False, "East to zone 12 should return False (to is greater than from)")
#     it("West past midnight should return True")

# def greet_user():
#      print("Hello!")
#
# greet_user()
#
# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
#
# favorite_book ("Alice in Wonderland")

# def favorite_book(title):
#     print(f"One of my favorite books is {title}")
#
# favorite_book("Alice in Wonderland")

# def greet_user(g_safar):
#     print(f" Hello,{g_safar}")
#
# greet_user ('Gulzina')

# def describe_pet(animal_type, pet_name):
#  """Выводит информацию о животном."""
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")
#
# describe_pet()

# def make_shirt(size ,text):
#     print(f"{size} Ты сможешь, {text.title()}")
#
# make_shirt("35", "мой любимый ")


# def favorite_book(title):
#    print(f"One of my favorite books is {title}")
# favorite_book (" fjhkdh")

# def ake_shirt(size="L", text="I love Python"):
#    print(f"The size of the shirt is {size} and the text on it is: '{text}'")
#
# ake_shirt ()

# def make_shirt(size, text = "Code is Life"):
#      print(f"The {size} of the shirt and the text on it is: {text}.")
#
# make_shirt(size = "M")

# def reverseVowels(self, s: str) -> str:
#     vowels = "aeiouAEIOU"
#     left = sorted([k for k in vowels if k % 2 == 0], reverse=True)
#     right = sorted([ k for  k in vowels if k%2 ==1])
#
#     result = left + right
#
#     return result
#
# result ="IceCreAm"
# print(result)


# def reverseVowels(s: str) -> str:
#     vowels = "aeiouAEIOU"
#     s = list(s)
#
#     left, right = 0, len(s) - 1
#     while left < right:
#         if s[left] not in vowels:
#             left += 1
#         elif s[right] not in vowels:
#             right -= 1
#         else:
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#
#     return ''.join(s)
#
# result = reverseVowels("IceCreAm")
# print(result)

#
# def reverseVowels(s: str) -> str:
#     vowels = set('aeiouAEIOU')
#     s = list(s)
#     left, right = 0, len(s) - 1
#
#     while left < right:
#         if s[left] in vowels and s[right] in vowels:
#
#             s[left], s[right] = s[right], s[left]
#             left += 1
#             right -= 1
#         elif s[left] not in vowels:
#             left += 1
#         else:
#             right -= 1
#
#     return ''.join(s)
#
#
#
# s = "leetcode"
# print(reverseVowels(s))

# magicians = ['alice', 'david', 'carolina']
# for i in magicians:
#  print(i) # Для каждого фокусника в списке вывести его имя

# magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(f"{magician.title()}, that was a great trick!")
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print("Thank you, everyone. That was a great magic show!")

# my_pizza =['peperoni', 'chili', 'simple']
# for pizza in my_pizza:
#     print(pizza)

# my_pizza = ['peperoni', 'chili', 'simple']
# for pizza in my_pizza:
#     print(f'I like {pizza} pizza')
# print("I really love pizza!")

# for numbers in range (1,20): # Последовательность чисел
#     print(numbers)
#
# for numbers in range (1,20):
#       if numbers %2 == 0: # Четная столбиком. нужно заглушить нечетную внизу строчку.
#          numbers += 1  # Нечетная столбиком.
#          print (numbers)
#
# even_numbers = list(range(2,20,2)) # Четная (1,20,2) - нечетная по горизонтали.
# print(even_numbers)

#
# class Dog():
#
#
#      def __init__(self, name, age):
#            self.name = name
#            self.age = age
#
#      def sit(self):
#          print(f"{self.name} is now sitting.")
#
#      def roll_over(self):
#          print(f"{self.name} rolled over!")
#
# my_dog = Dog('willie', 6)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
#
# my_dog = Dog('willie', 6)
# your_dog = Dog('lucy', 3)
# print(f"My dog's name is {my_dog.name}.")
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# print(list(filter(lambda elem: elem < 5, a)))
# print([elem for elem in a if elem < 5])

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,]
# result = []
# for elem in a:
#     if elem in b:
#         result.append(elem)
# print(result)

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# for elem in a:
#     if elem <5:
#         print(elem)

# books = {1:2, 2:3, 3:4}
# print(sorted(books.values()))
# books = sorted(books.values())
# print(books)

# numbers = [ 32,44,11,True, 'odd',False]
# print(numbers[0],numbers[-1])
# print(f'Первый:{numbers[0]}, Последний:{numbers[-1]}')

# a = int(input('Введите число:'))
# for i in range(1, a + 1):
#     print(str(i) *i)

#numbers = [52, 12, 47,332, 11, 237, 90, 54]
# for el in numbers:
#     if el == 237:
#         break
#     if el % 2 == 0:
#         print(el)

# numbers1 = [ 52,11,21,90,78,66]
# numbers2 = [76,55,14,21,90,78,33]
# result = []
# for num in numbers1:
#     if num in numbers2:
#         result.append(num)
# print(result)

# elements = [ 9.2, 'st', 5, 12, 9.21, 2]
# sum_element = 0
# for i in elements:
#     if type(i) == int:
#         sum_element += i
# print(sum_element)

# word = 'aziza'
# c = 0
# my_letter = input('Введите символ:')
# for i in word:
#     if i == my_letter:
#         c += 1
# print(f'Буква {my_letter}  встречается {c} раз')
#
# person_1 = {
#     'name': 'Jen',
#     'age': 28,
#     'city': 'New York',
#     'favorite_languages': ['python', 'ruby']
# }
#
# person_2 = {
#     'name': 'Sarah',
#     'age': 25,
#     'city': 'Los Angeles',
#     'favorite_languages': ['c']
# }
#
# person_3 = {
#     'name': 'Edward',
#     'age': 30,
#     'city': 'Chicago',
#     'favorite_languages': ['ruby', 'go']
# }
#
# # Сохраняем все три словаря в списке
# people = [person_1, person_2, person_3]
#
# # Перебираем список людей и выводим информацию о каждом человеке
# for person in people:
#     print(f"Name: {person['name']}")
#     print(f"Age: {person['age']}")
#     print(f"City: {person['city']}")
#     print("Favorite Languages:")
#     for language in person['favorite_languages']:
#         print(f"\t{language.title()}")
#     print()  # Пустая строка для разделения выводов между людьми

''' Сырая довести!!!!'''
#
# weeks = 0
# for i in range(1,8):
#     a = int(input(f'выручка за день {i}:'))
#     weeks += a
#     print('Средняя выручка за недель:', weeks /7)

''' Домашняя работа '''
''' Напишите программу кот.выводит числа от 1 до 100.
Для чисел кратных 3 - Fizz, 5 кратных - Buzz
а для 3 и 5 = FizzBuzz'''

number = []
number1 = []
number2 = []

for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        number.append(i)
    elif i % 3 == 0:
        number1.append(i)
    else:
        number2.append(i)

print(f'FizzBuzz: {number}\n')
print(f'Fizz: {number1}\n')
print(f'Bizz:{number2} \n')

'''№ 2 Нап.функ.кот. проверяет являютя ли 2 строки анаграммами'''

def are_anagrams (word1,word2):
    word1 =word1.replace(" ", " ").lower()
    word2 = word2.replace (" " , " ").lower()
    return sorted(word1) == sorted(word2)
word1 = "listen"
word2 = "silent"
print(are_anagrams(word1,word2))

'''№ 3 Нап.функ.которая подсчитывает кол-во каждого символа в строке '''

def count_symvol (string):
    quantity_symvol ={}

    for i in string:
        quantity_symvol[i] =quantity_symvol.get(i, 0)+1
    return  quantity_symvol

string = "gulzina"
print(count_symvol(string))

'''№ 4 Нап.функ.кот.возвращает список всех простых чисел
до заданного числа n'''

def get_prime_numbers(n):
    primes = []
    for num in range(2, n +1):
        is_prime =True
        for i in range (2,int( num ** 0.5)+1):
            if num  % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes
n = 20
print(get_prime_numbers(n))

'''№ 5 Реализуйте функ. вычисляющую  факториал числа с использованием
рекурсии и итерации.'''

def factorial_iterative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

n =5
print(factorial_iterative(n))










































































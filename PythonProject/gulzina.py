
''' Отсор.словарь по занчению убывание/возраст ??? '''
#a ={'a':2, 'b':3, 'c': 4}
#print(sorted.{a}values())

# '''отсорт.три ключа самым высоким значениям в словаре ???''
# my_dict ={'a':500, 'b':5874, 'c':560, 'd':400,'e':5874, 'f':20}
# num =[]
# for num in my_dict.values():
#    my_dict= max(my_dict)
#    print({my_dict})

'''  '''
# friends = {'Aizhan', 'Gulzat', 'Meerim', 'Zhiydegul', 'Aigerim'}
# my_friends = {'Kanykey', 'Gulzat', 'Aibiyke', 'Zhiydegul', 'Aruuke'}
# if my_friends in friends:
#   print("Aizhan, Gulzat есть в спсике")
# else:
#   print("Aizhan ,Gulzat нет в спсике")

# print(set(friends ))
#
# my_friends = {'Каныкей', 'Гүлзат', 'Айбийке', 'Жийдегүл', 'Арууке', 'Каныкей'}
# only_friends= []
# for i in my_friends:
#   if i not in only_friends:
#     only_friends.append(i)
#
# print(only_friends)

# friends = {'Айжан', 'Гулзат', 'Мээрим', 'Жийдегүл', 'Айгерим'}
# a = 'Айжан'
# b = 'Гулзат'
# if a and b not in friends:
#   print ('Они не в джрузях')
# else:
#   print('они в друзях')
#
#

# alien_0 = {'color': 'green' , 'points': 5}
# print(alien_0['color'])
# print(alien_0['points'])
# alien_0 ={'color': 'green', 'points': 5}
# print(alien_0)
#
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(ailen_0)
# alien_0 ={}
# alien_0['color'] = 'green'
# alien_0['points'] = 5
# print(alien_0)
# alien_0 = {'color':'green'}
# print(f"The alien is {alien_0['color']}.")
# alien_0['color'] = 'yellow'
# print(f"The alien is now {alien_0['color']}")

# alien_0 = {'x_position': 0,'y_position': 25,'speed': 'medium'}
# print(f"Original position:{alien_0['x_position']}")
# alien_0['speed'] = 'fast'
# if alien_0['speed'] == 'slow':
#     x_increment = 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2
# else:
#     x_increment =3
#
# alien_0['x_position'] = alien_0['x_position'] + x_increment
# print(f"New position: {alien_0['x_position']}")

# alien_0 ={'color': 'green','points': 5}
# print(alien_0)
#
# del alien_0['points']
# print(alien_0)

# favorite_languages ={
#   'Jen': 'python',
#   'Sarah': 'C',
#   'Edvard': 'ruby',
#   'Fill': 'python',
#    }
# language = favorite_languages['Sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# alien_0 = {'color': 'green','speed': 'slow'}
# point_value = alien_0.get('points', 'Балловое значение не присвоено')
# print(point_value)

# zina_names ={'first name':'Gulina',
#              'last name':'Appaz',
#              'city':'Bishkek',
#              'age': 35,
#              }
# print(f"Имя:{zina_names['first name']}")
# print(f"Фамилия:{zina_names['last name']}")
# print(f"Возраст:{zina_names['age']}")
# print(f"Город:{zina_names['city']}")

# for elem in zina_names.items():
#  print(f"Каждое {elem} это данные{zina_names}")

# favorite_numbers = {'Alice': 7,
#                     'Tom': 5,
#                     'Sam': 14,
#                     'Mira': 20,
#                     'Zina': 18,}
#
# for i, j in favorite_numbers.items():
#   print(f"У {i} любимое число {j}")

# terms ={'Переменная': 'ящик для храненияю',
#         'Циклы':'проходит по всем элементам',
#         'Кортеж':'всегда незменяемый',
#         'Условие': 'проверяет истинно или ложь',
#         'Методы':'Помогают ту или в ином действии',
#         }
# for word,definition in terms.items():
# print(f"{word}: \n {definition} \n")

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#      }
# for name in favorite_language.keys():
#     print(name.title())

# friends =['phil', 'sarah']
# for name in favorite_language.keys():
#     print(name.title())
#
#     if name in friends:
#         language = favorite_language[name].title()
#         print(f'{name.title()},I see you love {language}!')
#
# if 'erin' not in favorite_language.keys():
#     print('Erin, please take our poll!')
# for name in sorted (favorite_language.keys()):
#     print(f"{name.title()}, thank you for talking the poll.")
# print("The following languages has been mentioned:")
# for language in favorite_language.values():
#     print(language.title())

# for language in set(favorite_language.values()):
#     print(language.title())

# river_w = {'nile': 'egypt','amazon': 'brazil','yantsy': 'china'}
# for river, country in river_w.items():
#     print(f"The {river.title()} runs throught {country.title()}.")
# for river in river_w.keys():
#     print(river.title())
# for country in river_w.values():
#     print(country.title())

# favorite_language = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python',
#      }
# friends = ['edward', 'jen','amanda','tom','phil','lili']
# for name in friends:
#      if name in favorite_language:
#          print(f"{name.title()} thank you, you have already completed the survey" )
#      else:
#          print(f"{name.title()} I suggest you take part in the issue")

# alien_0 ={'color':'green','points':5}
# alien_1 = {'color':'yellow','points':10}
# alien_2 ={'color':'red','points':15}
# aliens =[alien_0,alien_1,alien_2]
# for alien in aliens:
#     print(alien)
# aliens =[]
# for alien_number in range(30):
#     new_alien ={'color':'green','points': 5,'speed':'slow'}
#     aliens.append(new_alien)
# for alien in aliens [:5]:
#     print(alien)
# print("Новый пришелец")
# print(f"Total number of aliens:{len(aliens)}")

# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'yellow', 'points': 10}
# alien_2 = {'color': 'red', 'points': 15}
#
# aliens = []
# for alien_number in range(30):
#     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#     aliens.append(new_alien)
#
#     for alien in aliens[0:3]:
#         if alien['color'] == 'green':  # Если инопланетянин зеленый
#             alien['color'] = 'yellow'
#             alien['speed'] = 'medium'
#             alien['points'] = 10
#         elif alien['color'] == 'yellow':  # Если инопланетянин стал желтым
#             alien['color'] = 'red'
#             alien['speed'] = 'fast'
#             alien['points'] = 15
#
#     # Проверим результат
# for alien in aliens[0:3]:
#     print(alien)

# pizza ={'crust':'thick',
#         'toppings':['mushrooms','extra cheese'],
#         }
# print(f"You ordered a pizza {pizza['crust']}- crust pizza"
#        "with the following toppings:" )
#
# for topping in pizza['toppings']:
#     print("\t" + topping)

# favorite_languages ={
#     'jen':['python','ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell']
#      }
#
# for name, languages in favorite_languages.items():
#      if len(languages) >1:
#        print(f"\n{name.title()}'s favorite languages are:")
#        for language in languages:
#          print(f"\t{language.title()}")
#      else:
#          print(f"\n {name.title()}'s favorite languages is {languages[0].title()}")

# users ={'aienstein':{'first':'albert','last':'einstein','location':'princeton'},
#         'mcurie':{'first':'marie','last':'curie','location':'paris'}}
#
# for username, user_info in users.items():
#     print(f"\n Username:{username}")
#     full_name = f"{user_info['first']} {user_info['last']}"
#     location =user_info['location']
#     print(f"\t Full name:{full_name.title()}")
#     print(f" \t Location:{location.title()}")
#
# person_1 = {
#           'name':'jen',
#            'age': 28,
#            'city': 'new york',
#            'favorite_languages':['python', 'ruby']
# }
#
# person_2 = {
#            'name': 'sarah',
#             'age': 25,
#             'city':'Los Angeles',
#             'favorite_languages':['c']
# }
#
# person_3 ={'name':'edward','age': 30,'city':'Chicago','favorite_languages':['ruby','go']}
#
# people =[person_1,person_2,person_3]
# for person in people:
#     print(f"Name:{person['name']}")
#     print(f"Age:{person['age']}")
#     print(f"City:{person['city']}")
#     print(f"favorite_languages:")
#
#     for language in person ['favorite_languages']:
#         print(f'\t{language.title()}')
#     print()

''' Предварительный хакатон № 1'''

'''Напишите функцию is_even  кот.принимает целое число  n  и возвращает
True, если n является четным числом, иначе возвращает False.'''
# def is_even(num):
#     if num  % 2 ==0:
#         return True
#     else:
#        return False
#
# print(is_even(8))
# print(is_even(45))

'''напишите функцию find_prime_numbers (start, end ) 
находит все простые числа в диапазоне от start до end 
и возвращает их в виде списка.'''

def find_prime_numbers(start, end):
    prime_numbers = []

    for num in range(start, end + 1):  # Проходим по всем числам от start до end
        if num > 1:  # Проверяем, что число больше 1 (так как 1 не является простым числом
            is_prime = True
            for i in range(2, num):  # Проверяем делители от 2 до num-1
                if num % i == 0:  # Если находим делитель, число не простое
                    is_prime = False
                    break
            if is_prime:
                prime_numbers.append(num)

    return prime_numbers
print(find_prime_numbers(1, 50))


''' Мини Хакатон № 2'''
#
# word = "Welcome to Python"
# new_word = word.replace("to Python","ring to tayler")
# print(new_word.upper())
# print(new_word [::-1])

# word ="Welcome to Python"
# new_word = word.replace("to Python","ring to tyler")
# print(new_word.upper())
# print(new_word[::-1].title())

''' Второе задание'''
# kilometres = 3 '''Основа примера'''
# miles = kilometres * 0.621
# print(miles)
# name = input("Введите имя:")
# distance =float(inpunt("Введите расстояние:"))
# miles =distance * 0.621
# print(f"{name.title()} приветствую тебя, ты прошел {miles} миль")

# week_1 = [5, 7, 25, 10, 30,15,7,10,15,7,30,20,25]
# a = int(input('введите число:'))
# week_1.append(a)
# profit = 150
# total_sales =[]
# print(week_1)
#
# for sale in week_1:
#    total_sales.append(sale * profit)
# print('total:', [total_sales])
# best_day = max( total_sales)
# worst_day = min(total_sales)
# print(f"Лучший день:", {best_day})
# print(f"Худший день:", {worst_day})





































































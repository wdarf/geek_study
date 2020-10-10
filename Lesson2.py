#Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
#элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать
#явно, в программе.
new_list = [False, 2.36, 666, 'random txt']
def show_type(el):
    for el in range(len(new_list)):
        print(type(new_list[el]))
    return
show_type(new_list)


#Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3
#и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов необходимо
#использовать функцию input().
list_elements = int(input("Введите количество элементов списка:"))
new_list = []
x = 0
el = 0
while x < list_elements:
    new_list.append(input("Введите элемент списка"))
    x += 1
for i in range(int(len(new_list)/2)):
    new_list[el], new_list[el + 1] = new_list[el + 1], new_list[el]
    el += 2
print(new_list)


#Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима, весна,
#лето, осень). Напишите решения через list и через dict.
seasons_list = ["winter", "spring", "summer", "fall"]
seasons_dict = {1: "winter", 2: "spring", 3: "summer", 4: "fall" }
month = int(input("Введите номер месяца"))
if month in [1, 2, 12]:
    print(seasons_list[0])
    print(seasons_dict.get(1))
elif month in [3, 4, 5]:
    print(seasons_list[1])
    print(seasons_dict.get(2))
elif month in [6, 7, 8]:
    print(seasons_list[2])
    print(seasons_dict.get(3))
elif month in [9, 10, 11]:
    print(seasons_list[3])
    print(seasons_dict.get(4))
else:
    print("There is no such month number")


#Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
#необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
stroka = input("Введите несколько слов через пробел")
new_word = []
num = 1
for el in range(stroka.count(' ') + 1):
    new_word = stroka.split()
    if len(str(new_word)) <= 10:
        print(f" {num} {new_word [el]}")
        num += 1
    else:
        print(f"{num} {new_word [el] [0:10]}")
        num += 1


#Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя необходимо
#запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем
#же значением должен разместиться после них.
#Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
#Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
#Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
#Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
#Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (123 - для завершения): "))
while digit != 123:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        if my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and new_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"Текущий рейтинг - {my_list}")
    digit = int(input("Введите число "))
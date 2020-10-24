"""1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка."""


with open("lesson5-1.txt", "w", encoding="UTF-8") as out_file:
    line = input("Type some random text: \n")
    while line:
        out_file.writelines(line + "\n")
        line = input("Type some random text: \n")
        if not line:
            break


"""2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке."""


with open("lesson5-2.txt", "w+", encoding="UTF-8") as out_file:
    line = ["Some\n", "random\n", "text\n", "AGAIN!\n"]
    out_file.writelines(line)
with open("lesson5-2.txt") as f:
    print("Количество строк в файле равно ", sum(1 for _ in f))


"""3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.:"""


with open("lesson5-3.txt", "r", encoding="UTF-8") as out_file:
    workers = {}
    all_salary = 0
    count = 0
    for line in out_file:
        key, value = line.split()
        workers[key] = value
        if int(value) < 20000:
            print(f"{key}: зарплата меньше 20000")
        salary = line.split()
        all_salary += int(salary[1])
        count += 1
average_salary = all_salary // count
print(f"Средняя величина дохода сотрудников составила: {average_salary}")


"""4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл."""


rus_nums = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_out_file = []
with open("Lesson5-4.txt", "r", encoding="UTF-8") as out_file:
    for i in out_file:
        i = i.split(" - ", 1)
        new_out_file.append(rus_nums[i[0]] + " - " + i[1])
with open("Lesson5-4.1.txt", "w", encoding="UTF-8") as out_file_2:
    out_file_2.writelines(new_out_file)


"""5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. Программа 
должна подсчитывать сумму чисел в файле и выводить ее на экран."""

with open("Lesson5-5.txt", "w+", encoding="UTF-8") as out_file:
    lines = input("Введите набор чисел через пробел: \n")
    out_file.write(lines)
    number = lines.split()
    print(f"Сумма введенных вами чисел составляет: {sum(map(int, number))}")


# """6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие
# лекционных, практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета не
# обязательно были все типы занятий. Сформировать словарь, содержащий название предмета и общее количество занятий по
# нему. Вывести словарь на экран.
# Примеры строк файла:
#
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря:
#
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}"""
#
# import re
#
# def my_func():
#     my_str = input("Введи числа и слова: ")
#     my_str = re.sub(r"[a-zа-я()]", "", my_str)
#     number = my_str.split()
#     return f"Сумма введенных вами чисел составляет: {sum(map(int, number))}"
#
# print(my_func())



"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, форма
собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила
убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста."""
import json

profit = {}
avg_profit = {}
prof = 0
prof_avg = 0
i = 0
with open("lesson5-7.txt", "r", encoding="UTF-8") as out_file:
    for line in out_file:
        firma, firm, earning, cost = line.split()
        profit[firma] = int(earning) - int(cost)
        if profit.setdefault(firma) >= 0:
            prof = prof + profit.setdefault(firma)
            i += 1
    if i != 0:
        prof_avg = prof / i
        print(f'Средняя прибыль фирм - {prof_avg:.2f}')
    else:
        print(f'Прибыль отсутствует. Идет работа в убыток')
    avg_profit = {'Средняя прибыль составила': round(prof_avg)}
    profit.update(avg_profit)
    print(f'Прибыль каждой компании - {profit}')
with open('Lesson5-7.json', 'w', ensure_ascii=False) as write_js:
    json.dump(profit, write_js)
    js_str = json.dumps(profit)
    print(f'Создан json-объект: \n 'f' {js_str}')
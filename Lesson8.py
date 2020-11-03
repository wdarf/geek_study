"""
1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год и
преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.
"""
from datetime import date


class Data:
    def __init__(self, data):
        self.data = data.split("-")

    @classmethod
    def get_data(cls, data):
        try:
            day, month, year = [int(i) for i in data.split("-")]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return "Указана неправильная дата"

    @staticmethod
    def check(data):
        try:
            day, month, year = data.split("-")
            date(int(year), int(month), int(day))
            return "Дата указана верно"
        except ValueError:
            return "Указана неправильная дата"


print(Data.check("02-11-2020"))
print(Data.get_data("02-11"))


"""
2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных, 
вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту 
ситуацию и не завершиться с ошибкой.
"""


class DivisionByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = DivisionByNull(10, 5)
print(DivisionByNull.divide_by_null(10, 2))
print(DivisionByNull.divide_by_null(10, 0.5))
print(div.divide_by_null(100, 0))

"""
3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел. Проверить 
работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и заполнять список. Класс-исключение
должен контролировать типы данных элементов списка.
Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу 
скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный список выводится на экран.
Подсказка: для данного задания примем, что пользователь может вводить только числа и строки. При вводе пользователем 
очередного элемента необходимо реализовать проверку типа элемента и вносить его в список, только если введено число. 
Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение. При 
этом работа скрипта не должна завершаться.
"""


class MyError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_value
        while True:
            try:
                try:
                    user_value = int(input("Введите числа: "))
                    ex = input(f"'Добавляем '{user_value}' в список.Для продолжения жмите y, завершить - n: ").lower()
                    self.my_list.append(user_value)
                    if ex == "n":
                        print(self.my_list)
                        break
                except ValueError:
                    raise MyError
            except MyError:
                ex = input(f"Вы ввели не число! Хотите продолжить? y/n: ").lower()
                if ex == "n":
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника», 
который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс). В 
базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры, 
уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в 
определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других 
данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для 
указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на 
уроках по ООП.
"""
class StoreMashines:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {"Модель устройства": self.name, "Цена за ед": self.price, "Количество": self.quantity}

    def __str__(self):
        return f"{self.name} цена {self.price} количество {self.quantity}"

    def reception(self):
        try:
            unit = input(f"Введите наименование ")
            unit_p = int(input(f"Введите цену за ед "))
            unit_q = int(input(f"Введите количество "))
            unique = {"Модель устройства": unit, "Цена за ед": unit_p, "Количество": unit_q}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f"Текущий список -\n {self.my_store}")
        except:
            return f"Ошибка ввода данных"

        print(f"Для выхода нажмите - Q, для продолжения - Enter")
        q = input(f"---> ")
        if q == "Q" or q == "q":
            self.my_store_full.append(self.my_store)
            print(f"Весь склад -\n {self.my_store_full}")
            return f"Выход"
        else:
            return StoreMashines.reception(self)


class Printer(StoreMashines):
    def to_print(self):
        return f"Печатать {self.numb} раз"


class Scanner(StoreMashines):
    def to_scan(self):
        return f"Сканировать {self.numb} листов"

class Copier(StoreMashines):
    def to_copier(self):
        return f"Сделать  {self.numb} копий"


unit_1 = Printer("Canon Pixma", 4500, 6500, 10)
unit_2 = Scanner("Epson V", 10, 2500, 10)
unit_3 = Copier("Kyocera EcoSYS", 3540, 42000, 15)
print(unit_1.reception())
print(unit_2.reception())
print(unit_3.reception())
print(unit_1.to_print())
print(unit_3.to_copier())

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку 
методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные числа) и
выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return f"Сумма равна: {self.a + other.a} + {self.b + other.b} * i"

    def __mul__(self, other):
        return f"Произведение равно: {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i"


c_1 = ComplexNumber(4, -8)
c_2 = ComplexNumber(6, 11)
print(c_1 + c_2)
print(c_1 * c_2)
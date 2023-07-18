# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.

from dis import get_instructions


BASE_HEX = 16  
BASE_DEC = 10  
ASCII_START = 55  


def main():
    number: int
    numbers = []

    print('Введите числа для перевода в HEX.\n'
          'Отрицательное число - завершить ввод')
    while True:
        number = get_instructions('Введите число: ')
        if number < 0:
            break
        numbers.append(number)

    print(' число | моя функция | heh() ')
    print('-----------------------------')
    for i in numbers:
        print(f" {i:<5} | {dec_to_heh(i):11} | {hex(i)}")


# перевод числа в 16-ричное представление
def dec_to_heh(dec_num: int) -> str:
    hex_num: str = ""

    while dec_num:
        div_mod = dec_num % BASE_HEX
        hex_num = (chr(div_mod + ASCII_START) if div_mod >= BASE_DEC else str(div_mod)) + hex_num
        dec_num //= BASE_HEX

    return '0x' + (hex_num if hex_num else "0")

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

import fractions


def main():
    fract_1 = get_str("Введите 1-ю дробь: ")
    fract_2 = get_str("Введите 2-ю дробь: ")

    print("Мои методы:")
    print(f"{fract_1} + {fract_2} = {fract_sum(fract_1, fract_2)}")
    print(f"{fract_1} * {fract_2} = {fract_milt(fract_1, fract_2)}")

    print("Проверочные методы:")
    print(f"{fract_1} + {fract_2} = {fractions.Fraction(fract_1) + fractions.Fraction(fract_2)}")
    print(f"{fract_1} * {fract_2} = {fractions.Fraction(fract_1) * fractions.Fraction(fract_2)}")


# сумма дробей
def fract_sum(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # ищем НОК, приводим к общему знаменателю
    fract_lcm = my_lcm(fract_1_part[1], fract_2_part[1])
    # добавочные множители для приведения к единому знаменателю
    mult_1 = int(fract_lcm / fract_1_part[1])
    mult_2 = int(fract_lcm / fract_2_part[1])
    fract_1_part = [i * mult_1 for i in fract_1_part]
    fract_2_part = [i * mult_2 for i in fract_2_part]
    # сложение дроби
    fract_1_part[0] += fract_2_part[0]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# приведение дроби из строкового представления к списку чисел
# [числитель, знаменатель]
def split_fraction(fract: str) -> list:
    fraction_parts = fract.split("/")
    fraction_parts = [int(s) for s in fraction_parts]
    return fraction_parts


# произведение дробей
def fract_milt(fract_1: str, fract_2: str) -> str:
    # получение числителей и знаменателей из дробей
    fract_1_part = split_fraction(fract_1)
    fract_2_part = split_fraction(fract_2)
    # умножение дробей
    fract_1_part[0] *= fract_2_part[0]
    fract_1_part[1] *= fract_2_part[1]

    return str(fract_1_part[0]) + "/" + str(fract_1_part[1])


# Поиск НОД
def my_gcd(num_1: int, num_2: int) -> int:
    if num_1 < num_2:
        num_1, num_2 = num_2, num_1

    while num_2:
        num_1 %= num_2
        num_1, num_2 = num_2, num_1

    return int(num_1)


# Поиск НОК
def my_lcm(num_1: int, num_2: int) -> int:
    return int(num_1 / my_gcd(num_1, num_2) * num_2)


# Запрос строковой величины
def get_str(message: str = None) -> str:
    if message is None:
        message = "Введите строку: "
    return input(message)


# Старт
if __name__ == "__main__":
    main()
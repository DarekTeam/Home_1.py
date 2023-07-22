#Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
#не должно быть дубликатов.

from tkinter.ttk import Style


def only_double(my_list: list) -> list:
    return list(set(filter(lambda x: my_list.count(x) > 1, my_list)))

#В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
#Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

def ten_popular(text: str) -> list[str]:
    delete = ".,!?;:-[]{}()='"
    for i in delete:
        text = text.replace(i, "")
    text = text.lower()
    return sorted(set(text.split()), key=lambda x: text.count(x))[-10:]

#Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. Определите какие
#вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант.

def backpack(shop: dict[str:int], size: int) -> list[list[str]]:
    # result = []
    # for elements in shop:
    #     if size > shop[elements]:
    #         result.append(elements)
    #         size = size - int(shop[elements])
    #     else:
    #         break
    # print(result)
    pcs, weight = zip(*sorted(shop.items(), key=lambda x: x[1], reverse=True))
    result, temp, temp_w = [], [], 0
    for index, w in enumerate(weight, 0):
        temp_w += w
        temp.append((pcs[index]))
        for index_n, wn in enumerate(weight[index:], index):
            if wn + temp_w <= size:
                temp_w += wn
                temp.append(pcs[index_n])
        result.append(temp)
        temp, temp_w = [], 0
    return result


def run():
    text_command = """
1 - Проверка дублирующимися элементами
2 - Подсчитать количество встречаемых слов и вернуть 10 самых частых
3 - Определите какие вещи влезут в рюкзак
4 - Выход из программы
Сделайте Ваш выбор:
"""
    while True:
        command = input(Fore.BLUE + text_command + Style.RESET_ALL)
        if command == '4':
            break

        if command == '1':
            my_list = list(input('Введите значения разделяя пробелом: ').split())
            # my_list1 = [1, 3, 5, 3, 5, "tru", "tru", "test", 3]
            print(my_list)
            # print(my_list1)
            print(only_double(my_list))
            # print(only_double(my_list1))

        if command == '2':
            text_str = "Словари Python — нечто совершенно иное; они вообще не являются последовательностями и" \
                       " взамен известны как отображения. Отображения также представляют собой коллекции других" \
                       " объектов, но они хранят объекты по ключам, а не по относительным позициям. " \
                       "В действительности отображения не поддерживают какой-либо надежный порядок слева направо;" \
                       " они просто отображают ключи на связанные значения. Словари — единственный тип" \
                       " отображения в наборе основных объектов Python — являются изменяемыми,’ как и списки," \
                       " их можно модифицировать на месте и они способны увеличиваться и уменьшаться по " \
                       "требованию. Наконец, подобно спискам словари — это гибкий инструмент для представления" \
                       " коллекций, но их мнемонические ключи лучше подходят, когда элементы коллекции именованы" \
                       " или помечены, скажем, как поля в записи базы данных."

            print(ten_popular(text_str))

        if command == '3':
            items = {'Мультитул': 500,
                     'Одеяло': 500,
                     'Котелок': 1000,
                     'Еда': 2500,
                     'Вода': 1000,
                     'Спички': 100,
                     'Палатка': 3000,
                     'Мешок': 2000,
                     }
            load_capacity = 10000
            print(backpack(items, load_capacity))
            # backpack(items, load_capacity)


if __name__ == "__main__":
    run()


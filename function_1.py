'''
Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0.
'''
def func_1(n_customers):
    # создадим пустой словарь, в который будем записывать номер группы и число участников группы
    groups = {}
    # в цикле пройдёмся по каждому номеру ID
    for i in range(n_customers+1):
        # на основе номера ID посчитаем группу, к которой пренадлежит данный ID
        # для этого преобразуем число в строку, из строки сделаем список символов, список символов преобразуем в список чисел, получис сумму чисел списка
        group = sum(map(int, list(str(i))))
        # прибавим одного участника к вычисленной выше группе, если группы не существует в словаре, то добавим её в словарь с количеством участников 1
        groups[f'group_{group}'] = groups.get(f'group_{group}', 0) + 1
    # вернём словарь
    return groups
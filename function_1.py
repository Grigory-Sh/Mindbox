'''
Функция, которая подсчитывает число покупателей, попадающих в каждую группу, если нумерация ID сквозная и начинается с 0.
'''
def func_1(n_customers):
    # создадим пустой словарь, в который будем записывать номер группы и число участников группы
    groups = {}
    
    # в цикле пройдёмся по каждому номеру IВ
    for i in range(n_customers):
        # на основе номера ID посчитаем группу, к которой пренадлежит данный ID
        # для номер группы положим равным нулю, а затем к нему будем прибалять остаток от деления на 10 номера ID (вычисляем сумму чисел ID)
        group = 0

        while i > 0:
            group += i % 10
            i //= 10
        # прибавим одного участника к вычисленной выше группе, если группы не существует в словаре, то добавим её в словарь с количеством участников 1
        groups[f'group_{group}'] = groups.get(f'group_{group}', 0) + 1
    
    # вернём словарь
    return groups
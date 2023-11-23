"""
    Немного поизвращался и решил задачу в процедурной с уклоном в декларативную парадигму,
    основное тело программы (начиная с 21 строки) выполнено в структурной парадигме.
    Процедурную парадигму выбрал для возможности переиспользования кода.
    Наверное правильнее будет сказать что это функциональная парадигма?
"""


def multi_list(n):
    return list(map(lambda x: '%d * %d = %d' % (n, x, (x * n)), [*range(1, 10)]))


def multi_list_rich(n):
    return list(map(multi_list, [*range(1, n)]))


def print_line(li):
    print(' || '.join(li))


if __name__ == '__main__':
    print('Таблица умножения для n:')
    print_line(multi_list(4))
    print('\nТаблица умножения от 1 до n:')
    list(map(print_line, multi_list_rich(4)))






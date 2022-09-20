def cicle_cost_collect(metrics_kit, collection):
    for i in metrics_kit:
        while True:
            try:
                cost = int(input(f'Оцените важность {i} от 1 до 10: '))
            except ValueError:
                print('Похоже, вы ввели не целое число, а что-то другое — так не пойдёт')
                continue

            if cost < 1 or cost > 10:
                print('Вы ввели значение, которое меньше 1 или больше 10 — оно не подойдёт. Попробуйте ещё раз')
                continue
            else:
                collection.append(cost)  # Convert the obtained values into convenient coefficients.
                break


def cicle_value_collect(metrics_kit, collection):
    for i in metrics_kit:
        while True:
            try:
                value = float(input(f'Введите среднее число {i} за период\n'))
            except ValueError:
                print('Похоже, вы ввели не целое число, а что-то другое — так не пойдёт')
                continue

            if value < 0:
                print('Вы ввели значение меньше 0 — оно не подойдёт. Попробуйте ещё раз')
                continue
            else:
                collection.append(value)
                break


def subscribers_collect():
    while True:
        try:
            subscribers = int(input('Сколько у вас подписчиков на конец исследуемого периода?\n'))
        except ValueError:
            print('Похоже, вы ввели не целое число, а что-то другое — так не пойдёт')
            continue

        if subscribers < 0:
            print('Вы ввели количество подписчиков меньше 0 — так не бывает. Попробуйте ещё раз')
            continue
        else:
            return subscribers

key_metrics = ['лайков', 'комментариев', 'репостов']
metric_costs = []

for i in key_metrics:
    while True:
        cost = input(f'Оцените важность {i} от 1 до 10\n')
        if float(cost) < 1 or float(cost) > 10:
            print('Вы ввели значение, которое меньше 1 или больше 10 — оно не подойдёт. Попробуйте ещё раз')
            continue
        else:
            metric_costs.append(cost)  # Convert the obtained values into convenient coefficients.
            break


metric_values = []

for i in key_metrics:
    while True:
        value = input(f'Введите среднее число {i} за период\n')
        if float(value) < 0:
            print('Вы ввели значение меньше 0 — оно не подойдёт. Попробуйте ещё раз')
            continue
        else:
            metric_values.append(value)
            break


while True:
    subscibers = input('Сколько у вас подписчиков на конец исследуемого периода?\n')
    if float(subscibers) <= 0:
        print('Вы ввели количество подписчиков меньше 0 — так не бывает. Попробуйте ещё раз')
        continue
    else:
        break


metric_results = []

for i in range(len(metric_values)):
    # Convert the obtained values into convenient coefficients.
    metric_results.append((int(metric_costs[i]) * int(metric_values[i])) / 10)


effective_engagement_index = (sum(metric_results) / float(subscibers)) * 100


print(key_metrics)
print(metric_costs)
print(metric_values)
print(subscibers)
print(metric_results)
print('Ваш индекс эффективного вовлечения: ' + str(effective_engagement_index) + '%')

important_metrics = ['просмотров', 'лайков', 'комментариев', 'репостов']
cost_metrics = []

for i in important_metrics:
    while True:
        cost = int(input(f'Оцените ценность {i} от 1 до 10'))
        if cost < 1 or cost > 10:
            print('Вы ввели неправильное значение. Попробуйте ещё раз')
            continue
        else:
            cost_metrics.append(cost)
            break


print(important_metrics)
print(cost_metrics)

important_metrics = ['просмотров', 'лайков', 'комментариев', 'репостов']
cost_metrics = []

for i in important_metrics:
    print(f'Оцените важность {i} от 1 до 10')
    cost = input()
    if int(cost) > 10 or int(cost) < 1:
        print('Вы указали недопустимое число')
    cost_metrics.append(cost)


print(important_metrics)
print(cost_metrics)

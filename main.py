from values_collector import *
from sheet_values import *

key_metrics = ['лайков', 'комментариев', 'репостов']

# Determining the importance of metrics.
metric_costs = []
cicle_cost_collect(key_metrics, metric_costs)

# Determination of average values by metrics.
means = means_list()

# Accepting the number of subscribers.
subscribers = subscribers_count()

# Convert the obtained values into convenient coefficients.
metric_results = []
for i in range(len(means)):
    metric_results.append(metric_costs[i] * means[i])

# Calculation of the Effective Engagement Index (EEI).
effective_engagement_index = (sum(metric_results) / subscribers) * 100

# Show the names of the studied values, they are costs.
m = 0
print('\nЗначит, изучаем значения:')
for i in key_metrics:
    print(f'- {i}. Важность метрики: {metric_costs[m]}.')
    m += 1

# Show the average values of key metrics from the loaded sheet.
k = 0
print('\nЗначения из вашей таблицы:')
for i in means:
    print(f'- среднее число {key_metrics[k]}: {i}.')
    k += 1
print(f'- подписчиков:', '{:,}'.format(subscribers).replace(',', ' ') + '.')

# Show Effective Engagement Index (EEI).
print('\nВаш индекс эффективного вовлечения: ' + str(round(effective_engagement_index, 2)) + '%')

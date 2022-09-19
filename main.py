from values_collector import *

key_metrics = ['лайков', 'комментариев', 'репостов']

# Determining the importance of metrics.
metric_costs = []
cicle_cost_collect(key_metrics, metric_costs)

# Determination of average values by metrics.
metric_values = []
cicle_value_collect(key_metrics, metric_values)

# Accepting the number of subscribers.
subscribers = subscribers_collect()

# Convert the obtained values into convenient coefficients.
metric_results = []
for i in range(len(metric_values)):
    metric_results.append((metric_costs[i] * metric_values[i]) / 10)

# Calculation of the Effective Engagement Index (EEI).
effective_engagement_index = (sum(metric_results) / subscribers) * 100


print(key_metrics)
print(metric_costs)
print(metric_values)
print(subscribers)
print(metric_results)
print('Ваш индекс эффективного вовлечения: ' + str(effective_engagement_index) + '%')

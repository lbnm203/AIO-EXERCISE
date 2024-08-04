import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("./Module2/Week4/StaticsforAI/advertising.csv")


def correlation(x, y):
    N = len(x)
    numerator = 0
    denominator = 0
    numerator = N * np.dot(x, y) - sum(x) * sum(y)
    denominator = np.sqrt(N * sum(x ** 2) - sum(x) ** 2) * \
        np.sqrt(N * sum(y ** 2) - sum(y) ** 2)
    return np.round(numerator / denominator, 2)


print("Cau5------------------------")
x = data['TV']
y = data['Radio']
corr_xy = correlation(x, y)
print(f" Correlation between TV and Sales : {round(corr_xy, 2)}")

print("Cau6------------------------")
features = ['TV', 'Radio', 'Newspaper']
for feature_1 in features:
    for feature_2 in features:
        correlation_value = correlation(data[feature_1], data[feature_2])
        print(f"Correlation between {feature_1} and {
              feature_2}: {round(correlation_value, 2)}")

print("Cau7------------------------")
x1 = data['Radio']
y1 = data['Newspaper']
result = np.corrcoef(x1, y1)
print(result)

print("Cau8------------------------")
print(data.corr())


print("Cau9------------------------")
plt.figure(figsize=(10, 8))
data_corr = data.corr()
sns.heatmap(data_corr, annot=True, fmt=".2f", linewidth=.5)
plt.show()

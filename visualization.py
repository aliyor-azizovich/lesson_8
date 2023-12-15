import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv

# df = pd.read_csv("california_housing_test.csv")
# columns = df.columns
# Изобразите отношение households к population с помощью точечного графика
# sns.scatterplot(data = df, x = "households", y = "population")

# Визуализировать longitude по отношения к median_house_value, используя линейный график

# sns.lineplot(data=df, x="longitude", y="median_house_value")

# Представить гистограмму по housing_median_age

# plt.hist(df['housing_median_age'])

# Изобразить гистограмму по median_house_value с оттенком housing_median_age

# sns.histplot(data = df, x = 'median_house_value', y = 'housing_median_age')

penguins = sns.load_dataset("penguins")
print(penguins.head())


plt.show()
# homework done

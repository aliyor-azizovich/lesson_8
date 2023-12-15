from pandas import *
import pandas as pd
data = pd.read_csv("california_housing_test.csv")
# print(type(data))
# print(data.shape)
# print(data.dtypes)
# print(data.info())
# print(data.isnull().sum())

# Показать median_house_value где median_income < 2
# filter = data[data["median_income"] < 2]["median_house_value"]
# print(filter)

# Показать данные в первых 2 столбцах
# result = data.iloc[:, :2]
# print(result)

# Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# filter = data[(data["housing_median_age"] < 20)&(data["median_house_value"] > 70000)]
# print(filter)

# Определить какое максимальное и минимальное значение median_house_value
# print(min(data["median_house_value"]))
# print(max(data["median_house_value"]))

# Показать максимальное median_house_value, где median_income = 3.1250
# print(max(data[data["median_income"] == 3.1250]["median_house_value"]))

# Узнать какая максимальная population в зоне минимального значения median_house_value
# res = data[data["median_house_value"] == data["median_house_value"].min()]["population"].max()
# print(res)

# Дан файл california_housing_test.csv. Определить среднюю стоимость дома (median_house_value), где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.

# filtered_df = data[data['population'] <= 500]
# avg = filtered_df['median_house_value'].mean()
# print(avg)
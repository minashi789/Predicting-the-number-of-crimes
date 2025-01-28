import pandas as pd
from dynamics import *
from analyticalalignment import * 
import numpy as np
import matplotlib.pyplot as plt
import os 


file = 'lab3.xlsx'
x1 = pd.ExcelFile(file)
print(x1.sheet_names)
df1 = x1.parse('Лист1')
print(df1.info)
mas1 = df1['Года'].values
mas2 = df1['Преступления'].values
base_absolute_increase1 = base_absolute_increase(mas2)
base_growth1 = base_growth(mas2)
base_increase1 = base_increase(mas2)
chains_absolute_increase1 = chains_absolute_increase(mas2)
chains_growth1 = chains_growth(mas2)
chains_increase1 = chains_increase(mas2)
avarage_level1 = avarage_level(mas2)
abs_avarage_level1 = abs_avarage_level(mas2)
growth_avarage_level1 = growth_avarage_level(mas2)
prediction_abs_avarage_increase1 = prediction_abs_avarage_increase(mas2)
prediction_growth_avarage_level1 = prediction_growth_avarage_level(mas2)
prediction_analytical_alignment1 = prediction_analytical_alignment(mas2)
avarage_increase_temp1 = avarage_increase_temp(mas2)

relative_accuracy1 = relative_accuracy(mas2)

df1['Базовый абсолютный прирост'] = [None] + base_absolute_increase1
df1['Базовый рост'] = [None] + base_growth1
df1['Базовый прирост'] = [None] + base_increase1

df1['Цепной абсолютный прирост'] = [None] + chains_absolute_increase1
df1['Цепной рост'] = [None] + chains_growth1
df1['Цепной прирост'] = [None] + chains_increase1
df1.at[0,'Средний уровень ряда'] = avarage_level1
df1.at[0,'Средние абсолютный прирост'] = abs_avarage_level1
df1.at[0,'Средний темп роста, %'] = growth_avarage_level1 
df1.at[0,'Средний темп прироста.%'] = avarage_increase_temp1
df1['Метод прогнозирования'] = np.nan
df1.at[0, 'Метод прогнозирования'] = 'по среднему абсолютному приросту'
df1.at[1, 'Метод прогнозирования'] = 'по среднему темпу роста'
df1.at[2, 'Метод прогнозирования'] = 'аналитическое выравнивание МНК'
df1['Прогноз'] = np.nan
df1.at[0, 'Прогноз'] = prediction_abs_avarage_increase1
df1.at[1, 'Прогноз'] = prediction_growth_avarage_level1
df1.at[2, 'Прогноз'] = prediction_analytical_alignment1
df1.at[0, 'Факт'] = 1966.8
relative_accuracy1.extend([np.nan] * (len(df1) - len(relative_accuracy1)))
df1['Относительная погрешность δ'] = relative_accuracy1


if os.path.exists('lab3_updated.xlsx'):
    os.remove('lab3_updated.xlsx')
df1.to_excel('lab3_updated.xlsx', index=False)


y_values = prediction_analytical_alignment_graphic(mas2)
plt.figure(figsize=(10, 15))  
plt.plot(mas1, mas2, marker='o')  
plt.plot(mas1, y_values, color='red')  

plt.xticks(mas1, rotation=45) 
plt.yticks(np.append(mas2, y_values)) 
plt.text(2020,2095, f'y={b(mas2)}x + {a(mas2)}')
plt.text(2020,2083, f'R\u00B2 = {prediction_coefficient(mas2)}')
plt.xlabel('Года') 
plt.ylabel('Кол-во преступлений, тысяч') 
plt.tight_layout()  
plt.show()  
print(avarage_increase_temp(mas2))
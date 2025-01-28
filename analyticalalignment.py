import numpy as np
from dynamics import *
def avarage_t(arr):
    return sum(range(1, len(arr) + 1)) / len(arr)

def square_t(arr):
    return sum(i**2 for i in range (1, len(arr)+1)) / len(arr)

def y_avarage(arr):
    return round(sum(arr)/len(arr),1)

def multiply_ty(arr):
    return round(sum([(i+1) * arr[i] for i in range(len(arr))])/len(arr),1)

def dispersion(arr):
    return square_t(arr) - pow(avarage_t(arr),2)

def b(arr):
    return round(((multiply_ty(arr) - y_avarage(arr) * avarage_t(arr))) / dispersion(arr),3)

def a(arr):
    return round(y_avarage(arr) - b(arr) * avarage_t(arr),2)

def prediction_analytical_alignment(arr):
    return round(b(arr) * (len(arr)+1) + a(arr),1)

def prediction_analytical_alignment_graphic(arr):
    return [b(arr) * i + a(arr) for i in range(1, len(arr)+ 1)]

def prediction_coefficient(arr):
    r = 0
    mas_sum_1 = []
    mas_sum_2 = []
    sum_chisl = 0
    sum_znam = 0
    for i in range (0, len(arr)):
        sum_chisl += pow(arr[i] - prediction_analytical_alignment_graphic(arr)[i],2)
        sum_znam  +=  pow(arr[i] - y_avarage(arr),2)
    r = 1 - sum_chisl/sum_znam
    return round(r,4)

def relative_accuracy(arr):
    a1 = round(abs(prediction_abs_avarage_increase(arr) - 1966.8) / 1966.8 * 100,2)
    a2 = round(abs(prediction_growth_avarage_level(arr) - 1966.8) / 1966.8 * 100,2)
    a3 = round(abs(prediction_analytical_alignment(arr) - 1966.8) / 1966.8 * 100,2)
    return [f'{a1}%', f'{a2}%' , f'{a3}%']

 

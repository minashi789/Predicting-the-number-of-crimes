def base_absolute_increase(arr):
    y = arr[0]
    return [round(x - y) for x in arr[1:]]

def base_growth(arr):
    y = arr[0]
    base_growth = []
    for i in range(1, len(arr)):
        base_growth.append(round((arr[i]/y)*100,1))
    return base_growth

def base_increase(arr):
    y = arr[0]
    base_increase = []
    for i in range(1, len(arr)):
        base_increase.append(round(((arr[i]-y)/y)*100,1))
    return base_increase

def chains_absolute_increase(arr):
    return [round(arr[i]-arr[i-1],2) for i in range(1,len(arr))]

def chains_growth(arr):
    chains_growth = []
    for i in range(1, len(arr)):
        chains_growth.append(round((arr[i]/arr[i-1])*100,1))
    return chains_growth

def chains_increase(arr):
    base_increase = []
    for i in range(1, len(arr)):
        base_increase.append(round(((arr[i]-arr[i-1])/arr[i-1])*100,1))
    return base_increase

def avarage_level(arr):
    return round(sum(arr)/(len(arr)),2)

def abs_avarage_level(arr):
    a = (arr[-1]-arr[0])
    b = len(arr)-1
    return round(a/b,1)

def growth_avarage_level(arr):
    return round(pow(arr[-1]/arr[0],1/(len(arr)-1))*100,2)

def avarage_increase_temp(arr):
    return round((growth_avarage_level(arr)-100),2)

def prediction_abs_avarage_increase(arr): 
    return arr[-1] + abs_avarage_level(arr)

def prediction_growth_avarage_level(arr):
    return round(arr[-1] * round((pow(arr[-1]/arr[0],1/(len(arr)-1))),2),1)



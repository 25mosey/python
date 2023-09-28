#1. Все отрицательные элементы массива заменить на их абсолютную величину
def replace_negative (tuple_data):
    new_tuple = tuple(abs(x)for x in tuple_data)
    return new_tuple
tuple1 = (1, -1 , -2 , 5 , 4)
tuple1 = replace_negative(tuple1)
print(tuple1)
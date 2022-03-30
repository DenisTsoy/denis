from time import perf_counter
from sys import getsizeof

start = perf_counter()
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = (src[index] for index in range(1, len(src)) if src[index] > src[index - 1])
print('Результат:', *result)
task_1 = perf_counter() - start
print('скорость выполнения:', task_1)
print('Память:', getsizeof(result))
result_1 = []
max = 1000
for index in src:
    if max == 1000:
        max = index
    else:
        if index > max:
            result_1.append(index)
        else:
            max = index
print('Результат:',result_1)
print('скорость выполнения:', perf_counter()-task_1)
print('Память:', getsizeof(result))

#два варианта решение задачи с генератором и без

# reduce是把一个函数作用在一个序列[x1, x2, x3, ...]上,这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 类似这种效果 reduce(f, [x1 ,x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce


def _execute(x, y):
    return x + y


def _reduce(fun, arr, init_num=None):
    if init_num is not None:
        ret = init_num
    else:
        ret = arr.pop(0)
    for temp in arr:
        ret = fun(ret, temp)
    return ret


print(_reduce(_execute, [1, 2, 3, 4]))
print(reduce(_execute, [1, 2, 3, 4]))

# filter()函数用于过滤序列
# filter()和map()类似，filter()也接收一个函数和一个序列
# 但和map()不同，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
# 类似下面实现原理


def _filter(fun, arr):
    _list = list([])
    for temp in arr:
        if fun(temp):
            _list.append(temp)
    return _list


def _execute(x):
    return type(x) is int


print(_filter(_execute, [1, "a", 1.50, 4, _execute, 6, None]))
print(list(filter(_execute, [1, "a", 1.50, 4, _execute, 6, None])))


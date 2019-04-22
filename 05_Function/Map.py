# map()是python内建的函数，map(fun,iterable),map函数接收两个参数，一个是回调函数，一个是迭代器
# 调用map(fun,iterable)方法，将会将让传入的fun函数依次作用到iterable迭代器的每个元素上
# 类似下面的实现


def execute(num):
    print(num)
    return num


def _map(fun, arr):
    _list = list([])
    for temp in arr:
        _list.append(fun(temp))
    return _list


_map(execute, [1, 3, 5, 7, 9])
list(map(execute, [1, 3, 5, 7, 9]))

# sorted()函数可以对list进行排序

# 从小到大排序
print(sorted([36, 1, -54, 8, -6, 0, 24, -5]))

# 从大到小排序
print(sorted([36, 1, -54, 8, -6, 0, 24, -5], reverse=True))

# 排序字符串，基于ASCII
print(sorted("python"))

# 排序字典
print(sorted({'q': 1, 'w': 2, 'e': 3, 'r': 4, 't': 5, 'y': 6}))

# sorted()函数也是一个高阶函数，sorted可以接收一个key函数来实现自定义排序

# 按绝对值大小排序
print(sorted([36, 1, -54, 8, -6, 0, 24, -5], key=abs))

# 根据字符长度进行排序
print(sorted(["36", "中", "abs", "Apple", "sad", "国", "#mmmmm", "_*"], key=len))


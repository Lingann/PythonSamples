# set和dict类似，也是一组key的集合，但不会存储value。由于key不能重复，所以再set中，没有重复的key
# 要创建一个set，需要提供一个list作为输入集合

# 第一种创建方式 关于代码提示
# 参考 下面的方式
#   * https://www.cnblogs.com/kaituorensheng/p/6139573.html
#   * https://stackoverflow.com/questions/36674083/why-is-it-possible-to-replace-sometimes-set-with
# 正常方法
_set = set([1, 2, 3])
# 第二种方法
_set2 = set((4, 2, 5))
# 推荐方法
_set3 = {1, 2, 3}

print(_set)

# 添加元素
_set.add(4)
print(_set)

# 移除元素
_set.remove(3)
print(_set)

# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作
print(_set & _set2)
print(_set | _set2)

# set的元素为不可变对象，及不能放入“引用类型”,只能为“值类型”

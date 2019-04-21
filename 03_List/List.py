# list 是python那种的一种数据类型：list，它是一种有序的集合，可以随时添加和删除其中的元素
_list = list(["老子", "墨子", "庄子", "孔子"])

# append方法可以往list中追加元素到末尾
_list.append("孟子")
print(_list)

# insert方法可以把元素插入到指定的位置，比如索引号为1的位置
_list.insert(1, "荀子")
print(_list)

# 要删除list末尾的元素，用pop()方法
_list.pop()
print(_list)

# 要删除list指定位置的元素，用pop(i)方法，其中i是索引位置
_list.pop(0)
print(_list)

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置
_list[0] = "孟子"
print(_list)

# * list里面的元素的数据类型也可以不同 ["庄子", 123, False]
# * list元素也可以是另一个list, ["墨家", "道家", ["孔子", "孟子"]]





# python内置了字典，dict全称dictionary，使用键-值(key-value)存储，具有极快的查找速度
_dict = dict({"老子": "道家", "墨子": "墨家", "庄子": "道家", "孔子": "儒家"})

print(_dict)

print(_dict["孔子"])


# 判断key是否存在
if "孟子" in _dict:
    print(True)
else:
    print(False)

if _dict.get("墨子") is None:
    print(False)
else:
    print(True)

if _dict.get("荀子", -1) == -1:
    print(False)
else:
    print(True)

# 删除一个Key
_dict.pop("老子")

print(_dict)

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的

# 和list比较，dict有以下几个特地:
#   * 1. 查找和插入的速度极快，不会随着key的增加而变慢
#   * 2. 需要占用大量的内存，内存浪费多
# 而list相反
#   * 1. 查找和插入的时间随着元素的增加而增加
#   * 2. 占用空间小，浪费内存很少
# 所以,dict是用空间来换取时间的一种方法
# 注意: dict的key必须是不可变对象



# python中，基本上封装是要靠规范来进行的，实际上就靠约定进行能不能访问成员


# python 中，对于私有变量有一下约定
# * 不应该直接访问以下划线为前缀的类的变量 如 class._variable 或class.__variable (实际上可以访问得到)
# * 由于python中没有private，所以对于私有变量，以下划线为开头进行命名，约定该变量为私有变量
# * 单下划线的变量，我们约定为只有子类可以访问，类似protected关键字，双下划线表示只有当前类可以访问，类似private关键字

# 构造函数类
class Teacher(object):
    # 类似 private __motto
    __motto = "留取丹心照汗青"
    # 类似 protected _age
    _age = 0

    def __init__(self, name, age):
        self.name = name
        self._age = age

    def say(self):
        self.__after_one_year()
        self._say_name()
        print(self.__motto, self._age)

    # 类似 private __after_one_year()
    def __after_one_year(self):
        self._age += 1

    # 类似protected _say_name()
    def _say_name(self):
        print(self.name)


tea = Teacher('琳', 18)

tea.say()
tea.say()
tea.say()


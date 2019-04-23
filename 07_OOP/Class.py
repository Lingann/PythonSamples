# 定义类
class Student(object):
    pass


# 实例化
stu = Student()

# 加入属性
stu.name = "王楠"

print(stu.name)


# 构造函数
class Teacher(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 实例化
tea = Teacher('琳', 60000)

print(tea.name, tea.age)


# 析构函数

class Person:

    def __init__(self):
        print("实例化时调用")

    def __del__(self):
        print("破坏时调用")


p = Person()

del p


# 静态函数
class Cat:
    voice = ""

    @staticmethod
    def say():
        print("喵喵喵?")


Cat.say()

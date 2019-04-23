# 继承
# 定义一个父类


class A:
    _fu = '青青子衿，悠悠我心。纵我不往，子宁不嗣音？' \
         '青青子佩，悠悠我思。纵我不往，子宁不来？' \
         '挑兮达兮，在城阙兮。一日不见，如三月兮。'

    def __init__(self):
        pass

    def say(self):
        print(self._fu)


# 定义一个子类 继承自A类
class B(A):
    def say_shi(self):
        self._fu = "诗经"
        print(self._fu)


a = A()
b = B()

b.say()
b.say_shi()
a.say()


# 多重继承
class C:
    __fu = "子衿"

    def say_fu(self):
        print(self.__fu)


class D(B, C):
    style = "国风"

    def say(self):
        self.say_shi()
        self.say_fu()
        print(self.style)


c = C()
d = D()
c.say_fu()
d.say()

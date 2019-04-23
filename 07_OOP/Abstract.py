# 抽象类的实现方法
# * https://pythonprogramminglanguage.com/abstract-base-classes/
import abc


# class Base(object):
#   __metaclass__ = abc.ABCMeta
#
#    def __init__(self):
#        raise Exception('Base is an abstract class and cannot be instantiated directly')


class BasePerson(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def walk(self):
        '''data'''

    @abc.abstractmethod
    def say(self):
        '''data'''


class Teacher(BasePerson):
    name = ''

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("正在走路...")

    def say(self):
        print(self.name)


tea = Teacher("琳")
tea.walk()
tea.say()

# 如果实例化一个抽象类，则会报错
s = BasePerson()

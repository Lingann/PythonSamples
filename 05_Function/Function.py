# 声明函数
def get_summation(num1, num2):
    return num1 + num2


# 调用函数
num = get_summation(2, 6)

print(num)


# 空函数 如果想定义一个什么事也不做的空函数，可以用 pass 语句
def nothing_to_do():
    pass


# pass不做任何事，pass不可打断函数执行，pass相当于占位符，当函数未定义完整时，可以先用pass进行占位，避免运行报错
def print_str(num1, num2):
    pass
    print(num1 + num2)
    return num1 + num2


print_str(2, 1)


# 函数返回多个值，在python中，允许函数返回多个值
def return_multiple_value():
    return 1, 2, 3, "孔子"


print(return_multiple_value())


# 回调函数
def execute_callback(callback):
    return callback()


def execute_print():
    return print("上下五千年")


execute_callback(execute_print)


# 递归函数
def summation(n):
    if n <= 0:
        return 0
    total = n + summation(n-1)
    print(total)
    return total


summation(10)


# 匿名函数
# 下面是一份关于匿名函数 lambda的说明指南，请不要过度和滥用lambda函数
# * https://treyhunner.com/2018/09/stop-writing-lambda-expressions/
print((lambda x: x + x)(4))

(lambda x: summation(x))(2)

# 经过导入发现， 无法通过import module_one 导入模块
# 这是因为在当前项目中，无法通过06_Module->package_one->module_one.py 的路径进行导入
# 实际上要导入可以通过相对路径进行导入，只需要在要导入的模块前添加 '.'
# 相对路径引入不能通过直接执行当前.py，否则会报错

# from package_one import module_one
# module_one.execute_print()

# from .module_one import *
# execute_print()

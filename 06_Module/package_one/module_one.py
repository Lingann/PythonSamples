#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 在python中，一个.py文件就称之为一个模块(Module) 这里的模块就是避免将所有代码写进一个.py文件里面

# Package 为了避免不同人命名相同的Module导致冲突，所以又加了一个新的概念，叫做包(Package)
# Package 实际上在python中就相当于文件夹目录
# 请注意，每一个包目录下面会有一个__init__.py文件

_str = "模块一"


def execute_print():
    print(_str)
    return

